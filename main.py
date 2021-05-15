# Author: YOSHI BANSAL
# Date: 15/05/2021 Saturday

import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink Water!!",
            message="Benefits of drinking water \n"  
                        "carrying nutrients and oxygen to your cells. \n", #max length of message -> 256
            app_icon="icon.ico",
            timeout=20 #in seconds
        )
        time.sleep(60*60) #seconds #60*60 = 1hour

        #venv\Scripts\activate
        #run using
            #python main.py
        #to run in background
            #pythonw.exe ./main.py
                # or
            #pythonw ./main.py

        #go to settings/notifications & actions and turn on 'GET NOTIFICATION FROM APPS AND OTHER SENDERS'
