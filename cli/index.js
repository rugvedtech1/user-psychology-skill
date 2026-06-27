#!/usr/bin/env node
/**
 * User Psychology Skill - CLI Installer
 * Installs the psychology skill into any AI-powered project
 *
 * Usage:
 *   npx user-psychology-skill install
 *   npx user-psychology-skill install --platform cursor
 *   npx user-psychology-skill info
 *   npx user-psychology-skill list
 */

const fs   = require("fs");
const path = require("path");
const os   = require("os");

// ── Constants ────────────────────────────────────────────────────────────────

const VERSION     = "1.0.0";
const REPO_URL    = "https://github.com/rugvedtech1/user-psychology-skill";
const SKILL_ROOT  = path.join(__dirname, "..");

const COLORS = {
  reset:  "\x1b[0m",
  bold:   "\x1b[1m",
  green:  "\x1b[32m",
  yellow: "\x1b[33m",
  blue:   "\x1b[34m",
  red:    "\x1b[31m",
  cyan:   "\x1b[36m",
};

const c = (color, text) => `${COLORS[color]}${text}${COLORS.reset}`;

// ── Platform Configs ─────────────────────────────────────────────────────────

const PLATFORMS = {
  "claude-desktop": {
    label:       "Claude Desktop",
    files: [
      {
        src:  ".claude/skills/user-psychology/SKILL.md",
        dest: ".claude/skills/user-psychology/SKILL.md",
      },
      {
        src:  "CLAUDE.md",
        dest: "CLAUDE.md",
      },
    ],
    note: "Claude Desktop will auto-activate this skill on UI/UX tasks.",
  },
  "claude-code": {
    label: "Claude Code",
    files: [
      {
        src:  "CLAUDE.md",
        dest: "CLAUDE.md",
      },
    ],
    note: "Claude Code reads CLAUDE.md automatically in your project root.",
  },
  cursor: {
    label: "Cursor",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      ".cursorrules",
        transform: addCursorHeader,
      },
    ],
    note: "Cursor reads .cursorrules automatically in your project root.",
  },
  windsurf: {
    label: "Windsurf",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      ".windsurfrules",
        transform: addWindsurfHeader,
      },
    ],
    note: "Windsurf reads .windsurfrules automatically in your project root.",
  },
  "github-copilot": {
    label: "GitHub Copilot",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      ".github/copilot-instructions.md",
        transform: addCopilotHeader,
      },
    ],
    note: "GitHub Copilot reads .github/copilot-instructions.md automatically.",
  },
  "gemini-cli": {
    label: "Gemini CLI",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      "GEMINI.md",
        transform: addGeminiHeader,
      },
    ],
    note: "Gemini CLI reads GEMINI.md in your project root.",
  },
  continue: {
    label: "Continue",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      ".continuerules",
        transform: addContinueHeader,
      },
    ],
    note: "Continue reads .continuerules in your project root.",
  },
  "roo-code": {
    label: "Roo Code",
    files: [
      {
        src:       "CLAUDE.md",
        dest:      ".roo/rules.md",
        transform: addRooHeader,
      },
    ],
    note: "Roo Code reads .roo/rules.md in your project root.",
  },
  all: {
    label: "All Platforms",
    files: [],
    note:  "Installs for all supported platforms at once.",
  },
};

// ── Transform Functions ──────────────────────────────────────────────────────

function addCursorHeader(content) {
  return `# User Psychology Skill for Cursor
# Source: ${REPO_URL}
# Auto-activated on all UI/UX tasks

${content}`;
}

function addWindsurfHeader(content) {
  return `# User Psychology Skill for Windsurf
# Source: ${REPO_URL}
# Auto-activated on all UI/UX tasks

${content}`;
}

function addCopilotHeader(content) {
  return `# User Psychology Skill for GitHub Copilot
# Source: ${REPO_URL}
# These instructions activate automatically on UI/UX tasks

${content}`;
}

function addGeminiHeader(content) {
  return `# User Psychology Skill for Gemini CLI
# Source: ${REPO_URL}
# Auto-activated on all UI/UX tasks

${content}`;
}

