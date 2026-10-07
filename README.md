# iPhone Duo Chrome DevTools Profiles

Unofficial Chrome DevTools custom-device profiles for testing **Duo Outer** and **Duo Inner** responsive layouts.

Designed for designers, developers, QA teams and anyone who needs to preview, capture screenshots, record videos or test responsive behaviour without having the physical device available.

## Included profiles

| Profile | CSS Viewport | DPR | Target Physical Resolution | Chrome Behaviour |
|---|---:|---:|---:|---|
| **iPhone Duo Outer** | `466 × 678` | `3` | `1398 × 2034` | Mobile + Touch |
| **iPhone Duo Inner** | `951 × 669` | `3` | `2853 × 2007` | Desktop (Touch) / Tablet-style |

> **Important:** These are unofficial Chrome DevTools testing presets. The profiles do not emulate physical Apple hardware, Safari/WebKit, hinges, cut-outs or device-specific safe areas.

---

# Why these profiles exist

Chrome DevTools uses **CSS pixels** for responsive viewport dimensions.

Entering a physical Retina resolution directly into Chrome DevTools can result in a website treating the viewport as an extremely large desktop display.

For example, entering:

```text
2853 × 2007
```

directly as the browser viewport can cause:

- extremely small navigation
- tiny cards
- incorrect responsive breakpoints
- desktop layouts instead of tablet layouts
- unrealistic screenshots

The correct approach is to use the CSS viewport together with the Device Pixel Ratio.

### Duo Outer

```text
CSS viewport:
466 × 678

Device Pixel Ratio:
3

466 × 3 = 1398
678 × 3 = 2034
```

### Duo Inner

```text
CSS viewport:
951 × 669

Device Pixel Ratio:
3

951 × 3 = 2853
669 × 3 = 2007
```

This allows Chrome to render the website using a realistic responsive viewport while retaining the intended high-density output relationship.

---

# Repository contents

```text
iphone-duo-chrome-devtools-profiles/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
│
├── INSTALL_WINDOWS.bat
├── DOCTOR_WINDOWS.bat
├── install_macos_linux.sh
│
├── docs/
│   └── MANUAL_SETUP.md
│
├── profiles/
│   ├── iphone-duo-devtools.json
│   └── reference.json
│
└── tools/
    └── duo_profiles.py
```

---

# Windows Installation

## Step 1 — Download the repository

Click:

```text
Code → Download ZIP
```

Extract the ZIP.

The extracted folder will usually be named:

```text
iphone-duo-chrome-devtools-profiles-main
```

---

## Step 2 — Find the Chrome profile

Before closing Chrome, open:

```text
chrome://version/
```

Find:

```text
Profile Path
```

Example:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
```

The final folder identifies the Chrome profile.

Examples:

```text
Default
Profile 1
Profile 2
Profile 3
```

Also note the:

```text
Google Chrome version
```

The Chrome version is useful when troubleshooting because Chrome's internal DevTools configuration can change between releases.

---

# Step 3 — Fully close Chrome

This step is important.

Closing the Chrome window may not completely close Chrome because background processes can remain active.

The installer changes Chrome's profile `Preferences` file. An active Chrome process can overwrite that file.

### Recommended method

Open:

```text
Task Manager
```

Find every:

```text
chrome.exe
```

process and choose:

```text
End task
```

Alternatively, open Command Prompt and run:

```bat
taskkill /F /IM chrome.exe
```

To verify that Chrome is no longer running:

```bat
tasklist | findstr /I chrome.exe
```

If no result appears, Chrome is fully closed.

---

# Step 4 — Run the installer

Inside the extracted repository folder, double-click:

```text
INSTALL_WINDOWS.bat
```

If multiple Chrome profiles exist, the installer may display:

```text
Chrome profiles found:

1. Default
2. Profile 1
3. Profile 2
4. Profile 3
```

Choose the profile matching the `Profile Path` found earlier at:

```text
chrome://version/
```

Example:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
```

