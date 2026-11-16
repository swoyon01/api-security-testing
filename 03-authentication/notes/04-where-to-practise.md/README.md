# 04Where to Practise: Authentication, Sessions, and 2FA

This guide lists free, legal practice environments for each authentication topic in this folder.

> **Rule:** only test systems you own, run locally, or have written permission to test. Never test a real website without permission.

---

## Recommended Labs by Topic

| Topic | Primary lab | Additional options |
|-------|-------------|--------------------|
| Brute force and account lockout | PortSwigger: *Broken brute-force protection, IP block* | DVWA: *Brute Force* module |
| 2FA bypass and broken logic | PortSwigger: *2FA simple bypass*, *2FA broken logic*, *2FA bypass using a brute-force attack* | OWASP Juice Shop: two-factor authentication challenges |
| Password reset flaws | PortSwigger: *Password reset broken logic*, *Password reset poisoning via middleware* | crAPI: forgot-password flow (OTP sent by email) |
| Username enumeration | PortSwigger: *Username enumeration via different responses*, *Username enumeration via response timing* | VAmPI: login endpoints |
| Session cookies and session IDs | PortSwigger: *Brute-forcing a stay-logged-in cookie* | DVWA: *Weak Session IDs* module |
| Session fixation and logout | DVWA: *Weak Session IDs* | crAPI: token behaviour after logout; Juice Shop login challenges |
| API keys and Basic Auth | VAmPI: Basic Auth and token endpoints | crAPI: requests with and without the token |
| JWT attacks | PortSwigger: JWT labs (completed) | crAPI tokens; Juice Shop JWT challenges |

---

## Practice Environments

### PortSwigger Web Security Academy (free, browser-based)

- Authentication labs: <https://portswigger.net/web-security/authentication>
- Start with Apprentice labs, then move to Practitioner.
- Use Burp Repeater and Intruder, as in your completed labs.

### OWASP crAPI (local, Docker)

- Already set up at `http://localhost:8888`.
- Use it for login and token checks, the forgot-password OTP flow (codes arrive in MailHog at `http://localhost:8025`), and API key or token placement.

### VAmPI (local, Docker)

```bash
docker run -p 5000:5000 erev0s/vampi
```

Use it for Basic Auth, token login, and checking which endpoints require a token. The API runs at `http://localhost:5000`.

### DVWA: Damn Vulnerable Web Application (local, Docker)

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

1. Open `http://localhost` and log in with `admin` / `password`.
2. Open **DVWA Security** and set the level to **Low**.

Modules to use:
- **Brute Force**: login brute force.
- **Weak Session IDs**: session ID patterns and cookie inspection.
- **CSRF**: cross-site request forgery basics.

### OWASP Juice Shop (local, Docker)

```bash
docker run -p 3000:3000 bkimminich/juice-shop
```

Open `http://localhost:3000`. Use the **Score Board** page to find authentication and 2FA challenges, and use the hints when you are stuck.

### TryHackMe (browser-based, free tier)

Search the room list for **"Broken Authentication"** and **"Authentication Bypass"**.

---

## Suggested Order

| Step | Practice | Why |
|:----:|----------|-----|
| 1 | DVWA: Weak Session IDs (Low) | See how session cookies behave in Burp |
| 2 | Brute force: DVWA, then PortSwigger IP-block lab | Learn lockout and rate-limit testing |
| 3 | Password reset: PortSwigger, then crAPI forgot-password | Learn reset token and logic flaws |
| 4 | 2FA: PortSwigger *simple bypass*, then *broken logic* | Learn step-skipping and code-checking flaws |
| 5 | API keys and Basic Auth: VAmPI, with and without the header | Learn credential placement |
| 6 | Juice Shop challenges | Apply what you have learned |

---

## Recording Your Practice

For each lab you complete:

1. Write a short report using `templates/lab-writeup-template.md`.
2. Add the lab to the index in `03-authentication/labs/README.md`.
3. Update the checklist in `03-authentication/README.md`.

---

## References

- [PortSwigger: Authentication vulnerabilities](https://portswigger.net/web-security/authentication)
- [DVWA (Damn Vulnerable Web Application)](https://github.com/digininja/DVWA)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [VAmPI](https://github.com/erev0s/VAmPI)
- [OWASP crAPI](https://github.com/OWASP/crAPI)
