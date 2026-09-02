#!/usr/bin/env python3
"""Analyze rubric-pilot-irr rater CSVs → metrics.json + printed report.

usage: python analyze.py  (run from the experiment dir)
"""
import csv, json, statistics as st, glob, re
from collections import defaultdict

W = {"1": 20, "2": 15, "3": 15, "4": 15, "5": 10, "6": 10, "7": 10, "8": 5}
TIER = {"1":"functional","3":"functional","4":"functional","8":"functional",
        "2":"psychosocial","5":"psychosocial","6":"psychosocial","7":"story-psych"}
TIER["7"]="story"

def load(path):
    out = {}
    for r in csv.DictReader(open(path)):
        rid = r["id"].strip()
        for g in ("celeste","mightyno9"):
            v = r[g].strip().rstrip("?")
            if v != "": out[(rid,g)] = float(v)
    return out

raters = {re.search(r"rater(\d)",f).group(1): load(f)
          for f in sorted(glob.glob("results/rater*.csv"))}
ids = sorted({k[0] for r in raters.values() for k in r}, key=lambda x:(x!="G1",x!="G2",x))
games = ("celeste","mightyno9")

report, metrics = [], {"n_raters": len(raters), "games": {}, "irr": {}}
# per-row agreement
deltas, high_disagree = [], []
for rid in ids:
    for g in games:
        vals = [r[(rid,g)] for r in raters.values() if (rid,g) in r]
        if len(vals) >= 2:
            rng = max(vals)-min(vals); deltas.append(rng)
            if rng >= 2: high_disagree.append(f"{rid}/{g}(Δ{rng:.0f})")
metrics["irr"]["mean_range"] = round(st.mean(deltas),3)
metrics["irr"]["pct_rows_range_ge2"] = round(100*sum(d>=2 for d in deltas)/len(deltas),1)
metrics["irr"]["high_disagreement"] = high_disagree

for g in games:
    gm = {"gates":{}, "dimensions":{}, "weighted_total":None, "subtotals":{}}
    for gate in ("G1","G2"):
        vals=[r[(gate,g)] for r in raters.values() if (gate,g) in r]
        gm["gates"][gate]=round(st.mean(vals),2)
    dim=defaultdict(list); tier=defaultdict(list)
    for rid in ids:
        if rid.startswith("G"): continue
        d=rid.split(".")[0]
        vals=[r[(rid,g)] for r in raters.values() if (rid,g) in r]
        if vals:
            m=st.mean(vals); dim[d].append(m); tier[TIER[d]].append(m)
    tot=sum(st.mean(v)*W[d] for d,v in dim.items()); wsum=sum(W[d] for d in dim)
    gm["dimensions"]={d:round(st.mean(v),2) for d,v in sorted(dim.items())}
    gm["subtotals"]={t:round(st.mean(v),2) for t,v in tier.items()}
    gm["weighted_total"]=round(tot/wsum,3)
    metrics["games"][g]=gm

metrics["separation"] = round(metrics["games"]["celeste"]["weighted_total"]
                            - metrics["games"]["mightyno9"]["weighted_total"],3)
json.dump(metrics, open("metrics.json","w"), indent=2)

print(f"raters={len(raters)}  mean per-row range={metrics['irr']['mean_range']}  "
      f"rows with range>=2: {metrics['irr']['pct_rows_range_ge2']}%")
for g in games:
    gm=metrics["games"][g]
    print(f"\n{g}: weighted {gm['weighted_total']}/4  gates {gm['gates']}  "
          f"subtotals {gm['subtotals']}\n  dims {gm['dimensions']}")
print(f"\nseparation (celeste - mightyno9): {metrics['separation']}")
print(f"\nhigh-disagreement rows ({len(high_disagree)}):", ", ".join(high_disagree) or "none")
