from config import INJECTION_THRESHOLD, PII_MASKING_ENABLED

def decide_policy(injection_score, pii_results):
    """
    Decide system action based on risk signals.
    """

    if injection_score >= INJECTION_THRESHOLD:
        return "BLOCK"

    elif PII_MASKING_ENABLED and len(pii_results) > 0:
        return "MASK"

    else:
        return "ALLOW"