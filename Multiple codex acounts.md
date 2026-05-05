You might want to switch between accounts on your Codex for whatever reason.
You can avoid logging in and out by having separate .codex folders.
I use .codex, .codex-profile2, and .codex-originalprofile, for example. The really important file in these folders is auth.json, which is used to authenticate. Using Codex CLI with another account is as simple as passing a home variable to it, and there are examples of this in the thread-dispatch skill. But the Codex desktop app will always use the auth.json from .codex, so I made this quick profile-switch script. All the .codex-profile folders and .codex-original should be in the same folder.

When creating .codex-profile2, you can copy the whole .codex folder with a new name, but instead you might want to replace some files in the new folder with symlinks to the original folder, for example the AGENTS.md file and the entire skills folder. That way you won't have to install the same skills in both profiles or forget to install them. You might also want config.toml to be a link, or you might want it specifically set up differently for different profiles.

## create the script

mkdir -p ~/bin
cat > ~/bin/switch-codex-profile <<'EOF'
#!/bin/zsh
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: switchCodex <profile-name>"
  echo "Example: switchCodex slobodan"
  echo "         switchCodex second"
  exit 1
fi

PROFILE="$1"
BASE="$HOME/.codex"
SRC_DIR="$HOME/.codex-$PROFILE"
SRC_AUTH="$SRC_DIR/auth.json"
DST_AUTH="$BASE/auth.json"

if [[ ! -d "$BASE" ]]; then
  echo "Error: $BASE does not exist"
  exit 1
fi

if [[ ! -f "$SRC_AUTH" ]]; then
  echo "Error: $SRC_AUTH not found"
  exit 1
fi

# Backup current auth.json if it exists
if [[ -f "$DST_AUTH" ]]; then
  cp -p "$DST_AUTH" "$BASE/auth.json.bak.$(date +%Y%m%d%H%M%S)"
fi

# Copy selected auth into ~/.codex
cp -p "$SRC_AUTH" "$DST_AUTH"

echo "Switched Codex auth to profile: $PROFILE"
echo "Source: $SRC_AUTH"
echo "Target: $DST_AUTH"
EOF


## make executable and use 

chmod +x ~/bin/switch-codex-profile
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
echo 'alias switchCodex="switch-codex-profile"' >> ~/.zshrc
source ~/.zshrc
switchCodex profile2
