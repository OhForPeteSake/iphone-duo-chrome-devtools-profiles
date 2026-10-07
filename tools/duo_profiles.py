#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, json, os, shutil, subprocess, sys
from pathlib import Path

KEY = "custom-emulated-device-list"
ROOT = Path(__file__).resolve().parents[1]
BUNDLED = ROOT / "profiles" / "iphone-duo-devtools.json"
TITLES = {"iPhone Duo Outer", "iPhone Duo Inner"}

def chrome_root() -> Path:
    if sys.platform.startswith("win"):
        return Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Google" / "Chrome"
    return Path.home() / ".config" / "google-chrome"

def chrome_running() -> bool:
    try:
        if sys.platform.startswith("win"):
            p = subprocess.run(["tasklist", "/FI", "IMAGENAME eq chrome.exe"],
                               capture_output=True, text=True, check=False)
            return "chrome.exe" in p.stdout.lower()
        if sys.platform == "darwin":
            p = subprocess.run(["pgrep", "-x", "Google Chrome"],
                               capture_output=True, text=True, check=False)
            return p.returncode == 0
        p = subprocess.run(["pgrep", "-x", "chrome"],
                           capture_output=True, text=True, check=False)
        return p.returncode == 0
    except Exception:
        return False

def discover():
    root = chrome_root()
    candidates = []
    for d in [root/"Default", *sorted(root.glob("Profile *"))]:
        f = d/"Preferences"
        if f.exists():
            candidates.append(f)
    return candidates

def choose(profile=None, prefs=None):
    if prefs:
        f = Path(prefs).expanduser().resolve()
        if not f.exists():
            raise FileNotFoundError(f)
        return f
    if profile:
        f = chrome_root()/profile/"Preferences"
        if not f.exists():
            raise FileNotFoundError(f)
        return f
    options = discover()
    if not options:
        raise FileNotFoundError("No Chrome Preferences files were found.")
    if len(options) == 1:
        return options[0]
    print("Chrome profiles found:")
    for i, f in enumerate(options, 1):
        print(f"  {i}. {f.parent.name}")
    while True:
        raw = input("Choose profile number: ").strip()
        try:
            n = int(raw)
            if 1 <= n <= len(options):
                return options[n-1]
        except ValueError:
            pass
        print("Enter a valid number.")

def decode_list(prefs):
    dp = prefs.setdefault("devtools", {}).setdefault("preferences", {})
    raw = dp.get(KEY)
    if raw is None:
        return [], "string"
    if isinstance(raw, str):
        parsed = json.loads(raw)
        if not isinstance(parsed, list):
            raise RuntimeError(f"{KEY} is not a JSON array.")
        return parsed, "string"
    if isinstance(raw, list):
        return raw, "array"
    raise RuntimeError(f"Unexpected {KEY} storage type: {type(raw).__name__}")

def encode_list(prefs, devices, storage):
    dp = prefs.setdefault("devtools", {}).setdefault("preferences", {})
    dp[KEY] = devices if storage == "array" else json.dumps(devices, separators=(",", ":"))

def validate_device(d):
    errors = []
    required = {
        "title": str,
        "type": str,
        "user-agent": str,
        "capabilities": list,
        "screen": dict,
        "show-by-default": bool,
    }
    for k,t in required.items():
        if k not in d:
            errors.append(f"missing {k}")
        elif not isinstance(d[k], t):
            errors.append(f"{k} has wrong type")
    if d.get("type") not in {"phone","tablet","notebook","desktop","foldable","smart-display","unknown"}:
        errors.append("invalid type")
    s=d.get("screen",{})
    if not isinstance(s.get("device-pixel-ratio"), (int,float)):
        errors.append("invalid DPR")
    for o in ("vertical","horizontal"):
        x=s.get(o)
        if not isinstance(x,dict) or not isinstance(x.get("width"),int) or not isinstance(x.get("height"),int):
            errors.append(f"invalid {o} dimensions")
    if d.get("show","Default") not in {"Always","Default","Never"}:
        errors.append("invalid show value")
    return errors

def backup(path):
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    b = path.with_name(path.name + ".duo-backup-" + stamp)
    shutil.copy2(path,b)
    return b

def atomic_save(path, data):
    tmp=path.with_name(path.name+".duo-tmp")
    tmp.write_text(json.dumps(data, separators=(",",":"), ensure_ascii=False), encoding="utf-8")
    os.replace(tmp,path)

