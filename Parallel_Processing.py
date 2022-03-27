import threading
import time
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from playsound import playsound
import sounddevice as sd
import main
from scipy.io.wavfile import write


##### CONSTANTS ################
fs = 22050
seconds = 3
sem = threading.Semaphore()
model = load_model("saved_models\Trigger.h5")

##### LISTENING THREAD #########
def listener():
    i = 0
    while True:
        i += 1
        print("Listening")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        write(str(i) + ".wav", fs, myrecording)
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction_thread(mfcc_processed)
        time.sleep(0.001)


def voice_thread():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()

def prediction(y):
    sem.acquire()
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.95:
        print("FOIND")

        # playsound('D:\AutoFoo\Sounds\initiated.wav')
        main.listen_to_request()
    time.sleep(0.1)

def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()

voice_thread()