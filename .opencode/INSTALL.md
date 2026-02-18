# GRC Plugin — OpenCode Installation

Follow these steps to install the GRC Knowledge Plugin for OpenCode.

## Step 1: Clone the repository

```bash
git clone https://github.com/mlunato47/claude-grc-plugin.git ~/.config/opencode/grc
```

## Step 2: Symlink the plugin

```bash
mkdir -p ~/.config/opencode/plugins
ln -s ~/.config/opencode/grc/.opencode/plugins/grc.js ~/.config/opencode/plugins/grc.js
```

## Step 3: Symlink the skills

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/grc/grc/skills/grc-knowledge ~/.config/opencode/skills/grc-knowledge
```

## Step 4: Symlink the commands

```bash
mkdir -p ~/.config/opencode/commands
for cmd in ~/.config/opencode/grc/grc/commands/*.md; do
  ln -s "$cmd" ~/.config/opencode/commands/$(basename "$cmd")
done
```

## Step 5: Restart OpenCode

Close and reopen OpenCode. The GRC skill will be loaded automatically and all `/grc-*` commands will be available.

## Verify

Type `/grc-control-lookup nist ac-2` to verify the plugin is working. You should get a detailed control lookup with specific control IDs, baselines, and evidence requirements.

## Update

To update to the latest version:

```bash
cd ~/.config/opencode/grc
git pull
```

The symlinks will automatically pick up the updated files.

## Uninstall

```bash
rm ~/.config/opencode/plugins/grc.js
rm ~/.config/opencode/skills/grc-knowledge
for cmd in ~/.config/opencode/commands/*.md; do
  [ -L "$cmd" ] && readlink "$cmd" | grep -q "opencode/grc/" && rm "$cmd"
done
rm -rf ~/.config/opencode/grc
```
