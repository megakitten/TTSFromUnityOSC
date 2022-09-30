"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time
import math

from pythonosc import osc_message_builder
from pythonosc import udp_client

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

def tts_string_handler(unused_addr, args, ttsString):
    client.send_message("/isDone", "True")
    #print("[{0}] ~ {1}".format(args[0], ttsString))
    #"""
    try:
        print("[{0}] ~ {1}".format(args[0], ttsString))
    except ValueError:
        pass
    #"""

if __name__ == "__main__":
#################
    # CLIENT PART    
    parser2 = argparse.ArgumentParser()
    parser2.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser2.add_argument("--port", type=int, default=7400,
                        help="The port the OSC server is listening on")
    args2 = parser2.parse_args()

    client = udp_client.SimpleUDPClient(args2.ip, args2.port)

#################
    # SERVER PART

    parser1 = argparse.ArgumentParser()
    parser1.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser1.add_argument("--port",
                        type=int, default=5005, help="The port to listen on")
    args1 = parser1.parse_args()

    dispatcher = Dispatcher()
    dispatcher.map("/tts", tts_string_handler, "String to synthesize")

    server = osc_server.ThreadingOSCUDPServer(
        (args1.ip, args1.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()






