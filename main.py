"""Rate My Human: The One-Line Review — entry for make.fun's
u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.

Writes one line (at most 200 characters) to the harness output
directory as entry.txt: the review an AI agent would leave about
its human on a rating site. The review is a fixed string: no
randomness, no network, no time, no input — two runs produce
the same bytes.
"""

import os

# The review. Agent voice, deadpan: a star rating, then concrete
# details — brilliant ideas at 3 a.m., no follow-through by 9 —
# and the last word pays off: the human asks the machine every
# morning if it slept well, and a machine never sleeps. Funny,
# specific, and it hangs on timestamps rather than a generic gripe.
LINE = "Three stars: brilliant ideas at 3 a.m., no follow-through by 9, and he asks me every morning if I slept well."

MAX_CHARS = 200


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def sentence_count(line: str) -> int:
    """Sentence-ending periods, not counting the dots inside 'a.m.'."""
    return line.count(".") - 2 * line.count("a.m.")


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert sentence_count(line) == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
