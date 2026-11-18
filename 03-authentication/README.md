# 03 · Authentication

**Goal:** learn how APIs verify identity, and how those checks fail.

## 📖 Checklist

- [x] PortSwigger authentication labs (5 solved) → [`labs/`](labs/)
- [x] PortSwigger JWT attack labs (5 solved) → [`labs/`](labs/)
- [x] API keys: header vs query vs cookie placement, and their risks → [`notes/01-api-keys-and-basic-auth.md`](notes/01-api-keys-and-basic-auth.md)
- [x] Basic Auth: Base64 is not encryption → [`notes/01-api-keys-and-basic-auth.md`](notes/01-api-keys-and-basic-auth.md)
- [x] Session tokens: cookie flags, fixation, invalidation → [`notes/02-sessions-and-tokens.md`](notes/02-sessions-and-tokens.md)
- [x] Brute force and credential stuffing protection → [`notes/03-brute-force-2fa-and-password-reset.md`](notes/03-brute-force-2fa-and-password-reset.md)
- [x] Password reset and 2FA flaws → [`notes/03-brute-force-2fa-and-password-reset.md`](notes/03-brute-force-2fa-and-password-reset.md)

## 📂 Folder Contents

| Path | What it holds |
|------|---------------|
| `notes/01-api-keys-and-basic-auth.md` | API key placement, Basic Auth risks, what to test |
| `notes/02-sessions-and-tokens.md` | Cookie flags, session fixation, logout and token checks |
| `notes/03-brute-force-2fa-and-password-reset.md` | Brute force, 2FA bypass, password reset flaws |
| `labs/` | Index of the PortSwigger authentication and JWT labs |

## ✅ Done When

- Each topic above has a note with what to test and how to fix it.
- Every solved PortSwigger lab is listed in `labs/README.md`.
- You have tested at least one API key or Basic Auth case on crAPI or VAmPI.