def install(args):
    if chrome_running() and not args.force:
        print("ERROR: Chrome is still running.")
        print("Close Chrome completely (including background processes) and run the installer again.")
        raise SystemExit(3)

    path=choose(args.profile,args.prefs)
    prefs=json.loads(path.read_text(encoding="utf-8"))
    current,storage=decode_list(prefs)
    incoming=json.loads(BUNDLED.read_text(encoding="utf-8"))

    for d in incoming:
        errs=validate_device(d)
        if errs:
            raise RuntimeError(f"{d.get('title')}: " + ", ".join(errs))

    pos={d.get("title"):i for i,d in enumerate(current) if isinstance(d,dict)}
    added=updated=0
    for d in incoming:
        if d["title"] in pos:
            current[pos[d["title"]]]=d
            updated += 1
        else:
            current.append(d)
            added += 1

    encode_list(prefs,current,storage)
    b=backup(path)
    atomic_save(path,prefs)

    # Re-read exact bytes we just wrote and verify the entries.
    check=json.loads(path.read_text(encoding="utf-8"))
    installed,_=decode_list(check)
    found={d.get("title") for d in installed if isinstance(d,dict)}
    missing=TITLES-found
    if missing:
        raise RuntimeError("Write verification failed: " + ", ".join(sorted(missing)))

    print()
    print("SUCCESS: Duo profiles written and verified on disk.")
    print(f"Chrome profile: {path.parent.name}")
    print(f"Preferences: {path}")
    print(f"Added: {added} | Updated: {updated}")
    print(f"Backup: {b}")
    print()
    print("Now reopen Chrome -> F12 -> Settings -> Devices.")
    print("Expected: iPhone Duo Outer + iPhone Duo Inner")

def listing(args):
    path=choose(args.profile,args.prefs)
    prefs=json.loads(path.read_text(encoding="utf-8"))
    devices,_=decode_list(prefs)
    print(f"Profile: {path.parent.name}")
    print(f"Preferences: {path}")
    found=0
    for d in devices:
        if isinstance(d,dict):
            mark = "  <DUO>" if d.get("title") in TITLES else ""
            s=d.get("screen",{})
            v=s.get("vertical",{})
            h=s.get("horizontal",{})
            print(f"- {d.get('title')} | DPR {s.get('device-pixel-ratio')} | "
                  f"V {v.get('width')}x{v.get('height')} | H {h.get('width')}x{h.get('height')}{mark}")
            if d.get("title") in TITLES:
                found += 1
    print(f"Duo profiles found on disk: {found}/2")

def doctor(args):
    path=choose(args.profile,args.prefs)
    print(f"Chrome running: {'YES' if chrome_running() else 'NO'}")
    print(f"Profile: {path.parent.name}")
    print(f"Preferences: {path}")
    prefs=json.loads(path.read_text(encoding="utf-8"))
    devices,storage=decode_list(prefs)
    print(f"Storage type: {storage}")
    duo=[d for d in devices if isinstance(d,dict) and d.get("title") in TITLES]
    print(f"Duo profiles on disk: {len(duo)}/2")
    for d in duo:
        errs=validate_device(d)
        print(f"  {d['title']}: {'OK' if not errs else 'ERROR - '+', '.join(errs)}")
    if len(duo) < 2:
        print("Run install with Chrome completely closed.")
    else:
        print("Disk configuration looks valid. If Chrome removes the entries after launch,")
        print("close Chrome again and rerun doctor to confirm Chrome rewrote the setting.")

def remove(args):
    if chrome_running() and not args.force:
        print("ERROR: Chrome is still running. Close it completely first.")
        raise SystemExit(3)
    path=choose(args.profile,args.prefs)
    prefs=json.loads(path.read_text(encoding="utf-8"))
    devices,storage=decode_list(prefs)
    new=[d for d in devices if not(isinstance(d,dict) and d.get("title") in TITLES)]
    b=backup(path)
    encode_list(prefs,new,storage)
    atomic_save(path,prefs)
    print(f"Removed {len(devices)-len(new)} Duo profile(s). Backup: {b}")

def main():
    p=argparse.ArgumentParser(description="Manage iPhone Duo Chrome DevTools custom-device profiles.")
    p.add_argument("--profile")
    p.add_argument("--prefs")
    sub=p.add_subparsers(dest="cmd",required=True)

    a=sub.add_parser("install")
    a.add_argument("--force",action="store_true",help="Write even if Chrome appears to be running.")
    a.set_defaults(fn=install)

    a=sub.add_parser("list"); a.set_defaults(fn=listing)
    a=sub.add_parser("doctor"); a.set_defaults(fn=doctor)

    a=sub.add_parser("remove")
    a.add_argument("--force",action="store_true")
    a.set_defaults(fn=remove)

    args=p.parse_args()
    args.fn(args)

if __name__=="__main__":
    main()
