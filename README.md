<div align="center">

# 🔐 API Security Testing — Learning Journey

[![Status](https://img.shields.io/badge/Status-Active%20Learning-brightgreen?style=for-the-badge)](#-progress-tracker)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Focus](https://img.shields.io/badge/Focus-REST%20%26%20GraphQL%20Security-critical?style=for-the-badge)](#-learning-path)
[![OWASP](https://img.shields.io/badge/OWASP-API%20Top%2010%202023-orange?style=for-the-badge)](https://owasp.org/API-Security/)

> A hands-on, documented journey through **API security testing** — from HTTP fundamentals to real-world bug bounty reporting.
> Every topic, lab solution, script and note in this repository is written so that a beginner can follow the same path.

[Learning Path](#-learning-path) •
[Progress](#-progress-tracker) •
[Repository Structure](#-repository-structure) •
[Labs](#-lab-index) •
[OWASP API Top 10](#-owasp-api-security-top-10-2023) •
[Setup](#-lab-setup) •
[Upload Workflow](#-how-to-add-new-work) •
[Resources](#-resources)

</div>

---

## 👤 About

| | |
|---|---|
| **Author** | Saber Hasan Swoyon |
| **Background** | Software Engineering undergraduate |
| **Goal** | Master API security → bug bounty → Application Security (AppSec) career |
| **Main portfolio** | [cybersecurity-labs](https://github.com/swoyon01/cybersecurity-labs) |
| **Tech stack** | Python · Linux · Burp Suite · Postman · Docker |

This repository is my centralized learning hub. Each folder covers one topic and contains my **notes**, **lab write-ups**, and **scripts**.

---

## 🧭 Where to Start

| If you want to see… | Go to |
|---|---|
| 🗺️ The full learning plan | [ROADMAP.md](ROADMAP.md) |
| 🔐 Authentication and JWT work | [`03-authentication/`](03-authentication/) |
| 🚪 Authorization (BOLA / BFLA / BOPLA) | [`04-authorization/`](04-authorization/) |
| 💉 Injection and server-side work | [`05-common-vulnerabilities/`](05-common-vulnerabilities/) |
| 🐍 Python testing tools | [`12-scripts/`](12-scripts/) |
| ✍️ Lab write-up template | [`templates/`](templates/) |
| 📏 How to add a new lab | [HOW_TO_ADD_NEW_LAB.md](HOW_TO_ADD_NEW_LAB.md) |
| 🛡️ My broader portfolio | [cybersecurity-labs](https://github.com/swoyon01/cybersecurity-labs) |

---

## ⚠️ Legal & Ethical Notice

All testing in this repository is performed only on:

- ✅ Intentionally vulnerable labs: **PortSwigger Web Security Academy**, **TryHackMe**, **OWASP crAPI**, **VAmPI**, **DVGA**
- ✅ Systems I own or run locally
- ✅ Bug bounty programs where the target is **explicitly in scope**

No write-up in this repository targets a real third-party service. Unauthorized testing is illegal.

---

## 🗺️ Learning Path

The path is ordered. Each phase builds on the one before it.

| Phase | Topics | Folder | Status |
|:-----:|--------|--------|:------:|
| **0** | Setup — Burp, Postman, Docker, lab environments | [`02-tools-setup`](02-tools-setup/) | ✅ |
| **1** | Web & HTTP fundamentals, REST APIs, JSON | [`01-basics`](01-basics/) | ✅ |
| **2** | Tools — Burp Suite, Postman, curl | [`02-tools-setup`](02-tools-setup/) | ✅ |
| **3** | API reconnaissance — Swagger/OpenAPI, endpoint discovery | [`09-recon`](09-recon/) | ⬜ |
| **4** | Authentication — API keys, sessions, brute force, 2FA | [`03-authentication`](03-authentication/) | ✅ |
| **5** | JWT attacks — `alg:none`, weak secrets, `kid`, algorithm confusion | [`03-authentication`](03-authentication/) | ✅ |
| **6** | Authorization — BOLA/IDOR, BFLA, BOPLA / mass assignment | [`04-authorization`](04-authorization/) | ⬜ |
| **7** | Injection — SQL injection, XSS, NoSQL, command injection | [`05-common-vulnerabilities`](05-common-vulnerabilities/) | 🟡 |
| **8** | Server-side — SSRF, misconfiguration, verbose errors, CORS | [`05-common-vulnerabilities`](05-common-vulnerabilities/) | ⬜ |
| **9** | Resource consumption — rate limiting, brute-force protection | [`05-common-vulnerabilities`](05-common-vulnerabilities/) | ⬜ |
| **10** | Business logic — sensitive flows, race conditions | [`11-business-logic`](11-business-logic/) | ⬜ |
| **11** | Advanced API types — OAuth 2.0 / OIDC, GraphQL, WebSockets, gRPC | [`10-advanced-apis`](10-advanced-apis/) | ⬜ |
| **12** | Automation — Python tools for repeatable testing | [`12-scripts`](12-scripts/) | 🟡 |
| **13** | Full practice — complete labs, reporting, first bug bounty | [`13-bug-bounty-reporting`](13-bug-bounty-reporting/) | ⬜ |

A detailed step-by-step plan with weekly goals is in [ROADMAP.md](ROADMAP.md).

---

## 📊 Progress Tracker

**Overall:** `5 of 14 phases complete` · **PortSwigger labs solved:** 13 (SQL Injection 6 · Authentication 4 · JWT 3) · **TryHackMe rooms completed:** 5 · **Scripts:** 1 in progress

> The full PortSwigger record lives in the [main portfolio](https://github.com/swoyon01/cybersecurity-labs). This repo focuses on **API-specific** work.

| Category | Folder | Done | In progress | Not started |
|----------|--------|:----:|:-----------:|:-----------:|
| Basics (HTTP, REST, JSON) | `01-basics` | 3 | 0 | 1 |
| Tools setup | `02-tools-setup` | 3 | 1 | 0 |
| Authentication | `03-authentication` | 2 | 0 | 2 |
| Authorization | `04-authorization` | 0 | 0 | 3 |
| Common vulnerabilities | `05-common-vulnerabilities` | 0 | 1 | 5 |
| Labs & practice | `06-labs-practice` | 0 | 0 | 4 |
| Notes & cheatsheets | `07-notes` | 0 | 0 | 2 |
| Resources | `08-resources` | 0 | 0 | 3 |
| Recon | `09-recon` | 0 | 0 | 3 |
| Advanced APIs | `10-advanced-apis` | 0 | 0 | 4 |
| Business logic | `11-business-logic` | 0 | 0 | 2 |
| Scripts | `12-scripts` | 0 | 1 | 2 |
| Bug bounty & reporting | `13-bug-bounty-reporting` | 0 | 0 | 3 |

**Legend:** ✅ Done · 🟡 In progress · ⬜ Not started

> Update this table every time you finish a lab. Keep the counts in sync with the topic folders.

---

## 📁 Repository Structure

```
api-security-testing/
│
├── README.md                       ← Main page (this file)
├── ROADMAP.md                      ← Detailed step-by-step learning plan
├── LICENSE                         ← MIT License
├── .gitignore                      ← Files Git must never upload
│
├── 01-basics/                      ← HTTP, REST, JSON
├── 02-tools-setup/                 ← Burp, Postman, curl, Docker labs
├── 03-authentication/              ← API keys, sessions, JWT, brute force
├── 04-authorization/               ← BOLA/IDOR, BFLA, BOPLA
├── 05-common-vulnerabilities/      ← SQLi, XSS, SSRF, rate limits, misconfig
├── 06-labs-practice/               ← Lab-by-lab write-ups (crAPI, VAmPI, PortSwigger, TryHackMe)
├── 07-notes/                       ← OWASP summary, cheatsheets
├── 08-resources/                   ← Courses, books, videos, platforms
├── 09-recon/                       ← Endpoint discovery and API documentation
├── 10-advanced-apis/               ← OAuth/OIDC, GraphQL, WebSockets, gRPC
├── 11-business-logic/              ← Workflow abuse, race conditions
├── 12-scripts/                     ← My Python testing tools
└── 13-bug-bounty-reporting/        ← Report templates, responsible disclosure
```

**Each topic folder contains:**
- `README.md` — what I learned and the lab checklist
- `labs/` — one write-up per solved lab
- `notes/` — my own study notes (optional)

---

## 🧪 Lab Index

### PortSwigger Web Security Academy

| # | Topic | Difficulty | Status | Write-up |
|:-:|-------|:----------:|:------:|----------|
| 1 | Authentication (4 solved) | Apprentice → Practitioner | ✅ | `03-authentication/labs/` |
| 2 | JWT attacks (3 solved) | Apprentice → Practitioner | ✅ | `03-authentication/labs/` |
| 3 | SQL injection (6 solved) | Apprentice → Practitioner | ✅ | `05-common-vulnerabilities/labs/` |
| 4 | API testing | Apprentice → Practitioner | ⬜ | — |
| 5 | Access control (IDOR) | Apprentice → Practitioner | ⬜ | — |
| 6 | SSRF | Apprentice → Practitioner | ⬜ | — |
| 7 | OAuth authentication | Apprentice → Practitioner | ⬜ | — |
| 8 | GraphQL | Apprentice → Practitioner | ⬜ | — |
| 9 | CORS | Apprentice → Practitioner | ⬜ | — |
| 10 | WebSockets | Apprentice → Practitioner | ⬜ | — |
| 11 | Business logic | Apprentice → Practitioner | ⬜ | — |
| 12 | Race conditions | Practitioner → Expert | ⬜ | — |

### OWASP crAPI — Completely Ridiculous API

| # | Challenge | Vulnerability | Status | Write-up |
|:-:|-----------|---------------|:------:|----------|
| 1 | Setup & first login | Environment | ⬜ | `06-labs-practice/` |
| 2 | Challenge 1 | BOLA | ⬜ | — |
| 3 | Challenge 2 | Broken authentication | ⬜ | — |
| 4 | Challenge 3 | BOPLA (excessive data) | ⬜ | — |
| 5 | Challenge 4 | BFLA | ⬜ | — |
| 6 | Challenge 5 | Resource consumption | ⬜ | — |

> Fill in challenge names as you solve them.

### VAmPI — Vulnerable API

| # | Challenge | Vulnerability | Status | Write-up |
|:-:|-----------|---------------|:------:|----------|
| 1 | Setup | Environment | ⬜ | `06-labs-practice/` |
| 2 | Auth bypass | Broken authentication | ⬜ | — |
| 3 | Object access | BOLA | ⬜ | — |

### TryHackMe

| # | Room | Topic | Status |
|:-:|------|-------|:------:|
| 1 | Brooklyn Nine Nine | CTF / Linux commands | ✅ |
| 2 | Bolt Room | Web / CTF | ✅ |
| 3 | Hacker Bounty | CTF / Web | ✅ |
| 4 | Ignite | Web / CTF | ✅ |
| 5 | Pickle Rick | CTF / Linux privesc | ✅ |
| 6 | OWASP API Security Top 10 rooms | API security | ⬜ |

**Legend:** ✅ Completed · 🟡 In progress · ⬜ Not started

---

## 🎯 OWASP API Security Top 10 (2023)

| ID | Risk | Covered in | Status |
|:--:|------|-----------|:------:|
| API1 | Broken Object Level Authorization (BOLA) | `04-authorization` | ⬜ |
| API2 | Broken Authentication | `03-authentication` | ✅ |
| API3 | Broken Object Property Level Authorization (BOPLA) | `04-authorization` | ⬜ |
| API4 | Unrestricted Resource Consumption | `05-common-vulnerabilities` | ⬜ |
| API5 | Broken Function Level Authorization (BFLA) | `04-authorization` | ⬜ |
| API6 | Unrestricted Access to Sensitive Business Flows | `11-business-logic` | ⬜ |
| API7 | Server-Side Request Forgery (SSRF) | `05-common-vulnerabilities` | ⬜ |
| API8 | Security Misconfiguration | `05-common-vulnerabilities` | ⬜ |
| API9 | Improper Inventory Management | `09-recon` | ⬜ |
| API10 | Unsafe Consumption of APIs | `10-advanced-apis` | ⬜ |

**Status key:** ✅ Practiced in a lab · 🟡 Learning · ⬜ Not started

---

## 📚 Topic Checklist

### 01 — Basics
- [x] HTTP methods (GET, POST, PUT, PATCH, DELETE, OPTIONS)
- [x] Status codes (1xx–5xx)
- [x] REST resources, endpoints, and JSON
- [ ] API vs website differences

### 02 — Tools Setup
- [ ] Burp Suite Community — Proxy, Repeater, Intruder, Target scope
- [ ] Firefox + FoxyProxy
- [ ] Postman — collections, environments, variables, tests
- [ ] curl — headers, auth, JSON bodies
- [ ] Docker — running crAPI and VAmPI

### 03 — Authentication
- [x] Authentication labs (PortSwigger, 4 solved)
- [x] JWT attack labs (PortSwigger, 3 solved)
- [ ] API keys — header vs query vs cookie placement
- [ ] Basic Auth (Base64 is not encryption)
- [ ] Session tokens and session fixation
- [ ] Brute force and credential stuffing protection
- [ ] Password reset and 2FA flaws

### 04 — Authorization ⭐
- [ ] BOLA / IDOR — changing object IDs
- [ ] BFLA — calling admin functions with a low-privilege token
- [ ] BOPLA — mass assignment and excessive data exposure
- [ ] Testing with two accounts (Autorize extension)

### 05 — Common Vulnerabilities
- [x] SQL injection labs (PortSwigger, 6 solved)
- [ ] SQL injection in JSON bodies and headers
- [ ] XSS through API responses
- [ ] NoSQL injection
- [ ] SSRF — internal addresses, blind SSRF
- [ ] Rate limiting and 429 bypass
- [ ] CORS misconfiguration
- [ ] Verbose errors and stack traces

### 06 — Labs & Practice
- [ ] crAPI — all challenges
- [ ] VAmPI — all challenges
- [ ] DVGA — GraphQL challenges
- [ ] PortSwigger API, access control, SSRF labs

### 07 — Notes & Cheatsheets
- [ ] OWASP API Top 10 (2023) summary
- [ ] HTTP and status code cheatsheet
- [ ] Bug bounty tips

### 08 — Resources
- [ ] Course list (APIsec University, PortSwigger)
- [ ] Video playlists
- [ ] Practice platform list

### 09 — Recon
- [ ] Finding `/swagger`, `/api-docs`, `/openapi.json`
- [ ] Old versions (`/v1/`, `/v2/`) and hidden paths
- [ ] `ffuf`, `Kiterunner`, `Arjun`
- [ ] Reading JavaScript files for endpoints

### 10 — Advanced APIs
- [ ] OAuth 2.0 flows and `redirect_uri` attacks
- [ ] OpenID Connect basics
- [ ] GraphQL introspection and IDOR through queries
- [ ] WebSockets interception in Burp
- [ ] gRPC and Protocol Buffers basics

### 11 — Business Logic
- [ ] Sensitive business flows (coupons, balances, quantities)
- [ ] Race conditions
- [ ] Skipping steps in multi-step flows

### 12 — Scripts
- [x] `bola_checker.py` (in progress)
- [ ] `jwt_decoder.py`
- [ ] `rate_limit_test.py`
- [ ] `endpoint_finder.py`

### 13 — Bug Bounty & Reporting
- [ ] Reading program scope and rules
- [ ] CVSS severity scoring
- [ ] Writing reports: steps, impact, fix
- [ ] Responsible disclosure
- [ ] First report submitted

---

## 🛠️ Toolkit

| Category | Tool |
|----------|------|
| Operating system | Kali Linux (VirtualBox) |
| Browser | Firefox + FoxyProxy |
| Intercepting proxy | Burp Suite Community Edition |
| Burp extensions | Autorize, InQL, Logger++, Param Miner |
| API client | Postman |
| Fuzzing & discovery | ffuf, Kiterunner, Arjun |
| Mobile traffic | mitmproxy |
| Editor | VS Code |
| Language | Python 3 (`requests`, `pyjwt`) |

```bash
pip install requests pyjwt
```

---

## 🧰 Lab Setup

### OWASP crAPI (official method)

crAPI runs with Docker Compose from the official repository:

```bash
git clone https://github.com/OWASP/crAPI.git
cd crAPI/deploy/docker
docker compose -f docker-compose.yml --compatibility up -d
```

- Web app: `http://localhost:8888`
- Mail catcher: `http://localhost:8025`

### VAmPI

```bash
docker run -p 5000:5000 erev0s/vampi
```

- API: `http://localhost:5000`

> Always run these labs on your own machine, not on a shared or public network.

---

## 📝 Lab Write-up Format

Every lab write-up in this repository uses this structure:

```markdown
# Lab: [Name]

- Platform:
- Vulnerability:
- OWASP API Top 10 ID:
- Difficulty:
- Date solved:

## Goal
## Recon
## Steps to Reproduce
(exact HTTP requests, with tokens redacted)
## Impact
## Mitigation
## References
```

---

## 📤 How to Add New Work

1. Put the write-up in the matching topic's `labs/` folder, for example `03-authentication/labs/portswigger-jwt-none-alg.md`.
2. Put screenshots in `labs/screenshots/`. Blur or remove tokens and cookies first.
3. Update the checkbox and progress tables in this README.
4. Check for secrets before committing:
   ```bash
   grep -rniE "password|token|apikey|secret|bearer" . --exclude-dir=.git
   ```
5. Commit and push:
   ```bash
   git add .
   git commit -m "03-authentication: JWT none-alg lab write-up"
   git push
   ```

**Commit message format:** `<folder>: <what you did>`, for example `04-authorization: crAPI BOLA challenge 1`.

---

## 📚 Resources

### Books & documentation
- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — free labs
- *Hacking APIs* — Corey Ball
- *API Security in Action* — Neil Madden

### Courses
- APIsec University — free API security courses

### Video channels
- [InsiderPhD](https://www.youtube.com/@InsiderPhD) — bug bounty and API hacking
- [STÖK](https://www.youtube.com/@STOKfredrik) — recon and methodology
- [NahamSec](https://www.youtube.com/@NahamSec) — beginner-friendly bug bounty
- [HackerSploit](https://www.youtube.com/@HackerSploit) — labs and tools

### Practice platforms
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [TryHackMe](https://tryhackme.com)
- [Hack The Box](https://www.hackthebox.com)
- [OWASP crAPI](https://github.com/OWASP/crAPI) · [VAmPI](https://github.com/erev0s/VAmPI) · [DVGA](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application)

### Bug bounty platforms
- [HackerOne](https://hackerone.com) · [Bugcrowd](https://bugcrowd.com) · [Intigriti](https://www.intigriti.com)

---

## 📬 Contact

- GitHub: [@swoyon01](https://github.com/swoyon01)
- LinkedIn: [linkedin.com/in/swoyon](https://linkedin.com/in/swoyon)
- TryHackMe: [tryhackme.com/p/swoyon](https://tryhackme.com/p/swoyon)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

⭐ **Star this repository to follow the journey.**

*Learning one vulnerability at a time.*

</div>
