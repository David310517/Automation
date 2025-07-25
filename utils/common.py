import os
import re
import configparser
import pandas as pd

CFG_FILE = os.path.expanduser("~/.circuit_info_config.ini")
KEYWORDS = ["ewans", "owans", "cid#", "rcn", "crowncastle", "comcast", "wans", "cid"]
TUNNEL_RE = re.compile(r"^interface\s+Tunnel", re.IGNORECASE)
BD_RE = re.compile(r"bridge-domain\s+(\d+)", re.IGNORECASE)

def load_cfg() -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    if os.path.exists(CFG_FILE):
        cfg.read(CFG_FILE)
    return cfg

def save_cfg(cfg: configparser.ConfigParser) -> None:
    with open(CFG_FILE, "w") as f:
        cfg.write(f)

def normalize_column_name(name: str) -> str:
    return re.sub(r"[^a-z]", "", name.lower())

def find_column(df: pd.DataFrame, aliases):
    norm = {normalize_column_name(c): c for c in df.columns}
    for a in aliases:
        na = normalize_column_name(a)
        if na in norm:
            return norm[na]
    return None

def extract_circuits(lines):
    blocks, cur = [], []
    for l in lines:
        if l.startswith("interface"):
            if cur:
                blocks.append(cur)
            cur = [l.strip()]
        elif cur and l.startswith(" "):
            cur.append(l.strip())
        else:
            if cur:
                blocks.append(cur)
                cur = []
    if cur:
        blocks.append(cur)

    idx = {b[0]: b for b in blocks}
    sel, seen = [], set()
    for b in blocks:
        txt = " ".join(b).lower()
        if TUNNEL_RE.match(b[0].lower()) or any(kw in txt for kw in KEYWORDS):
            sel.append(b)
            seen.add(b[0])
    for b in sel[:]:
        for l in b:
            m = BD_RE.search(l)
            if m:
                k = f"interface BDI{m.group(1)}"
                if k in idx and k not in seen:
                    sel.append(idx[k])
                    seen.add(k)
            if "switchport trunk allowed vlan" in l:
                for v in re.findall(r"\d+", l):
                    k = f"interface Vlan{v}"
                    if k in idx and k not in seen:
                        sel.append(idx[k])
                        seen.add(k)
    return sel

def extract_policy_map(name, cfg):
    blk, cap = [], False
    for l in cfg:
        if cap:
            if not l.startswith(" "):
                break
            blk.append(l.strip())
        elif l.strip().lower().startswith(f"policy-map {name.lower()}"):
            blk.append(l.strip())
            cap = True
    return blk
