from plyer import notification
import time

from plyer import notification
import time

def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "pythonlogo.ico",
        timeout = 10,
    )

while True:
    app_name= "Desktop Notifier"
    title = "This is a Desktop notifier app!"
    notify_me(app_name, title)
    # notify_me("Desktop Notifier", "This is a Desktop notifier app")
    time.sleep(10)  # wait for 10 seconds before sending the next notification
