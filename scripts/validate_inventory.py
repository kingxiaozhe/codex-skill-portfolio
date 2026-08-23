#!/usr/bin/env python3
"""Validate the public inventory without depending on a YAML/CSV package."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory.tsv"
VALID_DECISIONS = {
    "existing-public-project",
    "private-content-bound",
    "private-machine-specific",
    "private-pending-provenance",
    "private-permission-required",
    "private-safety-bound",
    "published",
    "runtime-component",
    "system-bundle",
    "upstream-no-republish",
    "upstream-reference",
}


def main() -> None:
    rows = INVENTORY.read_text(encoding="utf-8").splitlines()
    assert rows[0] == "name\tdecision\tcanonical_home\twhy", "invalid header"
    entries = [line.split("\t") for line in rows[1:] if line]
    assert len(entries) == 74, f"expected 74 direct skill entries, got {len(entries)}"
    assert all(len(entry) == 4 for entry in entries), "every row must have four columns"
    names = [entry[0] for entry in entries]
    assert len(names) == len(set(names)), "duplicate skill name"
    decisions = {entry[1] for entry in entries}
    assert decisions <= VALID_DECISIONS, f"unknown decision: {decisions - VALID_DECISIONS}"
    assert "published" in decisions, "portfolio must retain published work"
    assert "upstream-reference" in decisions, "portfolio must retain attribution"
    assert "private-pending-provenance" in decisions, "portfolio must retain ownership holds"
    print(f"OK: {len(entries)} direct installed skills, {len(decisions)} disposition types")


if __name__ == "__main__":
    main()
