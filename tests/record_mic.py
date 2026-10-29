import serial
import wave
import time

# CHANGE THIS TO YOUR ESP32 PORT
PORT = 'COM5' 
BAUD = 921600
RECORD_SECONDS = 5

try:
    ser = serial.Serial(PORT, BAUD)
except Exception as e:
    print(f"Error connecting: {e}\nDid you close the Arduino Serial Monitor?")
    exit()

print(f"Listening to ESP32... Recording {RECORD_SECONDS} seconds of audio.")

frames = bytearray()
bytes_to_read = 16000 * 2 * RECORD_SECONDS 

# Flush old data to ensure we start at the beginning of an audio frame
ser.reset_input_buffer() 

while len(frames) < bytes_to_read:
    frames.extend(ser.read(2048))

ser.close()

print("Recording complete. Saving to test_mic.wav...")

with wave.open("test_mic.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2) # 16-bit
    wf.setframerate(16000)
    wf.writeframes(frames)
    
print("Saved! You can now play test_mic.wav on your computer.")