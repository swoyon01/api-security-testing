# 04 · Docker and Lab Setup

> Docker runs the vulnerable apps (crAPI, VAmPI) in containers on your computer. Nothing needs to be installed directly on your system.

---

## 1. Install Docker

- **Windows / Mac:** install **Docker Desktop** and start it.
- **Linux:** install Docker Engine and the Compose plugin, then add your user to the `docker` group.

Check that it works:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

## 2. crAPI (OWASP Completely Ridiculous API)

Use the official repository and Docker Compose:

```bash
git clone https://github.com/OWASP/crAPI.git
cd crAPI/deploy/docker
docker compose -f docker-compose.yml --compatibility up -d
```

| Service | Address |
|---------|---------|
| crAPI web app | `http://localhost:8888` |
| Mail catcher (MailHog) | `http://localhost:8025` |

Stop it when you are done:

```bash
docker compose -f docker-compose.yml --compatibility down
```

## 3. VAmPI (Vulnerable API)

```bash
docker run -p 5000:5000 erev0s/vampi
```

| Service | Address |
|---------|---------|
| VAmPI | `http://localhost:5000` |

Stop it with `Ctrl+C`, or find the container with `docker ps` and run `docker stop <id>`.

## 4. Useful commands

```bash
docker ps                # running containers
docker logs <container>  # check errors
docker compose ps        # status of the crAPI stack
```

## 5. Safety rules

- Run labs only on your own machine. Do not expose them to a network or the internet.
- Do not reuse real passwords in lab accounts.
- Stop containers after each session to free memory.

## Setup checklist

- [x] `docker run --rm hello-world` succeeds
- [x] crAPI opens at `http://localhost:8888`
- [x] VAmPI responds at `http://localhost:5000`
- [x] You know how to stop both labs

---

## 🔗 References
- [OWASP crAPI](https://github.com/OWASP/crAPI)
- [VAmPI](https://github.com/erev0s/VAmPI)
