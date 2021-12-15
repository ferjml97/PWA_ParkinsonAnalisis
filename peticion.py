
# import sounddevice as sd
# from scipy.io.wavfile import write
import requests

'''
fs = 44100  # Sample rate
seconds = 30  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 

# Load the file to send
dato = open("./output.wav", 'rb')
print(dato)
files = {'audio': open("output.wav", 'rb')}
'''
files = {'audio': open("output.wav", 'rb')}
# Send the HTTP request and get the reply
reply = requests.post("https://morning-brushlands-40885.herokuapp.com/features_extract", files=files)
#reply = requests.post("http://127.0.0.1:5000/features_extract", files=files)
print(reply)
print(reply.text)