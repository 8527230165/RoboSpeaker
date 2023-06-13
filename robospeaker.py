import os

""" import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, world!")

engine.runAndWait() """

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, world!")

