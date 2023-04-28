import os
import sys
import glob
import subprocess
import soundfile as sf
import pyloudnorm as pyln

#target = -23 
files = glob.glob(os.path.join("audio", "demo", "**", "*.wav"), recursive=True)

for filename in files:

    #data, rate = sf.read(filename) # load audio (with shape (samples, channels))
    #data[:10*rate]
    #meter = pyln.Meter(rate) # create BS.1770 meter
    #loudness = meter.integrated_loudness(data) # measure loudness
    #adjustment = target - loudness
    #print(adjustment)
    adjustment = 0

    mp3outname = filename.replace(".wav",".mp3") 
    print(mp3outname)
    subprocess.call(["ffmpeg", "-hide_banner", "-loglevel", "panic", 
    "-y", "-ss", "0", "-t", "10",
    "-i", filename, "-filter:a", f"volume={adjustment}dB", "-q:a", "0", mp3outname])
    os.remove(filename)

    #sys.exit(0)