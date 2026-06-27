# Contributing to User Psychology Skill

Thank you for helping make AI-generated UI/UX more psychologically optimized.

## Ways to Contribute

### 1. Add a New Industry
Create `src/industries/your-industry.md` following the same structure as
existing industry files. Must include:
- Industry psychology overview
- Primary principles with weights
- Color psychology for that industry
- FOMO level and justification
- Form psychology specifics
- A/B test priority list

### 2. Add a New Real World Example
Create `src/examples/company-analysis.md` following the same structure.
Must include real, verifiable psychology patterns — not speculation.

### 3. Improve Existing Principles
Add research citations, new patterns, or better examples to any file
in `src/principles/`. Cite sources where possible.

### 4. Add Platform Support
Add a new platform to `cli/index.js` PLATFORMS object and document
the entrypoint file for that platform.

### 5. Fix Errors or Outdated Information
Psychology research evolves. If you find outdated stats or wrong
information, open an issue or submit a PR with correction and source.

## How to Submit

1. Fork the repository
2. Create a branch: `git checkout -b your-feature-name`
3. Make your changes following existing file format
4. Test: `python3 scripts/search.py --list` should show your additions
5. Commit with clear message: `git commit -m "add: gaming industry psychology"`
6. Push: `git push origin your-feature-name`
7. Open a Pull Request with description of what you added and why

## File Format Rules

- Use the same heading structure as existing files
- No placeholder content — every line must be real psychology knowledge
- Include industry-specific examples where possible
- Keep Indian market context in mind (this skill is India-aware)
- Do not add dark patterns as suggestions — only as warnings

## Commit Message Format
add: brief description of what was added

fix: brief description of what was fixed

improve: brief description of what was improved

docs: brief description of documentation change

## Code of Conduct

- Be respectful in all discussions
- Back claims with research or real examples
- No self-promotion in content files
- Keep focus on psychology principles, not personal opinions

## Questions?

Open a GitHub Discussion or Issue.