means:

```text
Choose: Default
```

---

# Windows permission issue

If the installer cannot update the Chrome Preferences file, right-click:

```text
INSTALL_WINDOWS.bat
```

and select:

```text
Run as administrator
```

Administrator mode should only be necessary when Windows permissions block access to the Chrome profile.

---

# Step 5 — Verify the Windows installation

Reopen Google Chrome.

Open DevTools:

```text
F12
```

Open DevTools Settings:

```text
F1
```

Then go to:

```text
Settings → Devices
```

The following custom devices should now appear:

```text
iPhone Duo Outer
iPhone Duo Inner
```

Make sure both devices are enabled.

---

# Step 6 — Open Device Toolbar

Use:

```text
Ctrl + Shift + M
```

Select:

```text
iPhone Duo Outer
```

or:

```text
iPhone Duo Inner
```

Reload the website after switching profiles.

---

# Expected Windows profiles

## iPhone Duo Outer

```text
Width:
466

Height:
678

DPR:
3

Device type:
Mobile
```

## iPhone Duo Inner

```text
Width:
951

Height:
669

DPR:
3

Device type:
Desktop (touch)

Recommended orientation:
Landscape
```

---

# Windows Troubleshooting

If the installer says:

```text
Added: 2
```

but the profiles do not appear in Chrome, check the following.

### Confirm Chrome Profile Path

Open:

```text
chrome://version/
```

Check that the selected installer profile matches:

```text
Profile Path
```

### Completely terminate Chrome

Run:

```bat
taskkill /F /IM chrome.exe
```

Then rerun:

```text
INSTALL_WINDOWS.bat
```

### Run as administrator

If Windows permissions are blocking the Preferences file:

```text
Right-click INSTALL_WINDOWS.bat
→ Run as administrator
```

### Check Devices directly

Open:

```text
F12
→ Settings
→ Devices
```

Check this page before checking the Device Toolbar dropdown.

---

# Windows Diagnostic Tool

A diagnostic helper is included:

```text
DOCTOR_WINDOWS.bat
```

Use this only when something is not working.

The diagnostic tool checks:

```text
Chrome running state
Chrome profile
Chrome Preferences path
Duo profile presence
Custom-device data
Configuration validity
```

The diagnostic tool does not install additional software.

---

# Windows Chrome profile paths

Typical Chrome profile root:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\
```

Default profile:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
```

