# 02 · Session Tokens and Session Management

> After login, the server must remember who you are on every later request. It does this with a session token, usually a cookie or a bearer token. If that token is weak, leaked, or not invalidated, the account can be taken over.

---

## 🍪 Cookies vs Bearer Tokens

| | Session cookie | Bearer token |
|---|----------------|--------------|
| Sent by | The browser, automatically | The client, in the `Authorization` header |
| Typical use | Websites | APIs, mobile apps, single-page apps |
| Main risks | CSRF, XSS theft, fixation | Leaks in JavaScript storage, logs, and URLs |

---

## 🛡️ Cookie Flags to Check

Look at the `Set-Cookie` header after login in Burp:

```http
Set-Cookie: session=abc123; Path=/; HttpOnly; Secure; SameSite=Lax
```

| Flag | Purpose | If missing |
|------|---------|-----------|
| `HttpOnly` | JavaScript cannot read the cookie | XSS can steal the session |
| `Secure` | Cookie sent only over HTTPS | Cookie can leak over HTTP |
| `SameSite` | Limits cross-site sending | CSRF risk increases |

---

## 🎯 Session Attacks to Understand

### Session fixation
The attacker gets a session ID first, makes the victim log in with it, and then uses the same ID.

**Test:** note the session cookie before login, log in, and check whether the cookie value changed. If it did not change, the app may be vulnerable to fixation.

### Session not invalidated on logout
**Test:** log in, copy the token, log out, then send the old token again. A `200` means the session is still valid.

### Predictable or weak tokens
**Test:** log in several times and compare the tokens. Look for sequential numbers, timestamps, or short strings.

### Token in URL
**Test:** search the URL history for `session=` or `token=`. Tokens in URLs leak through logs and the `Referer` header.

### No expiry
**Test:** check whether the token still works after hours or days without activity.

---

## 🔁 Bearer Token Checks

- Does the API accept a token with the signature removed or changed? (JWT labs cover this in detail.)
- Does the token still work after password change?
- Is the token stored in `localStorage`, where JavaScript can read it?

---

## ✅ Secure Practice

- Generate long random session IDs, and issue a new one after login.
- Set `HttpOnly`, `Secure`, and `SameSite` on cookies.
- Expire sessions after inactivity and on logout.
- Invalidate all sessions after a password change.

---

## 🔗 References

- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [PortSwigger: Session management](https://portswigger.net/web-security/authentication)
