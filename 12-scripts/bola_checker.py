#!/usr/bin/env python3
"""
bola_checker.py — simple BOLA (Broken Object Level Authorization) checker.

⚠️ FOR AUTHORIZED LABS ONLY (crAPI, VAmPI, PortSwigger).
   Do not run against systems you do not own or have written permission to test.

Idea:
  1. Log in as User A and User B (you get two tokens).
  2. Request objects with IDs in a range using User A's token.
  3. Request the same IDs using User B's token.
  4. If User B can read objects that belong to User A, BOLA is likely.

Usage example:
  python3 bola_checker.py --base http://localhost:8888 \
      --path "/api/v1/orders/{id}" --ids 1-20 --token-a "TOKEN_A"
"""

import argparse
import sys
import time

import requests


def parse_ids(value: str) -> list[int]:
    """Accept '1-10' or '3,5,8'."""
    if "-" in value:
        start, end = value.split("-", 1)
        return list(range(int(start), int(end) + 1))
    return [int(x) for x in value.split(",") if x.strip()]


def check(base: str, path: str, ids: list[int], token: str, delay: float):
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    results = {}
    for obj_id in ids:
        url = base.rstrip("/") + path.replace("{id}", str(obj_id))
        try:
            resp = session.get(url, timeout=10)
            results[obj_id] = (resp.status_code, len(resp.content))
        except requests.RequestException as exc:
            results[obj_id] = ("ERR", str(exc))
        time.sleep(delay)
    return results


def main():
    parser = argparse.ArgumentParser(description="Simple BOLA checker (lab use only)")
    parser.add_argument("--base", required=True, help="Base URL, e.g. http://localhost:8888")
    parser.add_argument("--path", required=True, help="Path with {id}, e.g. /api/orders/{id}")
    parser.add_argument("--ids", required=True, help="IDs as range '1-20' or list '3,5,8'")
    parser.add_argument("--token-a", required=True, help="Token of the user who owns the objects")
    parser.add_argument("--token-b", help="Token of the other user (the attacker)")
    parser.add_argument("--delay", type=float, default=0.2, help="Seconds between requests")
    args = parser.parse_args()

    if "{id}" not in args.path:
        sys.exit("Error: --path must contain {id}")

    ids = parse_ids(args.ids)
    print(f"[*] Testing {len(ids)} IDs on {args.base}{args.path}")

    owner = check(args.base, args.path, ids, args.token_a, args.delay)
    print("\n[+] Owner (User A) responses:")
    for obj_id, (code, size) in owner.items():
        print(f"    id={obj_id:<5} status={code}  size={size}")

    if args.token_b:
        other = check(args.base, args.path, ids, args.token_b, args.delay)
        print("\n[+] Other user (User B) responses:")
        suspicious = []
        for obj_id, (code, size) in other.items():
            print(f"    id={obj_id:<5} status={code}  size={size}")
            if code == 200 and owner.get(obj_id, (None,))[0] == 200:
                suspicious.append(obj_id)
        print("\n[!] Possible BOLA — User B can read these IDs:" if suspicious else "\n[-] No obvious BOLA found in this range.")
        if suspicious:
            print("    ", suspicious)


if __name__ == "__main__":
    main()