Preferences file:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default\Preferences
```

Additional profiles:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Profile 1\Preferences
```

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Profile 2\Preferences
```

The installer modifies the selected Chrome profile only.

---

# macOS Installation

## Step 1 — Download the repository

From GitHub select:

```text
Code → Download ZIP
```

The ZIP will normally download into:

```text
Downloads
```

After extraction, GitHub usually names the folder:

```text
iphone-duo-chrome-devtools-profiles-main
```

---

# Step 2 — Find the Chrome profile

Before closing Chrome, open:

```text
chrome://version/
```

Find:

```text
Profile Path
```

Example:

```text
/Users/YourName/Library/Application Support/Google/Chrome/Default
```

The final folder identifies the Chrome profile:

```text
Default
Profile 1
Profile 2
...
```

Also note the:

```text
Google Chrome version
```

---

# Step 3 — Open Terminal

Open:

```text
Applications
→ Utilities
→ Terminal
```

Then run:

```bash
cd ~/Downloads
```

Check the Downloads folder:

```bash
ls
```

Look for:

```text
iphone-duo-chrome-devtools-profiles-main
```

---

# Step 4 — Enter the repository folder

Run:

```bash
cd iphone-duo-chrome-devtools-profiles-main
```

Then:

```bash
ls
```

The output should contain files such as:

```text
README.md
install_macos_linux.sh
tools
profiles
docs
```

---

# Step 5 — Allow the installer to run

Run:

```bash
chmod +x install_macos_linux.sh
```

---

# Step 6 — Fully close Google Chrome

Run:

```bash
pkill -x "Google Chrome"
```

Nothing appearing afterward is normal.

This command ensures that Chrome and remaining background Chrome processes are closed before the Preferences file is changed.

---

# Step 7 — Run the Mac installer

Run:

```bash
./install_macos_linux.sh
```

The complete command sequence is:

```bash
cd ~/Downloads
ls
cd iphone-duo-chrome-devtools-profiles-main
ls
chmod +x install_macos_linux.sh
pkill -x "Google Chrome"
./install_macos_linux.sh
```

---

# If the downloaded folder has a different name

Use:

```bash
ls
```

and copy the exact folder name.

For example:

```text
iphone-duo-chrome-devtools-profiles-main-2
```

would require:

```bash
cd iphone-duo-chrome-devtools-profiles-main-2
```

---

# macOS permission error

If macOS returns:

```text
Permission denied
```

run:

```bash
bash install_macos_linux.sh
```

instead.

---

# Step 8 — Choose the correct Chrome profile

If multiple profiles are detected, choose the profile matching the path found earlier at:

```text
chrome://version/
```

Example:

```text
/Users/YourName/Library/Application Support/Google/Chrome/Default
```

means:

```text
Default
```

---

# Step 9 — Verify the Mac installation

Reopen Google Chrome.

Open DevTools:

```text
⌘ Command + ⌥ Option + I
```

Open Device Toolbar:

```text
⌘ Command + Shift + M
```

Open DevTools Settings:

```text
F1
```

Then go to:

```text
Settings → Devices
```

The following custom devices should appear:

```text
iPhone Duo Outer
iPhone Duo Inner
```

---

# macOS Chrome profile paths

Typical Chrome profile root:

```text
~/Library/Application Support/Google/Chrome/
```

Default profile:

```text
~/Library/Application Support/Google/Chrome/Default
```

Preferences file:

```text
~/Library/Application Support/Google/Chrome/Default/Preferences
```

Additional profiles:

```text
~/Library/Application Support/Google/Chrome/Profile 1/Preferences
```

```text
~/Library/Application Support/Google/Chrome/Profile 2/Preferences
```

---

# macOS Troubleshooting

If the profiles do not appear:

Fully close Chrome again:

```bash
pkill -x "Google Chrome"
```

Return to the repository:

```bash
cd ~/Downloads/iphone-duo-chrome-devtools-profiles-main
```

Run the installer again:

```bash
./install_macos_linux.sh
```

If direct execution fails:

```bash
bash install_macos_linux.sh
```

Then reopen Chrome and check:

```text
DevTools
→ Settings
→ Devices
```

---

# Manual Installation

If automatic installation does not work on a particular Chrome version, both profiles can be created manually.

Open:

```text
Chrome DevTools
→ Settings
→ Devices
→ Add custom device
```

---

# Manual — iPhone Duo Outer

Enter:

```text
Device:
iPhone Duo Outer

Width:
466

Height:
678

Device Pixel Ratio:
3

Device Type:
Mobile
```

Recommended form factor:

```text
Mobile
```

---

# Manual — iPhone Duo Inner

Enter:

```text
Device:
iPhone Duo Inner

Width:
951

Height:
669

Device Pixel Ratio:
3

