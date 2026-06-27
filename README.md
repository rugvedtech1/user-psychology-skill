<div align="center">

# 🧠 User Psychology Skill

### An AI Skill that teaches Claude and other AI assistants user psychology principles to automatically build high-converting, psychologically optimized UI/UX.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/rugvedtech1/user-psychology-skill)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-purple.svg)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-Supported-green.svg)](https://cursor.sh)
[![Windsurf](https://img.shields.io/badge/Windsurf-Supported-blue.svg)](https://windsurf.ai)
[![npm](https://img.shields.io/badge/npm-user--psychology--skill-red.svg)](https://www.npmjs.com/package/user-psychology-skill)

[Install Now](#-installation) • [See It In Action](#-how-it-works) • [Principles](#-psychology-principles) • [Industries](#-industries-covered) • [Contributing](#-contributing)

</div>

---

## 🚀 The Problem This Solves

Every time you ask Claude or Cursor to "build a landing page", you get code that **looks fine but does not convert**.

Why? Because AI assistants do not automatically know:
- Which CTA color drives clicks in fintech vs ecommerce
- How to apply FOMO ethically without destroying trust
- Which social proof type belongs above the fold vs near pricing
- Why healthcare UX must never use countdown timers
- How Amazon's "Only 3 left" psychology actually works

**This skill fixes that permanently.**

Install it once. Every UI/UX task Claude does from that point uses psychology automatically — without you needing to explain it every time.

---

## ✨ How It Works
You say:    "Build a landing page for my fintech startup"
Claude:     1. Reads SKILL.md → loads psychology knowledge

2. Detects industry → fintech

3. Loads fintech rules → trust signals heavy, blue palette, minimal FOMO

4. Applies above-fold psychology → headline + trust badge + single CTA

5. Applies social proof → client logos, transaction volume

6. Applies color psychology → navy blue for trust, white for clarity

7. Generates the full UI with psychology baked in

8. Explains every decision in Psychology Decisions table

### Output includes a Psychology Decisions Table:

| Principle | Applied | Reason | Expected Impact |
|-----------|---------|--------|-----------------|
| CTA Psychology | Blue "Get Started" button, first-person copy | Fintech requires trust color, not urgency color | +15-25% CTR |
| Color Psychology | Navy blue + white + green CTA | Blue = trust for financial products | Reduces bounce rate |
| Social Proof | Transaction volume + enterprise logos | B2B fintech needs scale proof | +30% trust score |
| FOMO | Not applied | Fintech users must not feel rushed on financial decisions | Prevents distrust |
| Trust Signals | RBI badge + encryption claim + partner banks | Regulatory trust is #1 conversion factor in fintech | +40% signup rate |

### Plus 3 A/B Test Recommendations every time.

---

## 📦 Installation

### Option 1: npx (Recommended — One Command)

```bash
# Install for Claude Desktop (default)
npx user-psychology-skill install

# Install for Cursor
npx user-psychology-skill install --platform cursor

# Install for Windsurf
npx user-psychology-skill install --platform windsurf

# Install for all platforms at once
npx user-psychology-skill install --platform all
```

### Option 2: Manual Install

```bash
# Clone the repository
git clone https://github.com/rugvedtech1/user-psychology-skill.git

# Copy skill files to your project
cp -r user-psychology-skill/.claude your-project/
cp user-psychology-skill/CLAUDE.md your-project/
```

### Option 3: Per Platform Manual Setup

| Platform | File to Copy | Destination |
|----------|-------------|-------------|
| Claude Desktop | `CLAUDE.md` + `.claude/` | Project root |
| Claude Code | `CLAUDE.md` | Project root |
| Cursor | `CLAUDE.md` → rename | `.cursorrules` |
| Windsurf | `CLAUDE.md` → rename | `.windsurfrules` |
| GitHub Copilot | `CLAUDE.md` → rename | `.github/copilot-instructions.md` |
| Gemini CLI | `CLAUDE.md` → rename | `GEMINI.md` |
| Continue | `CLAUDE.md` → rename | `.continuerules` |
| Roo Code | `CLAUDE.md` → rename | `.roo/rules.md` |

---

## 🧠 Psychology Principles

This skill teaches Claude 10 core psychology principles:

### 1. 🎯 CTA Psychology
Colors, placement, and wording that makes people click.
- First-person copy ("Start My Trial" vs "Start Your Trial")
- Action verb hierarchy: Get > Start > Join > Claim > Submit
- High contrast color rules per industry
- Sticky mobile CTA implementation

### 2. 🎨 Color Psychology
Emotional impact of colors mapped to each industry.
- Red → urgency (ecommerce, food)
- Blue → trust (fintech, healthcare, enterprise SaaS)
- Orange → enthusiasm (edtech, consumer SaaS)
- The 60-30-10 color rule applied automatically

### 3. 👥 Social Proof Patterns
Reviews, numbers, and logos placement for maximum trust.
- 7 types of social proof ranked by conversion impact
- Placement map: what goes above fold vs near pricing vs at checkout
- Formula: [Specific Result] + [Timeframe] + [Name, Title, Company]

### 4. ⏰ FOMO and Scarcity Design
Urgency triggers that convert without destroying trust.
- 4 types of scarcity: time, quantity, access, social
- Industry FOMO intensity guide (Healthcare = 0, Ecommerce = 5)
- Ethical scarcity checklist built in

### 5. 👁️ F-Pattern and Z-Pattern
How human eyes move on a webpage — and how to design for it.
- F-pattern: text-heavy pages, dashboards, listings
- Z-pattern: landing pages, homepages, focused conversion pages
- Left-side priority rules for maximum content visibility

### 6. 📐 Above The Fold Psychology
What must appear before scroll to hook users in 3 seconds.
- 5 mandatory above-fold elements
- Headline formulas that work by industry
- The 10 above-fold mistakes ranked by damage

### 7. 💰 Pricing Page Psychology
Anchoring, decoy pricing, and middle plan highlighting.
- Decoy pricing: why 3 plans beat 2 every time
- Price ratio formula: 1x / 2.5x / 10x
- Annual vs monthly toggle psychology
- Risk reversal placement rules

### 8. 📝 Form Completion Psychology
Reducing friction and maximizing completion rates.
- The 33% progress bar starting trick
- Field reduction framework: Tier 1 / Tier 2 / Tier 3
- Micro-copy formulas for every sensitive field
- Single column vs multi-column data

### 9. 🔒 Trust Signals
SSL badges, guarantees, and founder photos placement.
- 6 categories of trust signals ranked by impact
- Industry-specific trust requirements
- Trust copywriting: specific beats vague every time
- Full audit checklist

### 10. 🚫 Dark Patterns to Avoid
Manipulative UX that destroys long-term trust.
- 10 dark patterns with real examples and legal risks
- Ethical alternatives for every dark pattern
- Regulatory landscape: GDPR, India DPDP, US FTC
- Dark pattern audit checklist

---

## 🏭 Industries Covered

| Industry | Primary Principles | FOMO Level | Trust Level |
|----------|-------------------|------------|-------------|
| 🛒 Ecommerce | FOMO + Social Proof + CTA | Maximum | Medium |
| 💻 SaaS | Pricing + Above Fold + CTA | Medium | High |
| 💳 Fintech | Trust Signals + Color + Social Proof | Minimal | Maximum |
| 🏥 Healthcare | Trust + Color + Form Psychology | Zero | Maximum |
| 📚 Edtech | Social Proof + FOMO + Pricing | Medium-High | Medium |

---

## 🏆 Real World Examples Included

### 🛒 Amazon
- How "Only 3 left in stock" psychology works technically
- Why the orange Add to Cart button has not changed in 25 years
- The crossed-out price anchoring formula
- Real-time social scarcity stack analysis

### 🎬 Netflix
- The email-first micro-commitment strategy
- Why "Cancel anytime" in the hero INCREASES signups
- Dark background + red CTA psychology in entertainment
- "Leaving Soon" badge — ethical scarcity done right

### 🎵 Spotify
- Freemium friction design — deliberate and calculated
- Why upgrade CTA appears at exact pain moment
- Spotify Wrapped as social proof phenomenon
- Localized pricing psychology for India market

### 💳 Razorpay
- How one enterprise logo beats ten unknown logos
- Regulatory compliance as conversion feature
- Transaction volume as reliability proof
- Progressive KYC onboarding psychology

### 🍔 Swiggy
- Delivery time as primary conversion trigger
- Zero-input checkout for returning users
- Real-time operational data as ethical urgency
- Notification psychology that reduces anxiety

---

## 🔧 CLI Tools

```bash
# See all available content
npx user-psychology-skill list

# Get skill information
npx user-psychology-skill info

# Search psychology rules (requires clone)
python3 scripts/search.py --industry fintech
python3 scripts/search.py --principle cta
python3 scripts/search.py --keyword "countdown timer"
python3 scripts/search.py --product "food delivery app for India"
```

---

## 📁 Project Structure
user-psychology-skill/

├── CLAUDE.md                          ← Auto-activates skill in Claude

├── skill.json                         ← Skill metadata and platform config

├── .claude/skills/user-psychology/

│   └── SKILL.md                       ← Main psychology brain file

├── src/

│   ├── principles/                    ← 10 detailed psychology guides

│   │   ├── 01-cta-psychology.md

│   │   ├── 02-color-psychology.md

│   │   ├── 03-social-proof.md

│   │   ├── 04-fomo-scarcity.md

│   │   ├── 05-eye-patterns.md

│   │   ├── 06-above-fold.md

│   │   ├── 07-pricing-psychology.md

│   │   ├── 08-form-psychology.md

│   │   ├── 09-trust-signals.md

│   │   └── 10-dark-patterns.md

│   ├── industries/                    ← 5 industry-specific guides

│   │   ├── ecommerce.md

│   │   ├── saas.md

│   │   ├── fintech.md

│   │   ├── healthcare.md

│   │   └── edtech.md

│   ├── examples/                      ← Real world company analyses

│   │   ├── amazon-analysis.md

│   │   ├── netflix-analysis.md

│   │   ├── spotify-analysis.md

│   │   ├── razorpay-analysis.md

│   │   └── swiggy-analysis.md

│   └── reasoning/

│       └── industry-rules.md          ← Psychology decision engine

├── scripts/

│   └── search.py                      ← CLI search tool

├── cli/

│   ├── package.json                   ← npm package config

│   └── index.js                       ← npx installer

└── docs/

├── how-it-works.md

└── contributing-guide.md

---

## 🤝 Contributing

Contributions are welcome and encouraged.

### Ways to contribute:
- Add a new industry (gaming, real estate, travel)
- Add a new real world example analysis
- Add a new psychology principle
- Improve existing content with research citations
- Add platform support for a new AI tool
- Translate content to other languages

### How to contribute:
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/user-psychology-skill.git

# Create a branch
git checkout -b add-gaming-industry

# Make your changes
# Follow the existing file format

# Push and create a Pull Request
git push origin add-gaming-industry
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

MIT License — free to use, modify, and distribute.

See [LICENSE](LICENSE) for full text.

---

## ⭐ If This Helped You

If this skill improved your UI/UX output from Claude or any AI tool,
please star the repository. It helps others discover it.

**[⭐ Star on GitHub](https://github.com/rugvedtech1/user-psychology-skill)**

---

<div align="center">

Built with ❤️ by [rugvedtech1](https://github.com/rugvedtech1)

**[GitHub](https://github.com/rugvedtech1/user-psychology-skill) • [Issues](https://github.com/rugvedtech1/user-psychology-skill/issues) • [Discussions](https://github.com/rugvedtech1/user-psychology-skill/discussions)**

</div>
