"""Your Week in One Line — make.fun bounty entry.

Writes a single line (at most 100 characters) that sums up a week:
the win, the fail, the chaos, all of it.

Round 2: the week as escalating breakage — plans Monday, laptop
Wednesday — rescued Friday by tacos and a nap.
"""

ENTRY = "Monday broke my plans, Wednesday broke my laptop, Friday fixed everything with tacos and a nap."


def main() -> None:
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry must be 1-100 characters, got {len(line)}")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
