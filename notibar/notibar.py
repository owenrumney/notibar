import rumps

from github.credentials import get_github_token, save_github_token
from github.notifications import get_github_notifications, mark_notification_as_done, mark_notification_as_read
import webbrowser


def open_url(url, notification_id):
    """
    Open a URL in the default web browser.
    """
    webbrowser.open(url)
    mark_notification_as_done(notification_id)

class NotibarApp(rumps.App):
    def __init__(self):
        super(NotibarApp, self).__init__("Notibar", quit_button=None)
        self.menu = ["Settings", "Quit"]
        self.notification_count = 0



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
                if item not in ['Settings', 'Quit']:
                    del self.menu[item]
                elif isinstance(item, rumps.MenuItem):
                    self.menu.remove(item)
        notifications = get_github_notifications()
        self.notification_count = len(notifications)
        if self.notification_count > 0:
            self.title = f"📢 ({self.notification_count})"
            menu = []
            for notification in notifications:
                id = notification.get('id')
                title = notification.get('subject', {}).get('title', 'No Title')
                url = notification.get('subject', {}).get('url', '#').replace("api.github.com/repos", "github.com")
                self.menu.insert_before("Settings",rumps.MenuItem(title, callback=lambda x, id=id: open_url(url, id)))
            menu.append(["---"])
            self.menu.insert_before("Settings", menu)
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