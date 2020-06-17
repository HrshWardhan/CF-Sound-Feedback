# CF-Sound-Feedback
Gives audio feedback to your Submission Verdict on CodeForces.

## Initial Setup
* Run ```pip install -r req.txt``` to install required libraries.
* You may also need to install up ffmpeg separately. See install instructions [here](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up).
* Add Files "a.mp3" for corresponding to correct submission and "b.wav" for other verdicts to same directorty as audio.py. You may change these file names in audio.py at line 32 and 35 respectively.

## Using
Just run this script then input your username and this script will give audio feedback for all the submissions made on codeforces until it is terminated.
