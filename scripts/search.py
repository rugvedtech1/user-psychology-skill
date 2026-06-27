#!/usr/bin/env python3
"""
User Psychology Skill - Search Script
Search psychology rules by industry, principle, or keyword.
Usage: python3 scripts/search.py --industry fintech
       python3 scripts/search.py --principle cta
       python3 scripts/search.py --keyword "pricing"
       python3 scripts/search.py --product "food delivery app"
"""

import os
import re
import argparse
import sys
from pathlib import Path


# ── Constants ────────────────────────────────────────────────────────────────

SKILL_ROOT = Path(__file__).parent.parent
PRINCIPLES_DIR = SKILL_ROOT / "src" / "principles"
INDUSTRIES_DIR = SKILL_ROOT / "src" / "industries"
EXAMPLES_DIR   = SKILL_ROOT / "src" / "examples"
REASONING_FILE = SKILL_ROOT / "src" / "reasoning" / "industry-rules.md"

INDUSTRY_KEYWORDS = {
    "ecommerce": [
        "shop", "store", "product", "cart", "checkout", "buy", "purchase",
        "delivery", "shipping", "catalog", "listing", "d2c", "marketplace",
        "retail", "order", "inventory", "collection", "wishlist", "cod"
    ],
    "saas": [
        "software", "app", "platform", "dashboard", "subscription", "trial",
        "features", "pricing", "users", "team", "workspace", "integration",
        "api", "workflow", "automation", "b2b", "enterprise", "seats"
    ],
    "fintech": [
        "payment", "banking", "finance", "money", "transfer", "invest",
        "loan", "credit", "insurance", "wallet", "upi", "emi", "interest",
        "portfolio", "trading", "mutual fund", "rbi", "sebi", "gateway"
    ],
    "healthcare": [
        "doctor", "health", "medical", "patient", "appointment", "clinic",
        "hospital", "diagnosis", "symptom", "medicine", "prescription",
        "therapy", "wellness", "mental health", "consult", "hipaa"
    ],
    "edtech": [
        "course", "learn", "education", "student", "teacher", "curriculum",
        "certificate", "bootcamp", "cohort", "placement", "skill", "training",
        "mentor", "lecture", "quiz", "assignment", "syllabus", "tutor"
    ]
}

PRINCIPLE_FILES = {
    "cta":      "01-cta-psychology.md",
    "color":    "02-color-psychology.md",
    "social":   "03-social-proof.md",
    "fomo":     "04-fomo-scarcity.md",
    "eye":      "05-eye-patterns.md",
    "fold":     "06-above-fold.md",
    "pricing":  "07-pricing-psychology.md",
    "form":     "08-form-psychology.md",
    "trust":    "09-trust-signals.md",
    "dark":     "10-dark-patterns.md",
}

PRINCIPLE_ALIASES = {
    "call to action": "cta",
    "button":         "cta",
    "colours":        "color",
    "colours":        "color",
    "scarcity":       "fomo",
    "urgency":        "fomo",
    "reviews":        "social",
    "proof":          "social",
    "testimonial":    "social",
    "above fold":     "fold",
    "hero":           "fold",
    "f-pattern":      "eye",
    "z-pattern":      "eye",
    "eyetracking":    "eye",
    "checkout":       "form",
    "signup":         "form",
    "badge":          "trust",
    "ssl":            "trust",
    "guarantee":      "trust",
    "manipulation":   "dark",
    "ethics":         "dark",
}

COLORS = {
    "header":  "\033[95m",
    "blue":    "\033[94m",
    "green":   "\033[92m",
    "yellow":  "\033[93m",
    "red":     "\033[91m",
    "bold":    "\033[1m",
    "end":     "\033[0m",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def c(color: str, text: str) -> str:
    """Wrap text in terminal color."""
    return f"{COLORS.get(color, '')}{text}{COLORS['end']}"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def extract_sections(content: str, keyword: str) -> list[str]:
    """Return lines surrounding every occurrence of keyword (case-insensitive)."""
    lines   = content.splitlines()
    keyword = keyword.lower()
    hits    = []
    for i, line in enumerate(lines):
        if keyword in line.lower():
            start = max(0, i - 1)
            end   = min(len(lines), i + 5)
            block = "\n".join(lines[start:end])
            hits.append(block)
    return hits


def detect_industry(product_description: str) -> list[str]:
    """Return ranked list of matching industries for a product description."""
    desc    = product_description.lower()
    scores  = {}
    for industry, keywords in INDUSTRY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in desc)
        if score:
            scores[industry] = score
    return sorted(scores, key=scores.get, reverse=True)


def resolve_principle(name: str) -> str | None:
    """Resolve a principle name or alias to its short key."""
    name = name.lower().strip()
    if name in PRINCIPLE_FILES:
        return name
    for alias, key in PRINCIPLE_ALIASES.items():
        if alias in name:
            return key
    # Partial match
    for key in PRINCIPLE_FILES:
        if name in key:
            return key
    return None


def print_divider(char: str = "─", width: int = 60) -> None:
    print(c("blue", char * width))


