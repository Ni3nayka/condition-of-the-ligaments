import parselmouth

#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import glob
#import numpy as np
#import pandas as pd
#import parselmouth 
#import statistics

from parselmouth.praat import call
#from scipy.stats.mstats import zscore
#from sklearn.decomposition import PCA
#from sklearn.preprocessing import StandardScaler

import datetime

from pydub import AudioSegment

# https://python-scripts.com/datetime-time-python
def get_data():
    return str(datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S"))

# https://www.codespeedy.com/how-to-cut-a-particular-portion-of-an-mp3-file-in-python/
def cut_audio(path,start_milisec,end_milisec):
    sound = AudioSegment.from_wav(path)
    extract = sound[start_milisec:end_milisec]
    new_path = path[0:-4] + "___operating___" + get_data() + ".wav"
    extract.export(new_path, format="wav")
    return new_path

# https://github.com/YannickJadoul/Parselmouth
def view_audio(path):
    sns.set() # Use seaborn's default style to make attractive graphs   

    # Plot nice figures using Python's "standard" matplotlib library
    snd = parselmouth.Sound(path)
    #snd = parselmouth.Sound(cut_audio(path,6000,21000))
    plt.figure()
    plt.plot(snd.xs(), snd.values.T)
    plt.xlim([snd.xmin, snd.xmax])
    print([snd.xmin, snd.xmax])
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")

# https://github.com/drfeinberg/PraatScripts/blob/master/Measure%20Pitch%2C%20HNR%2C%20Jitter%2C%20Shimmer%2C%20and%20Formants.ipynb
def measurePitch(voiceID, start_milisec=None,end_milisec=None, f0min=75, f0max=300): # , unit
    sound = parselmouth.Sound(voiceID) # read the sound
    if start_milisec==None or start_milisec<sound.xmin*1000: start_milisec = sound.xmin*1000
    if end_milisec==None or end_milisec>sound.xmax*1000: end_milisec = sound.xmax*1000
    sound = parselmouth.Sound(cut_audio(voiceID,start_milisec,end_milisec)) # REread the sound

    duration = call(sound, "Get total duration") # duration
    pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    #meanF0 = call(pitch, "Get mean", 0, 0, unit) # get mean pitch
    #stdevF0 = call(pitch, "Get standard deviation", 0 ,0, unit) # get standard deviation
    harmonicity = call(sound, "To Harmonicity (cc)", 0.01, f0min, 0.1, 1.0)
    hnr = call(harmonicity, "Get mean", 0, 0)
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    localabsoluteJitter = call(pointProcess, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
    rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    ppq5Jitter = call(pointProcess, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
    ddpJitter = call(pointProcess, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
    localShimmer =  call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    localdbShimmer = call([sound, pointProcess], "Get shimmer (local_dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    aqpq5Shimmer = call([sound, pointProcess], "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq11Shimmer =  call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    ddaShimmer = call([sound, pointProcess], "Get shimmer (dda)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

    print(sound,
          duration,
          pitch,
          harmonicity,
          hnr,
          pointProcess,
          localJitter,
          localabsoluteJitter,
          rapJitter,
          ppq5Jitter,
          ddpJitter,
          localShimmer,
          localdbShimmer,
          apq3Shimmer,
          aqpq5Shimmer,
          apq11Shimmer,
          ddaShimmer)

    file = open("test_"+get_data()+".txt", 'w')
    file.write("duration:\n")
    file.write(str(duration))
    file.write("\n\n\npitch:\n")
    file.write(str(pitch))
    file.write("\n\n\nharmonicity:\n")
    file.write(str(harmonicity))
    file.write("\n\n\nhnr:\n")
    file.write(str(hnr))
    file.write("\n\n\npointProcess:\n")
    file.write(str(pointProcess))
    file.write("\n\n\nlocalJitter:\n")
    file.write(str(localJitter))
    file.write("\n\n\nlocalabsoluteJitter:\n")
    file.write(str(localabsoluteJitter))
    file.write("\n\n\nrapJitter:\n")
    file.write(str(rapJitter))
    file.write("\n\n\nppq5Jitter:\n")
    file.write(str(ppq5Jitter))
    file.write("\n\n\nddpJitter:\n")
    file.write(str(ddpJitter))
    file.write("\n\n\nlocalShimmer:\n")
    file.write(str(localShimmer))
    file.write("\n\n\nlocaldbShimmer:\n")
    file.write(str(localdbShimmer))
    file.write("\n\n\napq3Shimmer:\n")
    file.write(str(apq3Shimmer))
    file.write("\n\n\naqpq5Shimmer:\n")
    file.write(str(aqpq5Shimmer))
    file.write("\n\n\napq11Shimmer:\n")
    file.write(str(apq11Shimmer))
    file.write("\n\n\nddaShimmer:\n")
    file.write(str(ddaShimmer))
    file.close()
    
    

if __name__=="__main__":
    path = "D:/GitHub/_cache/condition-of-the-ligaments/src/test/Соловьева_НВ_1977_14_06_2022_185051_GX010425.wav"
    view_audio(path)
    measurePitch(path)