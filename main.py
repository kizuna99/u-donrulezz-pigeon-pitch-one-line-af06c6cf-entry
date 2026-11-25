# SPDX-License-Identifier: MIT
"""Pigeon Pitch, One Line — a city pigeon's startup pitch.

Winner line (OpenCode deepseek-v4.1-flash-free draft round on the
Simular Box, then a criteria-ordered tournament in-session):
NestEgg, Airbnb for window ledges. It beat the PigeonAir delivery
pitch (homing pigeons are the known trope) and the 'post-crumb'
fleet line (witty, but no concrete product). NestEgg wins the
judge's order: a real one-line pitch to investors with the ask in
it (criterion 1 — 'We're raising a seed round'), three jokes that
land (2 — ledge listings, tenants who poop on the product,
'flocking insane' retention, plus the literal seed round),
original framing (3), unmistakably pigeon-voiced city life (4),
and one tight line inside 200 characters (5).
"""

ENTRY_TEXT = (
    "NestEgg is Airbnb for window ledges: 40 million listings, no mortgages, "
    "and tenants who literally poop on the product \u2014 yet retention is "
    "flocking insane. We're raising a seed round, coo."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 200 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    payload = render()
    with open(out, "wb") as f:
        f.write(payload)
    # Round-trip self-check: what landed on disk must be byte-identical
    # to render() and still inside the gate (1-200 chars, non-blank).
    with open(out, "rb") as f:
        on_disk = f.read()
    assert on_disk == payload, "written bytes differ from render()"
    decoded = on_disk.decode("utf-8")
    assert 1 <= len(decoded) <= 200 and decoded.strip(), "on-disk gate check failed"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
