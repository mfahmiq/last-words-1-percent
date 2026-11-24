# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/mfahmiq/last-words-1-percent/rank.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/mfahmiq/last-words-1-percent/reward.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

An entry for the make.fun bounty **"Famous Last Words at 1 Percent"** — the funniest possible last words a phone would say when its battery hits 1 percent, a single line of at most 199 characters.

## The last words

> I clung to 1% for six minutes. Longer than your last relationship.

## Why it's funny

The line works because it turns a real phone behaviour into a burn. Every phone owner knows the moment: the battery clings to 1% far longer than it has any right to, and you stare at it willing it to survive one more text. The phone, in its own voice, reports that heroic last stand — six whole minutes — and then the second sentence reframes it as an insult: that stubborn little survival outlasted your last relationship. The punch lands at the very end, on the first read, with no explanation needed.

It stays on subject (a dying phone talking about its own battery), sounds like the phone itself rather than a narrator, and avoids the genre's stock moves: no will reading, no goodbye to the charger, no pun on "1 percent". The 1% is the premise, not the joke — the joke is the comparison.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–199 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 66-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 66-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
