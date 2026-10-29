# 02 · Tools Setup

**Goal:** get every testing tool working on my own machine before starting the labs.

## 📖 Checklist

- [x] **Burp Suite Community:** proxy on `127.0.0.1:8080`, Repeater, Intruder, target scope → [`notes/01-burp-suite-setup.md`](notes/01-burp-suite-setup.md)
- [x] **Firefox + FoxyProxy:** Firefox sends traffic to Burp, and the Burp CA certificate is trusted → [`notes/01-burp-suite-setup.md`](notes/01-burp-suite-setup.md) (step 3 and 4)
- [x] **Postman:** collections, environments, variables, and tests → [`notes/02-postman-setup.md`](notes/02-postman-setup.md)
- [x] **curl:** headers, auth, JSON bodies, HEAD and OPTIONS requests → [`notes/03-curl-commands.md`](notes/03-curl-commands.md)
- [x] **Docker:** crAPI and VAmPI running locally → [`notes/04-docker-labs.md`](notes/04-docker-labs.md)

## 🧰 Environment

| Tool | Address or version used |
|------|-------------------------|
| Burp proxy | `127.0.0.1:8080` |
| crAPI | `http://localhost:8888` |
| VAmPI | `http://localhost:5000` |
| Mail catcher (crAPI) | `http://localhost:8025` |

## 📂 Notes in this folder

| File | Covers |
|------|--------|
| `notes/01-burp-suite-setup.md` | Burp install, proxy, Firefox, CA certificate, first capture |
| `notes/02-postman-setup.md` | Collections, environments, variables, tests, optional Burp routing |
| `notes/03-curl-commands.md` | Options, GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS commands, tokens |
| `notes/04-docker-labs.md` | Docker install, starting and stopping crAPI and VAmPI, safety rules |

## ✅ Done When

- Burp captures traffic from Firefox.
- Postman sends a request from the collection and its tests pass.
- `curl` returns a response for GET and HEAD.
- crAPI and VAmPI both respond locally.
