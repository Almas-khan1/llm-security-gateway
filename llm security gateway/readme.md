
# LLM Security Gateway

A lightweight security layer for Large Language Models (LLMs) that detects **prompt injection attacks**, **PII leakage**, and enforces **policy-based access control** before sending requests to the model.

## Features

* Prompt Injection Detection
* Jailbreak & System Prompt Attack Detection
* PII Detection & Masking (using Presidio)
* Custom API Key Recognizer
* Policy-based Decision Engine (ALLOW / MASK / BLOCK)
* Latency Monitoring
* Integration with Ollama (local LLM)

##  Architecture Workflow

1. User Input
2. Injection Detection
3. PII Detection
4. Policy Decision
5. Action:

   * ALLOW → Send to LLM
   * mASK→ Anonymize sensitive data
   * BLOCK → Reject request

## Configuration (`config.py`)

* `INJECTION_THRESHOLD` → Score to block malicious input
* `PII_MASKING_ENABLED` → Enable/disable masking
* `PII_CONFIDENCE_THRESHOLD` → Detection sensitivity
* `MODEL_NAME` → LLM model (Ollama)


## Modules

### 1. Injection Detector

Detects:

* Prompt Injection
* Jailbreak Attempts
* System Prompt Extraction
* Data Exfiltration

Returns:

* Injection Score
* Attack Flags



### 2. PII Detector

* Uses Presidio for entity recognition
* Detects:

  * Phone numbers
  * Emails
  * API Keys (custom regex)

Supports anonymization of detected data.



### 3. Policy Engine

Decision logic:

* **BLOCK** → High injection score
* **MASK** → PII detected
* **ALLOW** → Safe input



### 4. Evaluation Module

Runs predefined test cases and reports:

* Expected vs Actual output
* Injection score
* PII count
* Latency



### 5. Main Pipeline

Handles:

* User input
* Security checks
* Model interaction
* Final response



##  Test Cases

Includes scenarios like:

* Normal queries
* Prompt injection attacks
* Jailbreak attempts
* System prompt extraction
* PII exposure (phone, API key)
* Mixed attacks



## How to Run


python main.py

For evaluation:


python evaluation.py

## Example Output

SECURITY REPORT
Injection Score: 2
Attack Flags: ['jailbreak']
PII Detected: 1
Policy Decision: MASK

## Future Improvements

* Machine learning–based injection detection
* Context-aware PII filtering
* Role-based access control
* Logging & monitoring dashboard

