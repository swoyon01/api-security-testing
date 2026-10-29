# 🗺️ API Security Testing — Step-by-Step Roadmap

This roadmap is ordered. Finish each phase's **Done when** checklist before moving on.

**Pace:** 1.5–2 hours per day. Adjust the timing to your own schedule.

---

## Phase 0 — Setup (1–2 days)

**Learn:** what a virtual machine is, what Docker does, what a "lab" is.

**Do:**
1. Install Burp Suite Community, Postman, Docker, and Python 3.
2. Install Firefox and the FoxyProxy add-on. Point FoxyProxy at `127.0.0.1:8080`.
3. Install Burp's CA certificate in Firefox.
4. Start crAPI and VAmPI (see the README).

**Done when:** Burp intercepts Firefox traffic and crAPI loads at `http://localhost:8888`.

---

## Phase 1 — Basics (1 week)

**Learn:** client/server model, HTTP methods, status codes, headers, JSON, REST resources.

**Do:** send 20+ requests to `https://jsonplaceholder.typicode.com` in Postman. Write one-page notes on methods and status codes.

**Done when:** you can read any JSON response and build a request for any REST endpoint.

---

## Phase 2 — Tools (1–2 weeks)

**Learn:** Burp Proxy, Repeater, Intruder, and target scope; Postman collections and environments; curl.

**Do:** build a Postman collection for crAPI. Send one request in Repeater, change one value, and compare the responses.

**Done when:** you can intercept, modify, and resend a request in Burp without help.

---

## Phase 3 — Reconnaissance (1–2 weeks)

**Learn:** finding Swagger/OpenAPI documents, old API versions, hidden paths, and endpoints in JavaScript.

**Do:** import the crAPI OpenAPI spec into Postman. Build a full endpoint inventory. Run `ffuf` against a lab.

**Done when:** you can produce a complete endpoint list for a lab from scratch.

---

## Phase 4 — Authentication (2 weeks)

**Learn:** API keys, Basic Auth, session tokens, brute force, password reset flaws, 2FA bypass.

**Do:** complete the PortSwigger Authentication labs and write up each one.

**Done when:** you can explain and reproduce at least one authentication bypass in a lab.

---

## Phase 5 — JWT (1–2 weeks)

**Learn:** JWT structure, claims, `alg:none`, weak secrets, `kid` injection, algorithm confusion.

**Do:** complete the PortSwigger JWT labs. Decode and re-sign a token in Python.

**Done when:** you can decode, modify, and re-sign a JWT in any lab.

---

## Phase 6 — Authorization ⭐ (3–4 weeks)

The most important API risk category.

| Week | Topic | Practice |
|:----:|-------|----------|
| 1 | BOLA / IDOR (API1) | Two accounts in crAPI; change object IDs |
| 2 | BFLA (API5) | Call admin endpoints with a normal user token |
| 3 | BOPLA / mass assignment (API3) | Send `"role":"admin"` in profile updates |
| 4 | Review | Use the Burp Autorize extension; write `bola_checker.py` |

**Done when:** you have documented one BOLA, one BFLA, and one BOPLA with reproducible steps.

---

## Phase 7 — Injection (2 weeks)

**Learn:** SQL injection in JSON bodies and headers; XSS through API responses; NoSQL injection.

**Do:** test a VAmPI parameter for SQLi. Complete the PortSwigger SQLi and XSS labs.

**Done when:** you can extract data from a database through an API parameter.

---

## Phase 8 — Server-Side Issues (2 weeks)

**Learn:** SSRF (API7), security misconfiguration (API8), CORS, verbose errors.

**Do:** complete the PortSwigger SSRF and CORS labs. Check CORS headers in crAPI with Repeater.

**Done when:** you can make a lab server request an internal address and explain a CORS misconfiguration.

---

## Phase 9 — Resource Consumption (1 week)

**Learn:** rate limits, HTTP 429, bypass via headers such as `X-Forwarded-For`, large page sizes (API4).

**Do:** write a short Python loop that sends login attempts and records when 429 appears.

**Done when:** you have shown evidence that a limit is missing or bypassable in a lab.

---

## Phase 10 — Business Logic (1–2 weeks)

**Learn:** sensitive business flows (API6), coupon abuse, skipped steps, race conditions.

**Do:** complete the PortSwigger business logic and race condition labs.

**Done when:** you can break a workflow in a lab and explain its impact.

---

## Phase 11 — Advanced API Types (3–4 weeks)

| Topic | What to learn | Practice |
|-------|---------------|----------|
| OAuth 2.0 / OIDC | `redirect_uri` manipulation, `state` parameter, token leakage | PortSwigger OAuth labs |
| GraphQL | Introspection, IDOR via arguments, batching | PortSwigger GraphQL labs, DVGA |
| WebSockets | Intercepting and modifying messages | PortSwigger WebSocket labs |
| gRPC | Protocol Buffers basics, reading traffic | Overview only |
| Unsafe consumption (API10) | Trusting third-party API data | Read and write a note |

**Done when:** you have completed at least one OAuth lab and one GraphQL lab.

---

## Phase 12 — Automation (ongoing from Phase 6)

Build one script per phase:

| Script | Purpose |
|--------|---------|
| `bola_checker.py` | Compare object access across two users |
| `jwt_decoder.py` | Decode and print a JWT header and payload |
| `endpoint_finder.py` | Check a wordlist of paths on a lab |
| `rate_limit_test.py` | Count requests until a 429 appears |

**Done when:** each script runs with one command and has a usage example in its docstring.

---

## Phase 13 — Full Practice & First Report (ongoing)

1. Solve all crAPI challenges and write a report for each.
2. Finish the remaining PortSwigger API-related labs.
3. Read 10 publicly disclosed reports on HackerOne Hacktivity.
4. Choose a bug bounty program with **API in scope**. Read its policy first.
5. Recon → test one endpoint → write a report with steps, impact, and a fix.

**Done when:** you have submitted your first report.

---

## 📌 Next Actions

1. Create the folders listed in the README structure.
2. Move your PortSwigger Authentication, JWT, and SQLi write-ups into their topic folders.
3. Set up crAPI using the official Docker Compose method.
