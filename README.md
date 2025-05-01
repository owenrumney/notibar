# Notibar

Notibar is a macOS menu bar app that will alert you to any notifications you have that you're specifically participating in or mentioned in.

# Building

Notibar is built using Python and relies on the following libraries:
- [rumps](https://github.com/jaredks/rumps) - Simple Python library for macOS status bar apps
- `requests` - For making GitHub API calls
- `keyring` - For securely storing your GitHub token

To set up the development environment:

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

You can now either run as `python notibar.py` or if you prefer to make it into an app using

```bash
make build # builds the app to dist
```

```bash
make install # builds that app to dist then copies to ~/Applications`
```

# Usage

## Prerequisites

You need to have a `GITHUB_TOKEN`, the only scope it needs is to read notifications.

## Configuration

1. Launch the app
2. Click the 📢 icon in the menu bar
3. Select "Settings"
4. Enter your GitHub token in the dialog box that appears
5. Click "Save"

## Features

- Shows a 📢 icon in the menu bar
- Displays notification count when you have unread notifications (e.g., "📢 (3)")
- Checks for new notifications every 5 minutes
- Only shows notifications where you are specifically mentioned or participating
- Click on any notification in the menu to view its details
- Settings option to update your GitHub token anytime

The app securely stores your GitHub token using the system keychain.

# Roadmap

I don't think much more will be done because its serving the purpose it was intended, I stop missing notifications.

- Add an icon
- Support marking notification as read
- Use more of the data from the notification in the menu item
- Add option to startup at login

