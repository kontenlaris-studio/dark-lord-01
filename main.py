#!/usr/bin/env python3
"""The Tired Dark Lord — a 100-word villain monologue, printed to /output/entry.txt."""
import os

MONOLOGUE = (
    "Four centuries I have ruled this mountain, and what finally broke me? "
    "Not the heroes. The paperwork. Tuesdays, a new party kicks down my door, "
    "swings my grandfather's sword, and expects a speech. I rehearsed once. "
    "Now I sigh and ask about torches; the dungeon budget was cut again. "
    "My minions unionized. The dragon wants dental. The moat's algae has "
    "opinions, and the literal skeletons filed a complaint about the stairs. "
    "I keep the throne because nobody else will mop the chamber. "
    "I would trade the whole cursed kingdom for one quiet weekend and "
    "a chair that does not whisper."
)
# Bounty contract: a monologue of exactly 100 words.
assert len(MONOLOGUE.split()) == 100, len(MONOLOGUE.split())


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")
    print(MONOLOGUE)


if __name__ == "__main__":
    main()
