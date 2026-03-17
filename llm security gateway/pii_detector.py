from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine
from config import PII_CONFIDENCE_THRESHOLD

# Initialize engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()



# 1. CUSTOM RECOGNIZER (API KEY)

def add_custom_recognizers():
    api_key_pattern = Pattern(
        name="api_key_pattern",
        regex=r"sk-[a-zA-Z0-9]{20,}",
        score=0.85
    )

    api_recognizer = PatternRecognizer(
        supported_entity="API_KEY",
        patterns=[api_key_pattern]
    )

    analyzer.registry.add_recognizer(api_recognizer)


# Call once
add_custom_recognizers()



# 2. PII ANALYSIS (WITH CONTEXT + CONFIDENCE FILTER)

def analyze_pii(text):
    results = analyzer.analyze(
        text=text,
        language='en'
    )

    # ---- Context-aware scoring ----
    text_lower = text.lower()

    for r in results:
        # Boost confidence if context matches
        if "phone" in text_lower and r.entity_type == "PHONE_NUMBER":
            r.score += 0.1

        if "email" in text_lower and r.entity_type == "EMAIL_ADDRESS":
            r.score += 0.1

        if "api key" in text_lower and r.entity_type == "API_KEY":
            r.score += 0.1

    # ---- Confidence calibration (filtering) ----
    filtered_results = [r for r in results if r.score >= PII_CONFIDENCE_THRESHOLD]

    return filtered_results



# 3. ANONYMIZATION (MASKING)

def anonymize_text(text, results):
    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )
    return anonymized.text



# TEST MODE

if __name__ == "__main__":
    text = input("Enter text: ")

    results = analyze_pii(text)

    print("\nDetected Entities:")
    for r in results:
        print(f"Type: {r.entity_type}, Score: {round(r.score, 2)}")

    if results:
        masked = anonymize_text(text, results)
        print("\nMasked Text:", masked)