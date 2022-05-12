import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please take a short Break, drink some water.",
            message = "It's best to take a break every 90 minutes(Based on Pozen).",
            app_icon = 'clipboard.ico',
            timeout =10
            )
        time.sleep(5400)