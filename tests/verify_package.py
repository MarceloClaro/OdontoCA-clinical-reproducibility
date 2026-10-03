import csv,json,hashlib
from pathlib import Path
from PIL import Image
r=Path(__file__).resolve().parents[1]
d=json.loads((r/"results/clinical_internal_validation.json").read_text())
assert (d["analysis_rows"],d["analysis_events"],d["analysis_children"]) == (996,83,81)
rows=list(csv.DictReader((r/"data/Figure_5_data.csv").open()))
assert len(rows)==20 and sum(int(x["transitions"]) for x in rows)==996 and sum(int(x["events"]) for x in rows)==83
for t in ["T82","T81","T71","T72"]:assert int(next(x for x in rows if x["tooth_position"]==t)["events"])==0
with Image.open(r/"figures/Figure_5.png") as im:assert im.size==(3480,2610)
assert not list(r.rglob("*.xlsx"))
print("PASS: aggregate cohort, 20 tooth positions, lower incisors, native Figure 5 dimensions, no raw worksheet")
