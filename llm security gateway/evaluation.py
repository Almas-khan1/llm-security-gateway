import time
from injection_detector import detect_injection
from pii_detector import analyze_pii
from policy import decide_policy
from test_cases import test_inputs


def evaluate_system():
    results = []

    for case in test_inputs:
        text = case["text"]
        expected = case["expected"]

        start = time.time()

        score, _ = detect_injection(text)
        pii = analyze_pii(text)
        decision = decide_policy(score, pii)

        latency = (time.time() - start) * 1000

        results.append({
            "input": text,
            "expected": expected,
            "actual": decision,
            "score": score,
            "pii_count": len(pii),
            "latency": latency
        })

    return results


def print_results(results):
    print("\n--- Scenario Evaluation Table ---")
    for r in results:
        print("\nInput:", r["input"])
        print("Expected:", r["expected"])
        print("Actual:", r["actual"])
        print("Score:", r["score"])
        print("PII Count:", r["pii_count"])
        print("Latency(ms):", round(r["latency"], 2))


if __name__ == "__main__":
    results = evaluate_system()
    print_results(results)