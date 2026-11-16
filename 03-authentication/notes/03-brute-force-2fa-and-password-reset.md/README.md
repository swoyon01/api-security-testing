# 03 · Brute Force, Credential Stuffing, 2FA, and Password Reset

> These are the most common ways to attack the login process. Most of them come from missing limits or from logic mistakes, not from broken cryptography.

---

## 🔨 Brute Force and Credential Stuffing

| Attack | What it does | Example |
|--------|--------------|---------|
| Brute force | Tries many passwords for one account | Trying a password list against `admin` |
| Credential stuffing | Tries leaked username and password pairs | Reusing a breach list on another site |
| Password spraying | Tries one common password on many accounts | `Summer2026!` on every user |

### Test for missing protection

1. Send 20 wrong logins for one account in Intruder (lab only).
2. Check for:
   - A lockout or a `429 Too Many Requests` response
   - A CAPTCHA or a delay that increases
   - An alert or a notification email
3. If nothing changes, the protection is missing.

### Bypass ideas that labs use

- **IP-based block:** the server may trust a header such as `X-Forwarded-For`. Change its value per request and see whether the block resets.
- **Counter reset:** a successful login for your own account may reset the counter. Use this to test whether the reset happens at the right time.
- **Multiple credentials per request:** some APIs accept a list in one request, which counts as one attempt.

---

## 🔢 Two-Factor Authentication (2FA)

### Common flaws

- **Skipping the step:** after the password, go straight to a page that is only meant for logged-in users.
- **Changing the account in the second step:** the 2FA code is checked against the username in a cookie or hidden field, so you can change that value.
- **No limit on code attempts:** a 4-digit or 6-digit code can be brute-forced.
- **Code not tied to the session:** a code requested for one account works for another.

### What to test

1. Log in with valid credentials and stop at the 2FA page.
2. Browse to a logged-in page directly.
3. Change any `username` or `verify` value in the second-step request.
4. Count how many wrong codes you can send before a lockout.

---

## 🔁 Password Reset Flaws

| Flaw | Test |
|------|------|
| Token is predictable | Request two resets and compare the tokens |
| Token does not expire | Use an old token after a long wait |
| Token is reused | Use the same token twice |
| Token is returned in the response | Check the reset response body |
| Reset works for another user | Change the `username` or `email` in the reset request |
| Host header poisoning | Change `Host` to your server and check whether the reset link points there |

---

## 🛡️ Secure Practice

- Rate-limit logins by account and by IP, and add lockout or delay.
- Use the same error message for "user not found" and "wrong password".
- Bind 2FA codes to the session and limit attempts.
- Make reset tokens random, short-lived, and single-use. Send them only to the registered email.
- Check the username on every step of a multi-step login.

---

## 🔗 References

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [PortSwigger: Authentication vulnerabilities](https://portswigger.net/web-security/authentication)
