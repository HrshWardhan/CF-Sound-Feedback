import requests
import json
from pydub import AudioSegment
from pydub.playback import play
import time
import sys
import os

inputfilename = "input.txt"
file = open(inputfilename, "r")

username = file.readline().strip(" \n")
if(not username):
    print("Please enter your CF handle in first line in input.txt")
    sys.exit()
ac_file = file.readline().strip(" \n")
if(not os.path.isfile(ac_file)):
    print("Please enter correct name of AC sound file in second line in input.txt")
    sys.exit()
wa_file = file.readline().strip(" \n")
if(not os.path.isfile(wa_file)):
    print("Please enter correct name of WA sound file in third line in input.txt")
    sys.exit()
error_file = file.readline().strip(" \n")
if(not os.path.isfile(error_file)):
    print("Please enter correct name of script error sound file in fourth line in input.txt")
    sys.exit()

url = "https://codeforces.com/api/user.status"
parameters = {"handle": username, "from":1, "count":1}

lastid = ""
lasterr = False

def sound(voice):
  song = AudioSegment.from_mp3(voice)
  play(song)
def ac():
  sound(ac_file)
def wa():
  sound(wa_file)
def error():
  global lasterr
  if lasterr == False:
    sound(error_file)
  lasterr = True

print("Script started...")
while True:
  try:
    response = ""
    response = requests.get(url, params=parameters, timeout=1)
    if lasterr:
        print("Connection Successful")
  except:
    error()
    print("Connection Error Retrying....")
    time.sleep(1)
    continue
  lasterr = False
  if response.status_code != 200:
    print("ERROR: status code - ", response.status_code)
    error()
    try:
      print(response.content)
    except:
      pass
    break
  else:
    lasterr = False
    body = response.json()["result"][0]
    sub_id = body["id"]
    if lastid == "":
      lastid = sub_id
    verdict = "TESTING"
    if "verdict" in body:
      verdict = body["verdict"]
    if sub_id != lastid and verdict != "TESTING":
      lastid = sub_id
      if verdict == "OK":
        ac()
      else:
        wa()
  time.sleep(1)