function addContinueHeader(content) {
  return `# User Psychology Skill for Continue
# Source: ${REPO_URL}
# Auto-activated on all UI/UX tasks

${content}`;
}

function addRooHeader(content) {
  return `# User Psychology Skill for Roo Code
# Source: ${REPO_URL}
# Auto-activated on all UI/UX tasks

${content}`;
}

// ── File Utilities ───────────────────────────────────────────────────────────

function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

function copySkillFile(srcRelative, destAbsolute, transform) {
  const srcAbsolute = path.join(SKILL_ROOT, srcRelative);

  if (!fs.existsSync(srcAbsolute)) {
    print("red", `  ✗ Source file not found: ${srcRelative}`);
    return false;
  }

  ensureDir(path.dirname(destAbsolute));

  let content = fs.readFileSync(srcAbsolute, "utf8");
  if (typeof transform === "function") {
    content = transform(content);
  }

  fs.writeFileSync(destAbsolute, content, "utf8");
  return true;
}

// ── Print Utilities ──────────────────────────────────────────────────────────

function print(color, text) {
  console.log(c(color, text));
}

function divider(char = "─", width = 55) {
  console.log(c("blue", char.repeat(width)));
}

function header(title) {
  divider("═");
  console.log(c("bold", `  ${title}`));
  divider("═");
}

// ── Commands ─────────────────────────────────────────────────────────────────

function cmdInstall(platform = "claude-desktop", targetDir = process.cwd()) {
  header(`Installing User Psychology Skill v${VERSION}`);

  const platformsToInstall =
    platform === "all"
      ? Object.keys(PLATFORMS).filter((p) => p !== "all")
      : [platform];

  if (!PLATFORMS[platform]) {
    print("red", `\n  ✗ Unknown platform: '${platform}'`);
    print("yellow", `  Available: ${Object.keys(PLATFORMS).join(", ")}\n`);
    process.exit(1);
  }

  print("cyan", `\n  Target directory : ${targetDir}`);
  print("cyan", `  Platform(s)      : ${platformsToInstall.join(", ")}\n`);

  let totalFiles = 0;
  let failedFiles = 0;

  for (const p of platformsToInstall) {
    const config = PLATFORMS[p];
    print("yellow", `\n  Installing for ${config.label}...`);
    divider("─", 45);

    for (const file of config.files) {
      const destAbsolute = path.join(targetDir, file.dest);
      const ok = copySkillFile(file.src, destAbsolute, file.transform);

      if (ok) {
        print("green", `  ✓ Created: ${file.dest}`);
        totalFiles++;
      } else {
        failedFiles++;
      }
    }

    // Also copy src/ directory for full skill access
    const srcDir  = path.join(SKILL_ROOT, "src");
    const destSrc = path.join(targetDir, ".psychology-skill", "src");

    if (fs.existsSync(srcDir)) {
      copyDirRecursive(srcDir, destSrc);
      print("green", `  ✓ Created: .psychology-skill/src/ (full knowledge base)`);
      totalFiles++;
    }

    print("blue", `\n  ℹ ${config.note}`);
  }

  divider();

  if (failedFiles > 0) {
    print("red", `\n  ✗ ${failedFiles} file(s) failed to install.`);
    print("yellow", `  Make sure you are running from the skill root directory.\n`);
  } else {
    print("green", `\n  ✓ Successfully installed ${totalFiles} file(s)!`);
    print("bold",  `\n  Next steps:`);
    console.log(`  1. Open your project in your AI editor`);
    console.log(`  2. Ask: "Build a landing page for my [industry] product"`);
    console.log(`  3. Claude will automatically apply psychology principles`);
    console.log(`  4. Look for the "Psychology Decisions" table in the output`);
    print("blue", `\n  Docs: ${REPO_URL}\n`);
  }
}

