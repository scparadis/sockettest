import socket
import time
import os
import winsound

def check_for_internet():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except OSError:
        return False
lines_written = int()
while True: 
    lines_written += 1 
    if check_for_internet():
        print('Attempt',lines_written,': Internet is working')
        winsound.Beep(frequency=2000, duration=500)
        winsound.Beep(frequency=2000, duration=500)
        winsound.Beep(frequency=2000, duration=500)
    else:
        print('Attempt',lines_written,': The world is over!')
        winsound.Beep(frequency=440, duration=1500)
    time.sleep(3)
    if lines_written % 5 == 0:
        os.system('cls')
        #lines_written = 0