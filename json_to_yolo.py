import os, json

ANN_DIR = "ann"
OUT_DIR = "labels_yolo"
os.makedirs(OUT_DIR, exist_ok=True)

CLASS_MAP = {"helmet": 0, "head": 1}

for ann_file in os.listdir(ANN_DIR):
    if not ann_file.endswith(".json"):
        continue

    with open(os.path.join(ANN_DIR, ann_file)) as f:
        data = json.load(f)

    w, h = data["size"]["width"], data["size"]["height"]
    lines = []

    for obj in data["objects"]:
        cls = obj["classTitle"]
        if cls not in CLASS_MAP:
            continue
        cid = CLASS_MAP[cls]
        (x1, y1), (x2, y2) = obj["points"]["exterior"]
        xc = ((x1 + x2) / 2) / w
        yc = ((y1 + y2) / 2) / h
        bw = (x2 - x1) / w
        bh = (y2 - y1) / h
        lines.append(f"{cid} {xc} {yc} {bw} {bh}")

    out = os.path.join(OUT_DIR, ann_file.replace(".json", ".txt"))
    with open(out, "w") as f:
        f.write("\n".join(lines))

print("Successful")
