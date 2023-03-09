# lmu-informatik-studiengangskoordinationssprechstunden-alarm

## Requirements

`pip install requests`

## Usage

Example usage checking for called number 22 (your waiting number is 24, you want a buffer of 2 positions, so the trigger number is 22) every 30 seconds triggering the playing of some-audio-file.mp3 if 22 is reached:

`python alarm.py 24 2 30 ".\some-audio-file.mp3"`

## Contribution

Feel free to use, share, extend and append this script to allow students to chill while waiting for their appointment.
