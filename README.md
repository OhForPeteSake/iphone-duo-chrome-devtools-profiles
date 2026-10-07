# iPhone Duo Chrome DevTools Profiles

Unofficial Chrome DevTools custom-device presets for responsive testing of Duo-style **Outer** and **Inner** viewports.

Useful for responsive design, QA, screenshots, screen recordings and product demos.

> These are Chrome responsive-testing presets, not physical-device or Safari/WebKit emulation.

## Profiles

| Profile | CSS viewport | DPR | Target physical pixels | DevTools behaviour |
|---|---:|---:|---:|---|
| iPhone Duo Outer | `466 × 678` | `3` | `1398 × 2034` | Mobile + touch |
| iPhone Duo Inner | `951 × 669` | `3` | `2853 × 2007` | Desktop rendering + touch |

## Before installing on Windows

### 1. Find the Chrome profile being used

Open Chrome and go to:

```text
chrome://version/
```

Look for:

```text
Profile Path
```

Example:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
```

The final folder tells which option to choose in the installer:

```text
Default
Profile 1
Profile 2
Profile 3
...
```

Also note the **Google Chrome version** shown on the same `chrome://version/` page. This is useful when reporting an issue because Chrome's internal DevTools settings can change between releases.

### 2. Close Chrome completely

Closing all Chrome windows may not be enough because Chrome can keep background processes running.

Recommended:

```text
Task Manager → Details / Processes → end every chrome.exe process
```

Or from Command Prompt:

```bat
taskkill /F /IM chrome.exe
```

To check:

```bat
tasklist | findstr /I chrome.exe
```

If nothing is returned, Chrome is fully closed.

### 3. Run the installer

Double-click:

```text
INSTALL_WINDOWS.bat
```

If Windows permissions prevent the Chrome Preferences file from being updated, right-click the installer and choose:

```text
Run as administrator
```

Administrator mode should be treated as a troubleshooting fallback rather than a requirement on every PC.

Choose the profile that matched the `Profile Path` shown in `chrome://version/`.

### 4. Reopen Chrome and verify

Open:

```text
F12 → Settings → Devices
```

Expected custom devices:

```text
iPhone Duo Outer
iPhone Duo Inner
```

Then open Device Toolbar with:

```text
Ctrl + Shift + M
```

and select the required profile.

---

## Chrome profile / Preferences paths

Chrome stores custom DevTools device settings inside the selected Chrome profile's `Preferences` file.

### Windows

Typical root:

```text
%LOCALAPPDATA%\Google\Chrome\User Data\
```

Examples:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default\Preferences

C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Profile 1\Preferences

C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Profile 2\Preferences
```

### macOS

Typical root:

```text
~/Library/Application Support/Google/Chrome/
```

Example:

```text
~/Library/Application Support/Google/Chrome/Default/Preferences
```

### Linux

Typical root:

```text
~/.config/google-chrome/
```

Example:

```text
~/.config/google-chrome/Default/Preferences
```

The installer updates:

```text
devtools.preferences.custom-emulated-device-list
```

A timestamped backup of the `Preferences` file is created before any change is written.

---

## Why CSS dimensions are smaller than the screenshot dimensions

Chrome DevTools expects viewport dimensions in **CSS pixels**. DPR then controls the pixel-density scaling.

```text
Outer
466 × 3 = 1398
678 × 3 = 2034

Inner
951 × 3 = 2853
669 × 3 = 2007
```

Using `2853 × 2007` directly as the CSS viewport makes responsive websites behave like they are running on a very large desktop display, which can make cards, navigation and text appear much too small.

---

## Manual setup

If direct Preferences installation does not work on a particular Chrome version, add the devices manually:

**Chrome DevTools → Settings → Devices → Add custom device**

Full instructions:

```text
docs/MANUAL_SETUP.md
```

---

## Troubleshooting

### Installer says the profiles were added, but they do not appear in DevTools

Check these in order:

1. Confirm the correct Chrome profile using `chrome://version/`.
2. Fully terminate every `chrome.exe` process.
3. Run `INSTALL_WINDOWS.bat` again.
4. If the Preferences file is blocked by Windows permissions, use **Run as administrator**.
5. Reopen Chrome.
6. Check **F12 → Settings → Devices** before checking the Device Toolbar dropdown.
7. If needed, close Chrome again and run:

```text
DOCTOR_WINDOWS.bat
```

### Report an issue

Include:

```text
Chrome version:
Profile Path:
Windows/macOS/Linux version:
Installer output:
Whether the profiles appear in F12 → Settings → Devices:
```

Both **Chrome version** and **Profile Path** are available from:

```text
chrome://version/
```

---

## Other commands

```bash
python tools/duo_profiles.py list
python tools/duo_profiles.py doctor
python tools/duo_profiles.py remove
```

---

## Important limitation

Chrome does not currently expose a supported **Import Custom Devices** button. The installer updates Chrome's internal custom-device preference and creates a backup first.

Because Chrome can change this internal storage format in future releases, the manual setup instructions remain the fallback.

## License

MIT
