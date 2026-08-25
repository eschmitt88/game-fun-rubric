#!/usr/bin/env python3
"""Score a filled rubric worksheet (docs/rubric.md v0.3 semantics).

usage: python tools/score.py tools/rubric_worksheet.csv [--profile "Mastery"]

Reads rater1..rater3 (0-4, blank = not scored), averages per criterion,
applies gates, computes functional / psychosocial / story subtotals and the
weighted total, flags rater deltas >= 2, and prints the bottom-five rows.
"""
import csv, sys, statistics as st
from collections import defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "tools/rubric_worksheet.csv"
profile = sys.argv[sys.argv.index("--profile")+1] if "--profile" in sys.argv else "(unset — run S1)"
rows = list(csv.DictReader(open(path)))

def scores(r):
    return [float(r[k]) for k in ("rater1","rater2","rater3") if r[k].strip()]

gates, crit = {}, []
for r in rows:
    s = scores(r)
    if not s: continue
    mean = st.mean(s); delta = (max(s)-min(s)) if len(s) > 1 else 0
    if r["tier"] == "gate": gates[r["id"]] = mean
    else: crit.append((r, mean, delta))

print(f"Target motivation profile (S1): {profile}\n")
capped = any(v == 0 for v in gates.values())
for g, v in gates.items(): print(f"{g}: {v:.1f}" + ("  <-- GATE FAILED" if v == 0 else ""))
if capped: print("\nVERDICT: not fun (a hard gate scored 0). Fix the gate before reading anything below.\n")

dim = defaultdict(list); tier = defaultdict(list); weight = {}
for r, m, d in crit:
    dim[r["dimension"]].append(m); tier[r["tier"]].append(m); weight[r["dimension"]] = float(r["weight"])

print("\nDimension means (0-4):")
total = 0; wsum = 0
for dname, vals in dim.items():
    mean = st.mean(vals); w = weight[dname]; total += mean*w; wsum += w
    print(f"  {dname:32s} {mean:.2f}   (w={w:.0f}%)")
if wsum == 0:
    print("\nNo criteria scored yet — fill rater1..rater3 (0-4) in the worksheet.")
    sys.exit(0)
print(f"\nWeighted total: {total/wsum:.2f} / 4   (weights provisional — ADR 0001/0002)")

print("\nSubtotals:")
for t in ("functional","psychosocial","story"):
    if tier[t]: print(f"  {t:12s} {st.mean(tier[t]):.2f}")
if tier["functional"] and st.mean(tier["functional"]) < 2.0:
    print("  ! functional floor < 2.0: psychosocial (2,5,6) scores are unreliable (ADR 0003). Story track (7) reported separately (ADR 0004).")

flag = [(r["id"], d) for r, m, d in crit if d >= 2]
if flag: print("\nRater disagreement >= 2 (discuss before trusting):", ", ".join(f"{i} (Δ{d:.0f})" for i, d in flag))

print("\nBottom five (next sprint):")
for r, m, d in sorted(crit, key=lambda x: x[1])[:5]:
    print(f"  {r['id']:4s} {m:.1f}  {r['criterion']}  [{r['tier_evidence']}]")
