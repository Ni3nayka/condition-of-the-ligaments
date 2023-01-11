from praat import view_audio, measurePitch
from graphics import graphics

if __name__=="__main__":

    def comanda_start(path,mode,start_audio=None,end_audio=None):
        if mode=="view": view_audio(path)
        else: measurePitch(path,start_milisec=start_audio,end_milisec=end_audio)

    window = graphics("Poulina project v1.0",comanda_start=comanda_start)
    window.loop()