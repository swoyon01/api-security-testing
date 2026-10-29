# 📏 How to Add a New Lab

Follow these steps every time you solve a lab, room, or challenge.

---

## Step 1 — Pick the topic folder

| Lab type | Folder |
|----------|--------|
| Login, sessions, password reset | `03-authentication/labs/` |
| JWT attacks | `03-authentication/labs/` |
| BOLA / BFLA / mass assignment | `04-authorization/labs/` |
| SQLi, XSS, SSRF, CORS, rate limits | `05-common-vulnerabilities/labs/` |
| crAPI / VAmPI / DVGA overall notes | `06-labs-practice/labs/` |
| OAuth, GraphQL, WebSockets | `10-advanced-apis/labs/` |
| Business logic and race conditions | `11-business-logic/labs/` |

## Step 2 — Name the file

Use this pattern, all lowercase, words separated by hyphens:

```
<platform>-<short-lab-name>.md
```

Examples:
- `portswigger-jwt-none-algorithm.md`
- `crapi-bola-vehicle-location.md`
- `vampi-auth-bypass.md`

## Step 3 — Write the lab file

1. Copy `templates/lab-writeup-template.md`.
2. Fill in every section. Leave nothing as template text.
3. Redact tokens, cookies, and passwords (replace them with `[REDACTED]`).

## Step 4 — Add screenshots (optional)

Save images in `labs/screenshots/` and link them:

```markdown
![Burp Repeater showing the 403 response](screenshots/crapi-bola-1.png)
```

## Step 5 — Update the tracking tables

1. In the topic's `README.md`, change ⬜ to ✅ and add the file name.
2. In the main `README.md`, update the Progress tracker and the Lab index.

## Step 6 — Check for secrets

```bash
grep -rniE "password|token|apikey|secret|bearer" . --exclude-dir=.git
```

Check any match. If it is a real credential, remove it before committing.

## Step 7 — Commit and push

```bash
git add .
git commit -m "<folder>: <what you did>"
git push
```

Example: `git commit -m "03-authentication: PortSwigger JWT none-algorithm lab"`
