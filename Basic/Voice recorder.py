import tkinter as tk
from tkinter import *
import recorder

def start():
    global running

    if running is not None:
        print("Already running")
    else:
        running = recorder.open("untitled.flac", "wb")
        running.start_recording()
        Label(window, text="Recording has started").pack()


def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running = None
        Label(window, text="Recording has stopped").pack()
    else:
        print("Not running")


window = Tk()
window.geometry("700x300")
window.title("TechVidvan")
Label(window, text="Click on Start To Start Recording", font=("bold", 20)).pack()
Button(window, text="Start", bg="green", command=start, font=("bold", 20)).pack()
Button(window, text="Stop", bg="green", command=stop, font=("bold", 20)).pack()

window.mainloop()