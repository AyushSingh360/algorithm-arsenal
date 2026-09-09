#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_site_data.py
==================
Scans the leetcode/ directory and enriches each problem with metadata
from LeetCode's public GraphQL API (difficulty, topic tags).

Results are cached in docs/data/problems.json so that subsequent runs
only fetch newly added problems — keeping CI fast.

Usage:
    python .scripts/build_site_data.py
"""

import os
import re
import json
import time
import urllib.request
import urllib.error
import sys

# Ensure UTF-8 output on all platforms (Windows fix)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
REPO_ROOT    = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEETCODE_DIR = os.path.join(REPO_ROOT, "leetcode")
OUTPUT_DIR   = os.path.join(REPO_ROOT, "docs", "data")
OUTPUT_FILE  = os.path.join(OUTPUT_DIR, "problems.json")

API_URL      = "https://leetcode.com/graphql"
API_DELAY    = 0.5   # seconds between successful API calls
RETRY_DELAY  = 2.0   # base seconds for exponential back-off
MAX_RETRIES  = 3
SAVE_EVERY   = 20    # save intermediate results every N new fetches

LANGUAGE_MAP = {
    ".py":    "Python",
    ".cpp":   "C++",
    ".c":     "C",
    ".java":  "Java",
    ".js":    "JavaScript",
    ".ts":    "TypeScript",
    ".go":    "Go",
    ".rs":    "Rust",
    ".cs":    "C#",
    ".rb":    "Ruby",
    ".swift": "Swift",
    ".sql":   "SQL",
    ".sh":    "Bash",
    ".kt":    "Kotlin",
    ".scala": "Scala",
    ".php":   "PHP",
}

GRAPHQL_QUERY = """
query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        difficulty
        topicTags { name }
    }
}
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_language(filename: str) -> str | None:
    _, ext = os.path.splitext(filename)
    return LANGUAGE_MAP.get(ext.lower())


def parse_folder_name(folder: str) -> tuple[int | None, str | None]:
    """'0001-two-sum'  →  (1, 'two-sum')"""
    match = re.match(r"^(\d+)-(.+)$", folder)
    if not match:
        return None, None
    return int(match.group(1)), match.group(2)


def scan_folder(folder_path: str) -> tuple[list[str], list[str], bool]:
    """Return (solution_files, languages, has_readme)."""
    files, languages = [], []
    has_readme = False
    for fname in sorted(os.listdir(folder_path)):
        if fname.lower() == "readme.md":
            has_readme = True
            continue
        lang = get_language(fname)
        if lang:
            files.append(fname)
            if lang not in languages:
                languages.append(lang)
    return files, languages, has_readme


def fetch_leetcode_metadata(slug: str) -> dict | None:
    """Call LeetCode's public GraphQL API. Returns the question dict or None."""
    payload = json.dumps({
        "query": GRAPHQL_QUERY,
        "variables": {"titleSlug": slug},
    }).encode("utf-8")

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(
                API_URL,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (compatible; AlgorithmArsenalBot/1.0)",
                    "Referer": f"https://leetcode.com/problems/{slug}/",
                    "x-csrftoken": "dummy",
                },
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("data", {}).get("question")
        except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
            wait = RETRY_DELAY * (2 ** attempt)
            print(f"    ⚠ attempt {attempt + 1}/{MAX_RETRIES} failed ({exc}) — retrying in {wait:.0f}s")
            if attempt < MAX_RETRIES - 1:
                time.sleep(wait)
    return None


def save(problems: list[dict]) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    problems_sorted = sorted(problems, key=lambda p: p["id"])
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(problems_sorted, f, separators=(",", ":"), ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_site_data() -> None:
    # 1. Load existing cache ------------------------------------------------
    cache: dict[str, dict] = {}
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    cache[p["slug"]] = p
            print(f"[CACHE] Loaded {len(cache)} cached problems from {OUTPUT_FILE}")
        except (json.JSONDecodeError, KeyError):
            print("[WARN] Cache file corrupted -- rebuilding from scratch.")

    # 2. Scan leetcode/ directory -------------------------------------------
    if not os.path.isdir(LEETCODE_DIR):
        print(f"[ERROR] Directory not found: {LEETCODE_DIR}")
        sys.exit(1)

    all_folders = sorted(
        f for f in os.listdir(LEETCODE_DIR)
        if os.path.isdir(os.path.join(LEETCODE_DIR, f))
    )
    print(f"[INFO] Found {len(all_folders)} problem folders in leetcode/\n")

    problems: list[dict] = []
    new_fetches = 0
    api_failures = 0

    for folder in all_folders:
        folder_path = os.path.join(LEETCODE_DIR, folder)
        num, slug = parse_folder_name(folder)
        if num is None:
            print(f"  ⚠ Skipping unrecognised folder: {folder}")
            continue

        files, languages, has_readme = scan_folder(folder_path)

        # Use cache if we already have enriched metadata
        if slug in cache and cache[slug].get('difficulty', 'Unknown') != 'Unknown':
            p = dict(cache[slug])
            # Always refresh file list (might have new languages)
            p["files"] = files
            p["languages"] = languages
            p["hasReadme"] = has_readme
            problems.append(p)
            continue

        # Fetch from LeetCode API
        print(f"  -> [{num:>4}] {slug} ... ", end="", flush=True)
        metadata = fetch_leetcode_metadata(slug)
        new_fetches += 1

        if metadata:
            p = {
                "id":         num,
                "title":      metadata.get("title", slug.replace("-", " ").title()),
                "slug":       slug,
                "folder":     folder,
                "difficulty": metadata.get("difficulty", "Unknown"),
                "topics":     [t["name"] for t in metadata.get("topicTags", [])],
                "languages":  languages,
                "files":      files,
                "hasReadme":  has_readme,
            }
            diff_label = {"Easy": "[E]", "Medium": "[M]", "Hard": "[H]"}.get(p['difficulty'], "[?]")
            print(f"{diff_label} {p['difficulty']}  [{', '.join(p['topics'][:3]) or 'No tags'}]")
        else:
            api_failures += 1
            p = {
                "id":         num,
                "title":      slug.replace("-", " ").title(),
                "slug":       slug,
                "folder":     folder,
                "difficulty": "Unknown",
                "topics":     [],
                "languages":  languages,
                "files":      files,
                "hasReadme":  has_readme,
            }
            print("[FAIL] API failed -- using defaults")

        problems.append(p)

        # Intermediate save every SAVE_EVERY new fetches
        if new_fetches % SAVE_EVERY == 0:
            save(problems)
            print(f"  [SAVE] Saved intermediate results ({len(problems)} problems)")

        time.sleep(API_DELAY)

    # 3. Final save ---------------------------------------------------------
    save(problems)

    print(f"\n[DONE] Finished!")
    print(f"   Total problems : {len(problems)}")
    print(f"   New API fetches: {new_fetches}")
    print(f"   API failures   : {api_failures}")
    print(f"   Output         : {OUTPUT_FILE}")


if __name__ == "__main__":
    build_site_data()
