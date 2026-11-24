"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a sunset sinking
into the sea. Of all the single emojis, this is the postcard
moment itself — golden hour over open water, the exact feeling
that makes a stranger want to book the flight. No words, no
explanation needed: one glance and the trip is already booked
in the reader's head.
"""

import os

EMOJI = "\U0001F305"  # sunrise/sunset over the sea


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
