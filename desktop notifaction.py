import time
from plyer import notification

while True:
    notification.notify(
        title="💡 Stay Hydrated!",
        message="Drink a glass of water.",
        timeout=5
    )
    time.sleep(36)  # wait 1 hour