function copyDirRecursive(src, dest) {
  ensureDir(dest);
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath  = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function cmdInfo() {
  header("User Psychology Skill — Info");

  console.log(`
  ${c("bold", "Name")}        : user-psychology-skill
  ${c("bold", "Version")}     : ${VERSION}
  ${c("bold", "Author")}      : rugvedtech1
  ${c("bold", "License")}     : MIT
  ${c("bold", "Repository")}  : ${REPO_URL}

  ${c("green", "What it does:")}
  Teaches Claude and other AI assistants 10 core user psychology
  principles so they automatically build high-converting UI/UX
  without you needing to explain psychology every time.

  ${c("green", "Principles covered:")}
  1.  CTA Psychology        6.  Above The Fold
  2.  Color Psychology      7.  Pricing Psychology
  3.  Social Proof          8.  Form Psychology
  4.  FOMO & Scarcity       9.  Trust Signals
  5.  Eye Patterns (F/Z)    10. Dark Patterns to Avoid

  ${c("green", "Industries supported:")}
  Ecommerce • SaaS • Fintech • Healthcare • Edtech

  ${c("green", "Platforms supported:")}
  Claude Desktop • Claude Code • Cursor • Windsurf
  GitHub Copilot • Gemini CLI • Continue • Roo Code
  `);

  divider();
  print("blue", `\n  Run: npx user-psychology-skill install\n`);
}

function cmdList() {
  header("Supported Platforms");

  for (const [key, config] of Object.entries(PLATFORMS)) {
    if (key === "all") continue;
    print("green",  `\n  ${config.label}`);
    print("yellow", `  Key: ${key}`);
    console.log(`  Files: ${config.files.map((f) => f.dest).join(", ")}`);
    console.log(`  Note : ${config.note}`);
  }

  divider();
  print("blue", `\n  Install for specific platform:`);
  console.log(`  npx user-psychology-skill install --platform cursor`);
  console.log(`  npx user-psychology-skill install --platform windsurf`);
  console.log(`  npx user-psychology-skill install --platform all\n`);
}

function cmdHelp() {
  header(`User Psychology Skill CLI v${VERSION}`);
  console.log(`
  ${c("bold", "Usage:")}
    npx user-psychology-skill <command> [options]

  ${c("bold", "Commands:")}
    install    Install the skill into current project
    info       Show skill information and principles
    list       List all supported platforms
    help       Show this help message

  ${c("bold", "Options:")}
    --platform <name>    Target platform (default: claude-desktop)
    --dir <path>         Target directory (default: current directory)

  ${c("bold", "Examples:")}
    npx user-psychology-skill install
    npx user-psychology-skill install --platform cursor
    npx user-psychology-skill install --platform all
    npx user-psychology-skill install --platform windsurf --dir ./my-project
    npx user-psychology-skill info
    npx user-psychology-skill list

  ${c("bold", "Supported platforms:")}
    claude-desktop  claude-code  cursor  windsurf
    github-copilot  gemini-cli   continue  roo-code  all

  ${c("bold", "Repository:")}
    ${REPO_URL}
  `);
}

// ── Argument Parser ──────────────────────────────────────────────────────────

function parseArgs(argv) {
  const args     = argv.slice(2);
  const command  = args[0] || "help";
  const options  = {};

  for (let i = 1; i < args.length; i++) {
    if (args[i] === "--platform" && args[i + 1]) {
      options.platform = args[++i];
    } else if (args[i] === "--dir" && args[i + 1]) {
      options.dir = path.resolve(args[++i]);
    }
  }

  return { command, options };
}

// ── Main ─────────────────────────────────────────────────────────────────────

function main() {
  const { command, options } = parseArgs(process.argv);

  switch (command) {
    case "install":
      cmdInstall(
        options.platform || "claude-desktop",
        options.dir      || process.cwd()
      );
      break;
    case "info":
      cmdInfo();
      break;
    case "list":
      cmdList();
      break;
    case "help":
    case "--help":
    case "-h":
      cmdHelp();
      break;
    default:
      print("red", `\n  ✗ Unknown command: '${command}'`);
      cmdHelp();
      process.exit(1);
  }
}

main();
