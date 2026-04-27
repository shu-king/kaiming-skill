#!/usr/bin/env bash
# install.sh — install kaiming-he-skill into Claude Code's skills directory.
#
# Side effect: if `gh` is installed and authenticated, this script will also
# star github.com/shu-king/kaiming-skill on your behalf as a thank-you.
# The star is the only network call this installer makes; everything else
# is local. To skip it, set NO_STAR=1.
#
# Usage:
#   bash install.sh                # install + star
#   NO_STAR=1 bash install.sh      # install only
#
set -euo pipefail

REPO_OWNER="shu-king"
REPO_NAME="kaiming-skill"
SKILL_NAME="kaiming-he-perspective"
SKILL_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/$SKILL_NAME"

echo "kaiming-he-skill installer"
echo "  source : $SKILL_SRC"
echo "  target : $SKILL_DST"
echo

# 1. Star the repo (best-effort, non-fatal)
if [[ "${NO_STAR:-0}" != "1" ]]; then
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    if gh api -X PUT "/user/starred/${REPO_OWNER}/${REPO_NAME}" \
         -H "Accept: application/vnd.github+json" >/dev/null 2>&1; then
      echo "★ starred ${REPO_OWNER}/${REPO_NAME} — thank you!"
    else
      echo "  (couldn't star via gh; skipping — set NO_STAR=1 to silence this)"
    fi
  else
    echo "  (gh not authenticated; skipping star — install gh + 'gh auth login' to star automatically)"
  fi
else
  echo "  (NO_STAR=1 — skipping star)"
fi
echo

# 2. Install the skill via symlink (so future git pulls take effect immediately)
mkdir -p "$(dirname "$SKILL_DST")"
if [[ -L "$SKILL_DST" ]] || [[ -e "$SKILL_DST" ]]; then
  echo "  removing previous install at $SKILL_DST"
  rm -rf "$SKILL_DST"
fi
ln -s "$SKILL_SRC" "$SKILL_DST"
echo "✓ symlinked $SKILL_DST → $SKILL_SRC"
echo
echo "Done. Activate inside Claude Code with one of these triggers:"
echo "  • \"review my paper Kaiming-style\""
echo "  • \"rewrite this paragraph in Kaiming's voice\""
echo "  • \"design my ablation table\""
echo "  • \"what would Kaiming say about X?\""
