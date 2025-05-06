from rumps import rumps as menu
import rumps

from github.credentials import get_github_token, save_github_token
from github.notifications import get_github_notifications, get_html_url, mark_notification_as_done
import webbrowser


def open_url(url, notification_id):
    """
    Open a URL in the default web browser.
    """
    print(f"Opening URL: {url} for notification ID: {notification_id}")
    html_url = get_html_url(url)
    if html_url:
        webbrowser.open(html_url)
    else:
        webbrowser.open(url)
    mark_notification_as_done(notification_id)

class NotibarApp(rumps.App):
    def __init__(self):
        super(NotibarApp, self).__init__("Notibar", quit_button=None)
        self.menu = ["Refresh", "Settings", "Quit"]
        self.notification_count = 0

    @rumps.clicked("Refresh")
    def refresh(self, sender):
        self.update_notifications(sender)

    @rumps.clicked("Settings")
    def settings(self, sender):
        window = rumps.Window("Enter your GITHUB_TOKEN","Settings",  default_text=get_github_token(), 
                              dimensions=(500, 20), ok="Save", cancel="Cancel")

        response = window.run()
        if response.clicked == 1:
            token = response.text
            # Save the token using keyring or any other method
            # save_github_token(token)
            rumps.alert("Token Saved", "Your GitHub token has been saved.")
            save_github_token(token)
        else:
            rumps.notification("Notibar", "Cancelled", "Settings were not saved.")
    
    @rumps.timer(600)
    def update_notifications(self, sender):
        for item in self.menu:
                if item not in ['Refresh', 'Settings', 'Quit']:
                    del self.menu[item]
                elif isinstance(item, menu.MenuItem):
                    self.menu.remove(item)
        notifications = get_github_notifications()
        self.notification_count = len(notifications)
        if self.notification_count > 0:
            self.title = f"📢 ({self.notification_count})"
            for notification in notifications:
                id = notification.get('id')
                repo = notification.get('repository', {}).get('name', 'Unknown Repository')
                title = notification.get('subject', {}).get('title', 'No Title')
                url = notification.get('subject', {}).get('url', '#')
                self.menu.insert_before("Refresh",menu.MenuItem(f'{repo}: {title}', callback=lambda x, url=url, id=id: (
                    open_url(url, id) ,
                    self.update_notifications(sender)
                )
                ))
            self.menu.insert_before("Refresh", menu.SeparatorMenuItem())
            rumps.notification("Notibar", "New Notifications", f"You have {self.notification_count} new notifications.")
        else:
            self.title = f"📢"
        

    @rumps.clicked("Quit")
    def quit_app(self, sender):
        rumps.quit_application()

if __name__ == "__main__":
    app = NotibarApp()
    app.title = "📢"

    app.run()