Device Type:
Desktop (touch)
```

Recommended form factor:

```text
Tablet
```

Recommended orientation:

```text
Landscape
```

---

# Optional Client Hint settings

The following fields can normally remain empty:

```text
Full browser version
Platform
Platform version
Architecture
Device model
```

These fields are only necessary when testing a website that specifically relies on User-Agent Client Hints.

---

# Using the profiles

After installation:

Open the website that needs testing.

Open Chrome DevTools.

### Windows

```text
F12
```

Device Toolbar:

```text
Ctrl + Shift + M
```

### macOS

Open DevTools:

```text
⌘ + ⌥ + I
```

Device Toolbar:

```text
⌘ + Shift + M
```

Select:

```text
iPhone Duo Outer
```

or:

```text
iPhone Duo Inner
```

Reload the page after changing profiles.

---

# Screenshot workflow

For screenshots:

Open Device Toolbar and choose the required Duo profile.

Open Chrome Command Menu.

### Windows

```text
Ctrl + Shift + P
```

### macOS

```text
⌘ + Shift + P
```

Search:

```text
Capture screenshot
```

This makes the profiles useful for:

```text
UI screenshots
A/B testing
Marketing creative
QA documentation
Product demos
Video capture
Responsive design reviews
```

---

# Uninstalling the profiles

## Windows

Close Chrome completely.

Open Command Prompt inside the repository folder and run:

```bat
python tools\duo_profiles.py remove
```

or:

```bat
py -3 tools\duo_profiles.py remove
```

---

## macOS

Close Chrome:

```bash
pkill -x "Google Chrome"
```

Enter the repository folder:

```bash
cd ~/Downloads/iphone-duo-chrome-devtools-profiles-main
```

Run:

```bash
python3 tools/duo_profiles.py remove
```

Reopen Chrome afterward.

---

# Diagnostic commands

## Windows

List installed custom devices:

```bat
py -3 tools\duo_profiles.py list
```

Run diagnostics:

```bat
py -3 tools\duo_profiles.py doctor
```

Remove Duo devices:

```bat
py -3 tools\duo_profiles.py remove
```

---

## macOS

List installed custom devices:

```bash
python3 tools/duo_profiles.py list
```

Run diagnostics:

```bash
python3 tools/duo_profiles.py doctor
```

Remove Duo devices:

```bash
python3 tools/duo_profiles.py remove
```

---

# Technical details

Chrome stores custom DevTools devices inside the selected profile's:

```text
Preferences
```

file.

The relevant preference is:

```text
devtools.preferences.custom-emulated-device-list
```

The installer:

```text
Finds the selected Chrome profile
Reads existing custom devices
Creates a Preferences backup
Adds or updates the Duo profiles
Preserves unrelated custom devices
Writes the updated Preferences file
Verifies that the Duo profiles exist on disk
```

---

# Preferences backup

Before the Preferences file is changed, the installer creates a timestamped backup.

Example:

```text
Preferences.duo-backup-20261007-142300
```

This allows the original Chrome configuration to be recovered if necessary.

---

# Important limitations

Chrome currently does not provide an official:

```text
Import Custom Devices
```

function for custom DevTools device profiles.

The automatic installer therefore modifies Chrome's internal DevTools Preferences configuration.

Because this is an internal Chrome setting:

- Chrome may change the storage format in future versions.
- Behaviour may differ between Chrome versions.
- Manual setup remains available as a fallback.
- Chrome emulation is not physical-device testing.
- Chrome does not emulate Safari/WebKit.
- Hardware hinges and cut-outs are not currently simulated.
- OS-specific behaviour may differ from real hardware.

Final QA should still be performed on physical hardware whenever possible.

---

# Reporting an issue

When reporting a problem, include:

```text
Operating system:
Chrome version:
Chrome Profile Path:
Installer output:
Whether Chrome was fully closed:
Whether the profiles appear in Settings → Devices:
```

Chrome version and Profile Path are available from:

```text
chrome://version/
```

---

# Contributing

Contributions and improvements are welcome.

Useful contributions include:

```text
Chrome compatibility updates
Improved installers
Verified viewport information
Safe-area information
macOS improvements
Windows improvements
Linux improvements
Documentation fixes
```

Pull requests can be submitted through GitHub.

---

# Disclaimer

This project is unofficial.

The presets are intended for responsive design and development testing only.

No claim is made that the profiles reproduce physical Apple hardware, Safari/WebKit behaviour or future production device specifications exactly.

---

# License

MIT License.

Free to use, modify, redistribute and share.
