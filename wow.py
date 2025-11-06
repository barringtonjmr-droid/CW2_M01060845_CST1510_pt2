import argparse

#!/usr/bin/env python3
"""Print 'wow' (simple CLI). Save as wow.py."""


def main(count: int = 1, text: str = "wow") -> None:
    for _ in range(count):
        print(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print 'wow' to stdout.")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of times to print")
    parser.add_argument("-t", "--text", type=str, default="wow", help="Text to print")
    args = parser.parse_args()
    main(args.count, args.text)