def print_header(title: str) -> None:
    print_divider("═")
    print(c("bold", f"  {title}"))
    print_divider("═")


# ── Search Functions ──────────────────────────────────────────────────────────

def search_by_industry(industry: str) -> None:
    """Show psychology rules and quick-reference for an industry."""
    industry = industry.lower().strip()

    if industry not in INDUSTRY_KEYWORDS:
        print(c("red", f"\n✗ Unknown industry: '{industry}'"))
        print(f"  Available: {', '.join(INDUSTRY_KEYWORDS.keys())}\n")
        sys.exit(1)

    print_header(f"Psychology Rules — {industry.upper()}")

    # Load industry file
    industry_file = INDUSTRIES_DIR / f"{industry}.md"
    content       = read_file(industry_file)

    if not content:
        print(c("red", f"  ✗ Industry file not found: {industry_file}"))
        sys.exit(1)

    # Print first 80 lines (overview + primary principles)
    lines = content.splitlines()
    for line in lines[:80]:
        if line.startswith("# "):
            print(c("header", line))
        elif line.startswith("## "):
            print(c("green",  f"\n{line}"))
        elif line.startswith("### "):
            print(c("yellow", line))
        else:
            print(line)

    print_divider()

    # Load reasoning engine — extract industry row from weight matrix
    reasoning = read_file(REASONING_FILE)
    matrix_hits = extract_sections(reasoning, industry)
    if matrix_hits:
        print(c("bold", "\n  Priority Matrix (from reasoning engine):"))
        for hit in matrix_hits[:3]:
            print(c("blue", "  │ ") + hit.replace("\n", "\n  │ "))

    # Quick cheat sheet
    print(c("bold", "\n  Quick Reference:"))
    cheat_hits = extract_sections(reasoning, "Quick Reference")
    if cheat_hits:
        industry_line = [
            l for l in cheat_hits[0].splitlines()
            if industry in l.lower()
        ]
        for l in industry_line:
            print(c("green", f"  ✓ {l.strip()}"))

    print_divider()
    print(c("blue", f"\n  Full file: src/industries/{industry}.md\n"))


def search_by_principle(principle: str) -> None:
    """Show detailed rules for a psychology principle."""
    key = resolve_principle(principle)

    if not key:
        print(c("red", f"\n✗ Unknown principle: '{principle}'"))
        print(f"  Available: {', '.join(PRINCIPLE_FILES.keys())}")
        print(f"  Aliases  : {', '.join(PRINCIPLE_ALIASES.keys())}\n")
        sys.exit(1)

    filename = PRINCIPLE_FILES[key]
    filepath = PRINCIPLES_DIR / filename
    content  = read_file(filepath)

    if not content:
        print(c("red", f"  ✗ Principle file not found: {filepath}"))
        sys.exit(1)

    print_header(f"Principle: {key.upper()} → {filename}")

    lines = content.splitlines()
    for line in lines[:70]:
        if line.startswith("# "):
            print(c("header", line))
        elif line.startswith("## "):
            print(c("green",  f"\n{line}"))
        elif line.startswith("### "):
            print(c("yellow", line))
        elif line.startswith("- "):
            print(c("blue", "  • ") + line[2:])
        else:
            print(line)

    print_divider()
    print(c("blue", f"\n  Full file: src/principles/{filename}\n"))


def search_by_keyword(keyword: str) -> None:
    """Full-text search across all skill files."""
    print_header(f"Keyword Search: '{keyword}'")

    all_files: list[tuple[str, Path]] = []

    for f in PRINCIPLES_DIR.glob("*.md"):
        all_files.append(("principle", f))
    for f in INDUSTRIES_DIR.glob("*.md"):
        all_files.append(("industry", f))
    for f in EXAMPLES_DIR.glob("*.md"):
        all_files.append(("example", f))
    all_files.append(("reasoning", REASONING_FILE))

    total_hits = 0

    for category, filepath in all_files:
        content = read_file(filepath)
        hits    = extract_sections(content, keyword)

        if hits:
            label = filepath.stem
            print(c("green", f"\n  [{category.upper()}] {label}"))
            print_divider("─", 50)
            for i, hit in enumerate(hits[:3]):   # max 3 snippets per file
                for line in hit.splitlines():
                    kw_lower = keyword.lower()
                    if kw_lower in line.lower():
                        idx   = line.lower().index(kw_lower)
                        highlighted = (
                            line[:idx]
                            + c("yellow", line[idx:idx + len(keyword)])
                            + line[idx + len(keyword):]
                        )
                        print(f"  {highlighted}")
                    else:
                        print(f"  {line}")
                if i < len(hits) - 1:
                    print(c("blue", "  ···"))
            total_hits += len(hits)

    if total_hits == 0:
        print(c("red", f"\n  ✗ No results found for '{keyword}'\n"))
    else:
        print_divider()
        print(c("green", f"\n  ✓ Found {total_hits} matches across skill files\n"))


