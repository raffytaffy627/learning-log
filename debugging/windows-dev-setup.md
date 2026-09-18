# Debugging: Windows Dev Setup

Environment issues from setting up VS Code, Git, and Python on my Windows PC.

## Issue: "Python was not found"

**Date:** 2026-09-18

**What I saw:** Running `python --version` in PowerShell said: `Python was not found; run without arguments to install from the Microsoft Store...`

**What I tried:** The VS Code Python extension had installed Python through `uv`, and scripts ran fine with the ▶ button, but the `python` command itself didn't work in the terminal.

**Cause:** Two things. Windows has built-in "app execution aliases" that send `python` to the Microsoft Store, and uv's install folder (`C:\Users\Raf\.local\bin`) wasn't on my PATH yet.

**Fix:** Ran `uv python install --default`, turned off the python.exe and python3.exe aliases in Windows Settings, ran `uv tool update-shell` to add uv's folder to PATH, then fully restarted VS Code.

**Lesson:** When a command "isn't found," check two things: is the program actually installed, and is its folder on PATH? Terminals only pick up PATH changes after a restart.

## Issue: Todo Tree "Failed to find vscode-ripgrep"

**Date:** 2026-09-18

**What I saw:** The Todo Tree extension showed `Failed to find vscode-ripgrep - please install ripgrep manually`.

**What I tried:** Reloaded the window. Installed ripgrep with `winget install BurntSushi.ripgrep.MSVC`, but `Get-Command rg` still said not found. The winget shortcut path didn't exist either.

**Cause:** Newer VS Code versions changed where ripgrep is bundled, so the extension couldn't find it. After installing it myself, VS Code's terminals still had the old PATH.

**Fix:** Searched for `rg.exe` directly with `Get-ChildItem ... -Recurse -Filter rg.exe`, then set the full path in `todo-tree.ripgrep.ripgrep` in settings.json (with double backslashes). Added it to `settingsSync.ignoredSettings` so the Windows-only path doesn't sync to my Ubuntu laptop.

**Lesson:** When PATH isn't cooperating, search for the file directly. In JSON, backslashes need to be doubled (`\\`).

## Open: PowerShell profile "Access denied"

**What I see:** Every new terminal shows `Access to the path '...\Microsoft.PowerShell_profile.ps1' is denied.`

**Status:** Not fixed yet. It doesn't block anything, so I'm leaving it for later.