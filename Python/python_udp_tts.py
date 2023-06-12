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
import simpleaudio as sa
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
    client.send_message("/Progress", "SynthStart")
    now = datetime.now()
    #fileName = "test_" + now.strftime("%m%d%Y_%H%M%S") + ".wav"

    location = "C:/Users/CUB-PC/Documents/GitHub/TTSFromUnityOSC/Python/" ## uncomment for Install PC
    #location = "C:/Users/megac/GitHub/TTSFromUnityOSC/Python/"

    fileName = "test_" + now.strftime("%m%d%y_%H%M%S") + ".wav"

    #speechModel = "tts_models/en/vctk/fast_pitch" + " --speaker_idx \"VCTK_p271\""
    #speechModel = "tts_models/en/vctk/vits" + " --speaker_idx \"p229\""  ## p225 - p 376
    #speechModel = "tts_models/en/vctk/vits" + " --speaker_idx \"p228\""  ## p225 - p 376
    speechModel = "tts_models/en/vctk/vits" + " --speaker_idx \"p227\"" ## p225 - p 376

    ### DONT USE THeSE ###
    # speechModel = "tts_models/en/ljspeech/speedy-speech"
    # speechModel = "tts_models/en/ljspeech/fast_pitch" # THIS HAS AN ISSUE WITH SOME UNICODE CHAR

    synthesize = "tts --text \"" + str(ttsString) + "\" --out_path " + location + fileName + " --model_name " + speechModel

    synthResult = run(synthesize)
    print(synthResult)
    print("Done Synthesizing.")
    client.send_message("/Progress", "SynthDone")

    try:
        print("Playing new sound file")
        client.send_message("/Progress", "Speaking")

        # PLAY AUDIO
        wave_obj = sa.WaveObject.from_wave_file(location+fileName)
        play_obj = wave_obj.play()
        play_obj.wait_done()

        client.send_message("/Progress", "SpeakingDone")
        print("Done Speaking")
    except ValueError:
        pass
        client.send_message("/Progress", "SpeechError")


if __name__ == "__main__":
#################
    # CLIENT PART    
    parser2 = argparse.ArgumentParser()
    parser2.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser2.add_argument("--port", type=int, default=8002,
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
    dispatcher.map("/user_input", tts_string_handler, "Synthesizing Speech...")
    dispatcher.map("/ai_response", tts_string_handler, "Synthesizing Speech...")

    server = osc_server.ThreadingOSCUDPServer(
        (args1.ip, args1.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()






