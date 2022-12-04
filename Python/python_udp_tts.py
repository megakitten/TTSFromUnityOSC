## Listens to OSC port for a string.
## On string receive, synthesize a
## sound file and play it.

##################################
##################################

## RUN: pip install playsound
## RUN: pip install python-osc
##      before running this script
import argparse
from operator import truediv
import random
import time
import math
import subprocess
from datetime import datetime
from playsound import playsound
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server


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
    client.send_message("/Progress", "Synthesizing")
    now = datetime.now()
    #fileName = "test_" + now.strftime("%m%d%Y_%H%M%S") + ".wav"

    #location = "C:/Users/CUB-PC/Documents/GitHub/TTSFromUnityOSC/Python/" ## uncomment for Install PC
    location = "C:/Users/megac/GitHub/TTSFromUnityOSC/Python/"

    fileName = "test_" + now.strftime("%m%d%Y_%H%M%S") + ".wav"
    speechModel = "tts_models/en/vctk/fast_pitch"
    #speechModel = "tts_models/en/ljspeech/speedy-speech"
    synthesize = "tts --text \"" + str(ttsString) + "\" --out_path " + location + fileName + " --model_name " + speechModel + " --speaker_idx \"VCTK_p271\""
    synthResult = run(synthesize)
    print(synthResult)
    print("Done Synthesizing.")
    client.send_message("/Progress", "Done Synthesizing.")
    try:
        print("Playing new sound file")
        client.send_message("/Progress", "Start Speaking")
        #playsound("C:/Users/megac/Github/test_10012022_151633.wav", True)  # blocking
        playsound(location+fileName, True)  # blocking
        client.send_message("/Progress", "Done Speaking")
        print("Done Speaking")
    except ValueError:
        pass
        client.send_message("/Progress", "Error Speaking")


if __name__ == "__main__":
#################
    # CLIENT PART    
    parser2 = argparse.ArgumentParser()
    parser2.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser2.add_argument("--port", type=int, default=8001,
                        help="The port the OSC server to listen to")
    args2 = parser2.parse_args()

    client = udp_client.SimpleUDPClient(args2.ip, args2.port)

#################
    # SERVER PART
    parser1 = argparse.ArgumentParser()
    parser1.add_argument("--ip", default="127.0.0.1", help="The ip to serve on")
    parser1.add_argument("--port", type=int, default=8000, help="The port to serve on")
    args1 = parser1.parse_args()

    dispatcher = Dispatcher()
    #dispatcher.map("/ai_text", tts_string_handler, "Synthesizing Speech...")
    dispatcher.map("/user_input", tts_string_handler, "Synthesizing Speech...")

    server = osc_server.ThreadingOSCUDPServer(
        (args1.ip, args1.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()






