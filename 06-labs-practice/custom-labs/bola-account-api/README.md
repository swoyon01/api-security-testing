# BOLA Lab: Accessing Another User's Account

> ⚠️ This is an intentionally vulnerable API for local learning.
> It uses fictional data and should not be deployed publicly.
> Test other systems only when you have explicit permission.

## Overview

In this lab, I practiced identifying Broken Object Level Authorization
(BOLA) using a small Python API.

The vulnerable API returned account information based on an account ID
without checking whether the requester owned that account.

I tested the vulnerable behavior, enabled an ownership check, and
retested the same requests.

- **Category:** OWASP API Security Top 10 — API1:2023 BOLA
- **Lab type:** Custom local API
- **Tools:** Python 3 and curl
- **Target:** `http://127.0.0.1:8000`
- **Data:** Fictional accounts

## What I learned

- Changing an object ID can expose another user's data when the API
  does not check ownership.
- The server must check authorization for each requested object.
- Authentication and authorization are different controls.
- An ownership check is not enough if the API trusts a user-controlled
  header as proof of identity.

## Lab accounts

| Account ID | Owner | Balance |
|---|---|---:|
| 101 | Alice | 100 |
| 102 | Bob | 200 |

The lab uses the `X-Lab-User` header to simulate a user identity.
This header is **not real authentication** because the client can
change its value.

## Requirements

- Python 3.9 or later
- curl

No additional Python packages are required.

## Part 1: Test the vulnerable API

### Step 1: Start the server

Run this command from the folder containing `api_lab.py`:

```bash
python3 api_lab.py
```

Expected server output:

```text
Lab running at http://127.0.0.1:8000 (secure=False)
```

Leave the server running and open a second terminal.

### Step 2: Request Alice's account

```bash
curl -i -H "X-Lab-User: alice" http://127.0.0.1:8000/accounts/101
```

Observed response:

```http
HTTP/1.0 200 OK
Content-Type: application/json

{"owner": "alice", "balance": 100}
```

Alice can access her own account.

### Step 3: Request Bob's account as Alice

Change the account ID from `101` to `102` while keeping Alice's header:

```bash
curl -i -H "X-Lab-User: alice" http://127.0.0.1:8000/accounts/102
```

Observed response:

```http
HTTP/1.0 200 OK
Content-Type: application/json

{"owner": "bob", "balance": 200}
```

**Finding:** The API returned Bob's data to a request claiming to be
Alice. The vulnerable mode did not check the account owner.

In a real application, this type of flaw could expose another user's
private information.

### Step 4: Request an account that does not exist

```bash
curl -i -H "X-Lab-User: alice" http://127.0.0.1:8000/accounts/103
```

Observed response:

```http
HTTP/1.0 404 Not Found
Content-Type: application/json

{"error": "Not found"}
```

This account is not present in the lab data. The `404` response does
not demonstrate an authorization check.


## Part 2: Enable the ownership check

Stop the server with `Ctrl+C`. Then restart it:

```bash
python3 api_lab.py --secure
```

The server should show:

```text
Lab running at http://127.0.0.1:8000 (secure=True)
```

The relevant code is:

```python
elif SECURE and account["owner"] != user:
    self.respond(403, {"error": "Access denied"})
```

This compares the account owner with the user supplied in the header.

### Retest the API

In another terminal, run:

```bash
# Alice requests her own account
curl -i -H "X-Lab-User: alice" http://127.0.0.1:8000/accounts/101

# Alice requests Bob's account
curl -i -H "X-Lab-User: alice" http://127.0.0.1:8000/accounts/102

# Bob requests his own account
curl -i -H "X-Lab-User: bob" http://127.0.0.1:8000/accounts/102
```

### My results

| Request | Vulnerable mode | Ownership-check mode |
|---|---|---|
| Alice requests Alice's account | 200 OK | 200 OK |
| Alice requests Bob's account | 200 OK | 403 Forbidden |
| Bob requests Bob's account | Not separately recorded | 200 OK |
| Alice requests nonexistent account | 404 Not Found | Not separately recorded |


The screenshot shows the server running with `secure=True` and
responses of `200`, `403`, and `200`. The server log does not show
the request headers; the identities above come from the curl requests
I ran during the experiment.

## Important limitation

The `--secure` option only enables an ownership check. It does **not**
make this API secure.

The server trusts the `X-Lab-User` header, so anyone can claim to be
Bob:

```bash
curl -i -H "X-Lab-User: bob" http://127.0.0.1:8000/accounts/102
```

The server returns Bob's account because it does not authenticate the
requester.

A real application must:

1. Authenticate the user using a validated credential or session.
2. Derive the user's identity from that validated credential.
3. Check whether that authenticated user can access the requested
   object.
4. Test both permitted and denied access.

## Conclusion

I reproduced a BOLA-style authorization problem by changing an
account ID. I then tested an ownership check and observed the
cross-account request return `403 Forbidden`.

The lab also showed why an authorization check must use a
**verified identity**, not a user-supplied name.

## References

- [OWASP API1:2023 — Broken Object Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)
- *API Security for White Hat Hackers* by Confidence Staveley — learning reference

This custom lab was developed with AI assistance and tested locally
using fictional data.

