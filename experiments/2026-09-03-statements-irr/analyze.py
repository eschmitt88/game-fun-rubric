#!/usr/bin/env python3
"""statements-irr: agreement + separation for the v0.6 instrument, vs the
v0.4 pilot baseline. Run from the experiment dir."""
import csv, json, glob, re, statistics as st
from collections import defaultdict

W = {"1":20,"2":15,"3":15,"4":15,"5":10,"6":10,"7":10,"8":5}
def load(path):
    out={}
    for r in csv.DictReader(open(path)):
        sid=r["id"].strip()
        for g in ("celeste","mightyno9"):
            v=r[g].strip().rstrip("?").lower()
            if v and v not in ("na","n/a"): out[(sid,g)]=float(v)
    return out
raters={re.search(r"rater(\d)",f).group(1):load(f) for f in sorted(glob.glob("results/rater*.csv"))}
sids=sorted({k[0] for r in raters.values() for k in r})
games=("celeste","mightyno9")

deltas=[]; hi=[]
for sid in sids:
    for g in games:
        vals=[r[(sid,g)] for r in raters.values() if (sid,g) in r]
        if len(vals)>=2:
            rng=max(vals)-min(vals); deltas.append(rng)
            if rng>=2: hi.append(f"{sid}/{g}(Δ{rng:.0f})")
m={"n_raters":len(raters),"n_statement_cells":len(deltas),
   "irr":{"mean_range":round(st.mean(deltas),3),
          "pct_range_ge2":round(100*sum(d>=2 for d in deltas)/len(deltas),1),
          "high_disagreement":hi},
   "games":{}}
for g in games:
    rowmeans=defaultdict(list)
    for sid in sids:
        vals=[r[(sid,g)] for r in raters.values() if (sid,g) in r]
        if vals: rowmeans[re.sub(r"[a-z]$","",sid)].append(st.mean(vals))
    dim=defaultdict(list); gates={}
    for rowid,means in rowmeans.items():
        rm=st.mean(means)
        if rowid.startswith("G"): gates[rowid]=round(rm,2)
        else: dim[rowid.split(".")[0]].append(rm)
    tot=sum(st.mean(v)*W[d] for d,v in dim.items()); ws=sum(W[d] for d in dim)
    m["games"][g]={"gates":gates,
                   "dimensions":{d:round(st.mean(v),2) for d,v in sorted(dim.items())},
                   "weighted_total":round(tot/ws,3)}
m["separation"]=round(m["games"]["celeste"]["weighted_total"]-m["games"]["mightyno9"]["weighted_total"],3)
try:
    base=json.load(open("../2026-08-25-rubric-pilot-irr/metrics.json"))
    m["baseline_v04"]={"mean_range":base["irr"]["mean_range"],
                       "pct_range_ge2":base["irr"]["pct_rows_range_ge2"],
                       "separation":base["separation"]}
except FileNotFoundError: pass
json.dump(m,open("metrics.json","w"),indent=2)
print(f"v0.6: mean range {m['irr']['mean_range']}  %>=2 {m['irr']['pct_range_ge2']}  separation {m['separation']}")
if "baseline_v04" in m:
    b=m["baseline_v04"]; print(f"v0.4: mean range {b['mean_range']}  %>=2 {b['pct_range_ge2']}  separation {b['separation']}")
for g in games: print(g, m["games"][g]["weighted_total"], m["games"][g]["gates"], m["games"][g]["dimensions"])
print("high disagreement:", ", ".join(hi) or "none")
