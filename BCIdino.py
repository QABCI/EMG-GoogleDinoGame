from pylsl import StreamInlet, resolve_stream
from pyautogui import keyDown
import os

def main():
    stream_type = "EMG" # init BCI connection
    print("looking for an", stream_type, "stream...")
    streams = resolve_stream('type', stream_type)
    print("Connecting to an", stream_type, "stream...")
    inlet = StreamInlet(streams[0])
    
    trigger = True # init setting
    threshold = 0.98
    value_length = 2
    count = 0
    # os.system("cls") # Clear debug data
    while True:
        valuelist = []
        while len(valuelist) < value_length: # detect the value twice to make sure the correction
            chunk, timestamps = inlet.pull_chunk()
            if timestamps:
                valuelist.append(chunk[0][1]) # collecting the data
            
        if sum(i >= threshold for i in valuelist) >= value_length / 2: # logic to jump
            if trigger:
                keyDown('space') # jump
                print("Jump ", count)
                count += 1
            trigger = not trigger
            
if __name__ == '__main__':
    main()