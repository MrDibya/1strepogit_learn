import time
from plyer import  notification
if __name__== "__main__":
    while True:
        notification.notify(
            title= "**please drink water",
            message="make your body hydret its make you stay happy",
            app_icon="C:\\Users\\LENOVO\\Desktop\\icon.ico",
            timeout=5
        )
        time.sleep(5)