## Listens to OSC port for a string.
## On string receive, synthesize a
## sound file and play it. 
## Send 

## -- mvpvh (Paulus)
##    with borrowed code from:
##      -->
##      -->
##      -->
##      -->

##################################
##################################

## RUN: pip install playsound
##      before running this script

import argparse
from operator import truediv
import random
import time
import math

import subprocess

from datetime import datetime

from pythonosc import osc_message_builder
from pythonosc import udp_client

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

from playsound import playsound

# for running the tts code
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def tts_string_handler(unused_addr, args, ttsString):
    try:
        print("[{0}] ~ {1}".format(args[0], ttsString))
    except ValueError:
        pass
    print("Starting Synthesizer")
    client.send_message("/Synthesizing", "True")
    now = datetime.now()
    fileName = "test_" + now.strftime("%m%d%Y_%H%M%S") + ".wav"
    synthesize = "tts --text \"" + ttsString + ".\" --out_path " + fileName
    synthResult = run(synthesize)
    print("Done Synthesizing")
    client.send_message("/DoneSynthesizing", "True")

    # TO DO : add a check that the file is there 
    print("Playing new sound file")
    playsound(fileName, True) # blocking

    client.send_message("/DoneSpeaking", "True")

if __name__ == "__main__":
#################
    # CLIENT PART    
    parser2 = argparse.ArgumentParser()
    parser2.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser2.add_argument("--port", type=int, default=7500,
                        help="The port the OSC server is listening on")
    args2 = parser2.parse_args()

    client = udp_client.SimpleUDPClient(args2.ip, args2.port)

#################
    # SERVER PART
    parser1 = argparse.ArgumentParser()
    parser1.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
    parser1.add_argument("--port", type=int, default=7501, help="The port to listen on")
    args1 = parser1.parse_args()

    dispatcher = Dispatcher()
    dispatcher.map("/tts", tts_string_handler, "Synthesizing speech...")

    server = osc_server.ThreadingOSCUDPServer(
        (args1.ip, args1.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()






