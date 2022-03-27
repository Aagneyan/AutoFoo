import sounddevice as sd
from scipy.io.wavfile import write


def background_recorder(location, file_count):
    input("To start recording background, press 'Enter' Once started please do not interrupt.")
    for i in range(file_count):
        fs = 44100
        seconds = 3
        print("Recording background ", i)
        rec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(location + str(i) + ".wav", fs, rec)


def positive_recorder(location, file_count):
    for i in range(file_count):
        input("To start recording background, press 'Enter'")
        fs = 44100
        seconds = 3
        print("Recording trigger word", i)
        rec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(location + "bg" + str(i) + ".wav", fs, rec)
        print("Successfully recorded ", i, " th trigger word sample")

background_recorder("D:\AutoFoo\Sounds\Background", 100)
# positive_recorder("D:\AutoFoo\Sounds\Positives", 100)
