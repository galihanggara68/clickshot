# 📸 ClickShot — Annotated Screenshot Recorder from Click Events

ClickShot is a command-line tool that listens for mouse or touchpad click events, takes annotated screenshots at the cursor position, and generates an editable HTML log of your steps.

It supports:

- 📷 Screenshot tools: `grim`, `maim`, `scrot`
- 🖱️ Cursor providers: `hyprctl`, `xdotool`
- 🧠 Clean CLI
- 📝 Editable HTML output + printable/exportable

---

## 🚀 Features

- Annotates click/touch location with a red circle
- Auto-generates step-by-step HTML log
- Editable titles/descriptions
- HTML printable/exportable to PDF
- Supports both Wayland and X11 environments

---

## 🛠️ Installation

```bash
pip install clickshot
````
---

## 🧪 Requirements

Install at least one screenshot tool **and** one cursor position tool:

| Tool    | For                        | Install Command                                 |
| ------- | -------------------------- | ----------------------------------------------- |
| grim    | Screenshot                 | `sudo pacman -S grim` / `sudo apt install grim` |
| maim    | Screenshot                 | `sudo apt install maim`                         |
| scrot   | Screenshot                 | `sudo apt install scrot`                        |
| hyprctl | Cursor (Wayland, Hyprland) | Comes with Hyprland                             |
| xdotool | Cursor (X11)               | `sudo apt install xdotool`                      |
| convert | Annotation                 | `sudo apt install imagemagick`                  |

---

## ✅ Quick Start

```bash
clickshot record
```

This uses:

* `grim` as screenshot backend
* `hyprctl` as cursor provider
* Output directory: `~/click_screenshots`

---

## 📸 Select Backends Manually

### X11 Example:

```bash
clickshot record --screenshot maim --cursor xdotool
```

### Wayland (Hyprland):

```bash
clickshot record --screenshot grim --cursor hyprctl
```

### Fallback with `scrot`:

```bash
clickshot record --screenshot scrot --cursor xdotool
```

---

## 🔧 CLI Options

| Option         | Description                                  | Default               |
| -------------- | -------------------------------------------- | --------------------- |
| `--output-dir` | Where to save screenshots and HTML           | `~/click_screenshots` |
| `--screenshot` | Screenshot backend (`grim`, `maim`, `scrot`) | `grim`                |
| `--cursor`     | Cursor backend (`hyprctl`, `xdotool`)        | `hyprctl`             |

---

## ⌨️ Keyboard Controls

While running:

* Press `p` to **pause/resume**
* Press `q` to **quit gracefully**

---

## 📂 Output

Each click creates:

* An annotated `.png` screenshot with a red circle at the cursor
* Appended step to `index.html` with editable titles

You can open the HTML manually:

```bash
xdg-open ~/click_screenshots/index.html
```

Or print/export directly in your browser.

---

## 🧩 Extensibility

You can add new screenshot or cursor backends easily by adding classes under:

```
clickshot/backends/
```

See `grim_backend.py` or `xdotool_cursor.py` for examples.

---

## 🧠 Tips & Troubleshooting

* Ensure your compositor or DE supports the screenshot tool (e.g., `grim` works only on Wayland).
* On X11, prefer `maim` or `scrot` with `xdotool`.
* Use `--help` for CLI options:

```bash
clickshot record --help
```
---

## 🙌 Credits

Inspired by needs for lightweight UI documentation, bug reproduction steps, and instructional content.
