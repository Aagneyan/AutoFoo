import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
Un-comment this to check if it is reading the files correctly from the directory.
sample = "Sounds\Background\Backgroundbg0.wav"
data, sample_rate = librosa.load(sample)

plt.title("Waveform")
librosa.display.waveshow(data, sr=sample_rate)

plt.show()
for file_path in os.listdir("Sounds\Background"):
    print(file_path)
'''

audio_data = []

data_to_label_dictionary = {
    0: ["Sounds\Background" + '\\' + file_path for file_path in os.listdir("Sounds\Background")],
    1: ["Sounds\Positives" + '\\' + file_path for file_path in os.listdir("Sounds\Positives")]
}

for class_label, file_list in data_to_label_dictionary.items():
    for single_file in file_list:
        data, sample_rate = librosa.load(single_file)
        mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
        mfcc_proc = np.mean(mfccs.T, axis=0)
        audio_data.append([mfcc_proc, class_label])
    print("Preprocessed class label ",class_label)

df = pd.DataFrame(audio_data, columns=["features", "class_label"])
df.to_pickle("Audio_data_final.csv")

