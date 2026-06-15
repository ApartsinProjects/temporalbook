#!/usr/bin/env python
"""Generate chapter illustrations from per-chapter manifests via one batch job.

Each chapter module dir has images/_illustrations.json: a JSON array of items
  {"file": "name.png", "section": "section-N.M.html", "after_heading": "...",
   "type": "...", "prompt": "<single-line gemini prompt>",
   "alt": "...", "caption": "..."}

This driver collects every (chapter, file, prompt) across the requested chapters
IN ORDER, writes one prompts file, runs gemini-imagegen batch_generate.py to a
temp dir (outputs img_001.png ... in order), then moves each output to its
target chapter/images/<file>. Idempotent: skips items whose target already
exists unless --force.

Usage:
  python scripts/gen_illustrations.py part-1-foundations/module-01-* part-1-.../module-02-*
  python scripts/gen_illustrations.py --part 1
  python scripts/gen_illustrations.py --all [--force] [--sync]
"""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
BATCH = pathlib.Path(
    "E:/Projects/claude-skills/gemini-imagegen/scripts/batch_generate.py")
MODEL = "gemini-2.5-flash-image"


def chapter_dirs(args):
    if args.all:
        return sorted(ROOT.glob("part-*/module-*"))
    if args.part:
        return sorted(ROOT.glob(f"part-{args.part}-*/module-*"))
    out = []
    for a in args.dirs:
        out.extend(sorted(ROOT.glob(a)) if "*" in a else [pathlib.Path(a)])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="*")
    ap.add_argument("--part")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--size", default="1K")
    args = ap.parse_args()

    jobs = []  # (target_path, prompt)
    for d in chapter_dirs(args):
        man = d / "images" / "_illustrations.json"
        if not man.exists():
            print(f"  no manifest: {d.name}")
            continue
        try:
            items = json.loads(man.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  BAD manifest {man}: {e}")
            continue
        for it in items:
            tgt = d / "images" / it["file"]
            if tgt.exists() and not args.force:
                continue
            p = it["prompt"].replace("\n", " ").strip()
            jobs.append((tgt, p))

    if not jobs:
        print("Nothing to generate (all targets exist or no manifests).")
        return
    print(f"Generating {len(jobs)} illustrations...")

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="taibook_imgs_"))
    prompts_file = tmp / "prompts.txt"
    prompts_file.write_text("\n".join(p for _, p in jobs), encoding="utf-8")

    cmd = [sys.executable, str(BATCH), "--prompts", str(prompts_file),
           "--output-dir", str(tmp), "--model", MODEL,
           "--aspect-ratio", args.aspect, "--image-size", args.size]
    if args.sync:
        cmd += ["--sync", "--workers", "4"]
    print("  ", " ".join(cmd))
    r = subprocess.run(cmd)
    if r.returncode != 0:
        print("Batch generation failed.")
        sys.exit(1)

    moved = 0
    for i, (tgt, _) in enumerate(jobs):
        out = tmp / f"img_{i+1:03d}.png"
        if out.exists():
            tgt.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(out), str(tgt))
            moved += 1
        else:
            print(f"  MISSING output for {tgt.relative_to(ROOT)}")
    print(f"Routed {moved}/{len(jobs)} images to chapter image dirs.")


if __name__ == "__main__":
    main()
