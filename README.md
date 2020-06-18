# CF-Sound-Feedback
Gives audio feedback to your Submission Verdict on CodeForces.

## Initial Setup
Follow these instructions before using the script for the first time.

* Clone this repo or download ZIP
* Run ```pip install -r req.txt``` to install required libraries.
* You may also need to install up ffmpeg separately. See install instructions [here](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up).
* Add three audio files corresponding to AC, for other verdicts, and for when script gets an error to same directorty as audio.py.
* In ```input.txt``` write your userhandle in first line, file name for AC audio file in second line, for other verdicts audio file in third line and for errors in fourth line.
Example for ```input.txt``` :
```
my_handle
correct.mp3
wrong.mp3
error.mp3
```

## Using
Just run this script and this script will give audio feedback for all your further submissions made on codeforces until it is terminated.
