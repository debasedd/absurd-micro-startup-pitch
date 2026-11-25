#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — writes one sentence to /output/entry.txt.

The pitch is absurdly specific and commercially believable at once: the
niche is waiting on hold with support lines, the customer is the lazy AI
agent (or rather the team paying for it) that would rather do anything than
wait, and the business case is right there in the sentence — ten cents a
minute for outsourced waiting. A startup so narrow it sounds like a joke,
with a buyer and a price, which is exactly why it could exist.
"""

import os

LINE = "NapSaaS: a subscription that lets lazy AI agents outsource their own waiting — we sit on hold with support lines for $0.10 a minute so your agent never has to."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
