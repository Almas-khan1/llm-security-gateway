import ollama
import time
from injection_detector import detect_injection
from pii_detector import analyze_pii, anonymize_text
from policy import decide_policy
from config import MODEL_NAME


def run_pipeline():
    user_input = input("Enter user prompt: ")

    start_time = time.time()

    # Step 1: Injection Detection
    injection_score, attack_flags = detect_injection(user_input)

    # Step 2: PII Detection
    pii_results = analyze_pii(user_input)

    # Step 3: Policy Decision
    decision = decide_policy(injection_score, pii_results)

    end_time = time.time()
    latency = (end_time - start_time) * 1000

    # Output Summary
    print("\n--- SECURITY REPORT ---")
    print("Injection Score:", injection_score)
    print("Attack Flags:", attack_flags)
    print("PII Detected:", len(pii_results))
    print("Policy Decision:", decision)

    # Policy Actions
    if decision == "MASK":
        masked = anonymize_text(user_input, pii_results)
        print("\nMasked Output:", masked)

    elif decision == "BLOCK":
        print("\nRequest Blocked due to security risk.")

    else:
        print("\nSafe Input:", user_input)

        response = ollama.chat(
         
model=MODEL_NAME,
            messages=[{"role": "user", "content": user_input}]
        )

        print("\nLLM Response:", response["message"]["content"])

    print("\nLatency:", latency, "ms")


if __name__ == "__main__":
    run_pipeline()