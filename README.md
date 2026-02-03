# Banking API Mock Server

A fully functional **mock banking API server** built using **WireMock** to simulate core banking services.  
This project enables testing of downstream systems **without dependency on real backend services**, which is a common requirement in enterprise QA and integration testing environments.

---

## Project Overview

In large-scale banking and financial systems, backend services are often unavailable, unstable, or costly to access during development and testing.  
This project solves that problem by providing **mocked REST APIs** that behave like real banking services and can be reliably used for:

- Integration testing
- Automation testing
- Contract testing
- CI/CD pipelines

Automated API tests are implemented using **Pytest**, and a detailed **HTML test report** is generated as the final output.

---

##  Mocked Banking APIs

| API | Method | Endpoint | Description |
|----|-------|---------|-------------|
| Account Balance | GET | `/api/v1/account/balance` | Fetch current account balance |
| Transaction History | GET | `/api/v1/account/transactions` | Retrieve account transactions |
| Fund Transfer | POST | `/api/v1/transfer` | Simulate fund transfer |

---

## Tech Stack

- **WireMock (Standalone)** – API mocking framework
- **Node.js** – Project orchestration & scripting
- **Python** – Test automation
- **Pytest** – API testing framework
- **pytest-html** – HTML test reporting
- **REST / JSON** – API communication

---
## Getting Started

### Prerequisites

- Java 8 or above
- Python 3.9+
- Node.js (optional, for scripts)
- WireMock Standalone JAR

---

### Running the Mock Server

From the project root directory:

```bash
java -jar wiremock-jre8-standalone-3.3.1.jar --port 8080 --root-dir wiremock
Expected output:
```
Loaded mappings from filesystem
Listening on port 8080

### Verify Mock APIs

#### Open in browser or Postman:
```
http://localhost:8080/api/v1/account/balance
http://localhost:8080/api/v1/account/transactions
```

#### WireMock Admin UI:
```
http://localhost:8080/__admin
```
### Running Automated Tests
#### Install dependencies
```
pip install -r requirements.txt
```
Run tests and generate report
```
pytest --html=reports/test_report.html
```
---

### Test Report Output
After execution, an HTML report will be generated at:
```
reports/test_report.html
```
The report includes:
Test execution summary

Passed/Failed test cases

Execution time

Assertion details

This report serves as test evidence and submission output.

---

### Enterprise Use Cases
Mocking unavailable banking services

Parallel development & testing

Automation testing without environment dependency

CI/CD pipeline integration

Performance-safe API simulations

### Key Learnings Demonstrated
API mocking using WireMock

Banking domain understanding

Automation testing with Pytest

Debugging HTTP 500 mock failures

Windows filesystem & environment troubleshooting

Test reporting and documentation

### Future Enhancements
Negative test scenarios (400 / 404 / 500)

Request body validation

API contract testing

CI pipeline using GitHub Actions

Dockerized version of WireMock

---

## Author
Davis Niranjan

###License
This project is intended for educational and portfolio purposes.


