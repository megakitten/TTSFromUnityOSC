# TTSFromUnityOSC
 send string from unity over OSC to Python for TTS 

Only tested on Windows 10 machine with NVIDIA RTX 2070 Super (requires use of CUDA)


TO DO:

Include instructions on how to install Coqui locally

Unity project with OSC publisher to send string to Python

Async Python Script to receive OSC (just print received string)

Unity script to take keyboard input and send string on "Enter" over OSC

Put tts-server call inside of async function.
--> synthesizes string when received (plays on System)
