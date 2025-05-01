import rumps

from github.credentials import get_github_token, save_github_token
from github.notifications import get_github_notifications


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
        notifications = get_github_notifications()
        self.notification_count = len(notifications)
        if self.notification_count > 0:
            self.title = f"📢 ({self.notification_count})"
            menu = []
            for notification in notifications:
                title = notification.get('subject', {}).get('title', 'No Title')
                menu.append(title)
            menu.append(["---", 'Settings', "Quit"])
            self.menu = menu
            rumps.notification("Notibar", "New Notifications", f"You have {self.notification_count} new notifications.")
        else:
            self.title = f"📢"
        

    @rumps.clicked("Quit")
    def quit_app(self, sender):
        rumps.quit_application()

if __name__ == "__main__":
    app = NotibarApp()
    app.title = "📢"
    app.update_notifications(None)  # Initial check for notifications
    app.run()