def search_by_product(description: str) -> None:
    """Auto-detect industry and show recommended psychology stack."""
    print_header(f"Product Analysis: '{description}'")

    industries = detect_industry(description)

    if not industries:
        print(c("yellow", "\n  Could not detect industry from description."))
        print("  Try: --industry ecommerce|saas|fintech|healthcare|edtech\n")
        return

    primary = industries[0]
    print(c("green", f"\n  ✓ Detected industry: {primary.upper()}"))

    if len(industries) > 1:
        print(c("blue", f"  Also matched: {', '.join(industries[1:])}"))

    # Load reasoning engine quick cheat sheet
    reasoning = read_file(REASONING_FILE)

    print(c("bold", "\n  Recommended Psychology Stack:"))
    print_divider("─", 50)

    cheat_lines = []
    in_cheat    = False
    for line in reasoning.splitlines():
        if "Quick Reference" in line:
            in_cheat = True
        if in_cheat and primary in line.lower():
            cheat_lines.append(line.strip())
        if in_cheat and line.startswith("## ") and "Quick" not in line:
            in_cheat = False

    for line in cheat_lines:
        print(c("green", f"  ✓ {line}"))

    # Load weight matrix for this industry
    print(c("bold", "\n  Principle Weights for This Industry:"))
    print_divider("─", 50)

    in_matrix = False
    for line in reasoning.splitlines():
        if "Weight Matrix" in line or "| Principle" in line:
            in_matrix = True
        if in_matrix:
            if primary[:4] in line or "Principle" in line or "---" in line:
                print(f"  {line}")
        if in_matrix and line.strip() == "" and "---" not in line:
            in_matrix = False

    # Anti-pattern warning
    print(c("bold", "\n  Anti-Patterns to Avoid:"))
    print_divider("─", 50)
    anti_hits = extract_sections(reasoning, f"{primary} +")
    for hit in anti_hits[:2]:
        for line in hit.splitlines():
            if line.strip():
                print(c("red", f"  ✗ {line.strip()}"))

    print_divider()
    print(c("blue", f"\n  Run for full details:"))
    print(f"  python3 scripts/search.py --industry {primary}")
    print(f"  python3 scripts/search.py --principle trust\n")


def list_all() -> None:
    """List all available principles, industries, and examples."""
    print_header("User Psychology Skill — Content Index")

    print(c("green", "\n  PRINCIPLES (10 core psychology rules):"))
    for key, filename in PRINCIPLE_FILES.items():
        filepath = PRINCIPLES_DIR / filename
        lines    = len(read_file(filepath).splitlines())
        print(f"  {c('yellow', key.ljust(10))}  {filename}  ({lines} lines)")

    print(c("green", "\n  INDUSTRIES (5 industry-specific guides):"))
    for f in sorted(INDUSTRIES_DIR.glob("*.md")):
        lines = len(read_file(f).splitlines())
        print(f"  {c('yellow', f.stem.ljust(15))}  ({lines} lines)")

    print(c("green", "\n  REAL WORLD EXAMPLES (5 company analyses):"))
    for f in sorted(EXAMPLES_DIR.glob("*.md")):
        lines = len(read_file(f).splitlines())
        print(f"  {c('yellow', f.stem.ljust(25))}  ({lines} lines)")

    print(c("green", "\n  REASONING ENGINE:"))
    lines = len(read_file(REASONING_FILE).splitlines())
    print(f"  {c('yellow', 'industry-rules.md'.ljust(25))}  ({lines} lines)")

    print_divider()
    print(c("blue", "\n  Usage examples:"))
    print("  python3 scripts/search.py --industry fintech")
    print("  python3 scripts/search.py --principle cta")
    print("  python3 scripts/search.py --keyword 'social proof'")
    print("  python3 scripts/search.py --product 'food delivery app for India'")
    print("  python3 scripts/search.py --list\n")


# ── CLI Entry Point ───────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="search.py",
        description="Search User Psychology Skill rules by industry, principle, or keyword.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/search.py --industry fintech
  python3 scripts/search.py --principle cta
  python3 scripts/search.py --keyword "countdown timer"
  python3 scripts/search.py --product "B2B invoicing SaaS for Indian startups"
  python3 scripts/search.py --list
        """
    )

    parser.add_argument(
        "--industry", "-i",
        metavar="INDUSTRY",
        help="Industry to look up (ecommerce|saas|fintech|healthcare|edtech)"
    )
    parser.add_argument(
        "--principle", "-p",
        metavar="PRINCIPLE",
        help="Principle to look up (cta|color|social|fomo|eye|fold|pricing|form|trust|dark)"
    )
    parser.add_argument(
        "--keyword", "-k",
        metavar="KEYWORD",
        help="Full-text search across all skill files"
    )
    parser.add_argument(
        "--product", "-r",
        metavar="DESCRIPTION",
        help="Describe your product — auto-detects industry and recommends stack"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all available content in the skill"
    )

    args = parser.parse_args()

    if args.industry:
        search_by_industry(args.industry)
    elif args.principle:
        search_by_principle(args.principle)
    elif args.keyword:
        search_by_keyword(args.keyword)
    elif args.product:
        search_by_product(args.product)
    elif args.list:
        list_all()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
