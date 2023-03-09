# additional requirements: pip install requests
import requests
import sys
import os
import time

# your waiting number
waiting_number = int(sys.argv[1])

# your specified buffer before the alarm
buffer = int(sys.argv[2])

alarm_number = waiting_number - buffer

# the interval of requesting the current waiting number in seconds
interval = int(sys.argv[3])

# your individual alarm sound
# download alarm sounds here for example: https://pixabay.com/de/sound-effects/search/alarme/
alarm_sound_file = sys.argv[4]

called_up = False
while not called_up:
    # fetch html data
    url = 'http://www2.tcs.ifi.lmu.de/~barths/stukoordination/wartenummer.html'
    print("Requesting the current number...", end='\r')
    r = requests.get(url)

    # extract current waiting number
    content = r.text
    current_number = int(content.split()[6][0:2])

    # play mp3 file when the alarm number is reached
    if alarm_number <= current_number:
        print('Congrats! Finally, it is your turn! :P')
        called_up = True
        os.system(alarm_sound_file)
    print('Patience dude! Current number: ' + str(current_number), end='\r')
    time.sleep(interval)
