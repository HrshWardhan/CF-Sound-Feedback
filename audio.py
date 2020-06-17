from bs4 import BeautifulSoup
import requests
import urllib
import os
from os.path import basename
import sys
import time
from pydub import AudioSegment
from pydub.playback import play
print(" Enter your CodeForces Username")
usrnm = input()
lst = ""
f = False
while True:
    url = "https://codeforces.com/submissions/"+usrnm;
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    table = soup.find("table", { "class" : "status-frame-datatable" })
    row = table.findAll("tr")[1]
    cell = row.findAll("td")[0]
    sub_num  = cell.find( "a" , { "class" : "view-source" } )['submissionid']
    if lst == "":
        lst = sub_num
    if sub_num != lst:
        f = True
        lst = sub_num
    if f and (row.findAll("td")[5])['waiting'] == "false":
        verdict =  (row.findAll("td")[5]).find( "span" , { "class" : "submissionVerdictWrapper" })['submissionverdict']
        f = False
        print(verdict)
        if verdict == "OK":
            song = AudioSegment.from_mp3("a.mp3")
            play(song)
        else :
            song = AudioSegment.from_mp3("b.wav")
            play(song)
    time.sleep(1)