# Manual Setup

## Find the active Chrome profile first

Open:

```text
chrome://version/
```

Record:

- **Google Chrome version**
- **Profile Path**

Example:

```text
C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
```

The final folder (`Default`, `Profile 1`, `Profile 2`, etc.) identifies the Chrome profile.

---

## Add iPhone Duo Outer

Open:

**Chrome DevTools → Settings → Devices → Add custom device**

Enter:

- Device: `iPhone Duo Outer`
- Width: `466`
- Height: `678`
- Device pixel ratio: `3`
- Device type: `Mobile`

Suggested User-Agent Client Hint form factor:

- `Mobile`

---

## Add iPhone Duo Inner

Add another custom device:

- Device: `iPhone Duo Inner`
- Width: `951`
- Height: `669`
- Device pixel ratio: `3`
- Device type: `Desktop (touch)`

Suggested User-Agent Client Hint form factor:

- `Tablet`

Use landscape orientation for the intended Inner view.

Optional Client Hint fields can remain blank for normal responsive-layout testing unless the tested site specifically depends on them.

---

## Windows installer troubleshooting

Before using the automatic installer:

1. Close every Chrome window.
2. Open Task Manager.
3. End any remaining `chrome.exe` processes.

Or run:

```bat
taskkill /F /IM chrome.exe
```

Then run:

```text
INSTALL_WINDOWS.bat
```

If Windows blocks access to the Chrome `Preferences` file, right-click the installer and choose:

```text
Run as administrator
```

Then reopen Chrome and check:

```text
F12 → Settings → Devices
```
