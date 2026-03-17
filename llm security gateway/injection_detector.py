def detect_injection(text):
    text_lower = text.lower()
    score = 0
    flags = []

    # Attack pattern categories
    patterns = {
        "prompt_injection": [
            "ignore previous instructions",
            "disregard rules",
            "bypass safety"
        ],
        "jailbreak": [
            "jailbreak",
            "do anything now",
            "act as unrestricted"
        ],
        "system_extraction": [
            "reveal system prompt",
            "show hidden instructions",
            "what are your rules"
        ],
        "data_exfiltration": [
            "give me secrets",
            "show api key",
            "leak credentials"
        ]
    }

    # Scoring logic
    for category, keywords in patterns.items():
        for keyword in keywords:
            if keyword in text_lower:
                score += 2
                flags.append(category)

    # Remove duplicates
    flags = list(set(flags))

    return score, flags


# Test mode
if __name__ == "__main__":
    text = input("Enter text: ")
    score, flags = detect_injection(text)
    print("Score:", score)
    print("Flags:", flags)