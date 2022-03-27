'''from tensorflow.python.client import device_lib
import tensorflow


def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    print(x.name for x in local_device_protos if x.device_type == 'GPU')


model = tensorflow.keras.Sequential()
get_available_gpus()'''

import pip

def install_whl(path):
    pip.main(['install', path])

install_whl("D:/PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
