import pyaudio
import numpy

BITRATE = 96000                                     # change to 44100 if performance issues
def sinOsc(frequency, duration, amplitude=.5):      # 50% volume
    nframes = duration * BITRATE
    frames = numpy.arange(nframes)
    frame_frequency = frequency / BITRATE
    val = amplitude * numpy.sin(frames * frame_frequency * 2.0 * numpy.pi)
    return val.astype(dtype=numpy.float32)

def main():
    """ Generates binaural audio on your headphones """

    print("'AUDIOPHILE' BINAURAL BEATS (PURE SINUS WAVES)")
    print()
    print("\t[OPTIONS] Select which beat you would like to hear:")
    print()
    print("\t[1]\tDelta Waves (0.1 to 4HZ)")
    print("\t\t\tPromotes sleep state")
    print("\t[2]\tTheta Waves (4 to 7HZ)")
    print("\t\t\tImproves meditation, creativity, and sleep")
    print("\t[3]\tAlpha Waves (7 to 13HZ)")
    print("\t\t\tEncourages relaxation and focus")
    print("\t[4]\tBeta Waves (13 to 30HZ)")
    print("\t\t\tHelps promote concentration and alertness.")
    print("\t\t\tMay increase anxiety at the higher end of the range.")

    print()
    wave_type = input("Enter the number you would like to hear:")
    print()

    # load audio option
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paFloat32, channels=2, rate=BITRATE, output=True)
    if wave_type == "1":
        print("[DELTA] 2HZ waves, sweet dreams ...")
        signal_left = sinOsc(frequency=60.0, duration=500.0)
        signal_right = sinOsc(frequency=62.0, duration=500.0)
    if wave_type == "2":
        print("[THETA] 4HZ waves, wind down ...")
        signal_left = sinOsc(frequency=70.0, duration=500.0)
        signal_right = sinOsc(frequency=74.0, duration=500.0)
    if wave_type == "3":
        print("[ALPHA] 8HZ waves, enjoy the calm ...")
        signal_left = sinOsc(frequency=70.0, duration=500.0)
        signal_right = sinOsc(frequency=78.0, duration=500.0)
    if wave_type == "4":
        print("[BETA] 20HZ waves, go have fun ...")
        signal_left = sinOsc(frequency=100.0, duration=500.0)
        signal_right = sinOsc(frequency=120.0, duration=500.0)


    # play binaural audio
    stereo_signal = numpy.ravel(numpy.column_stack((signal_left, signal_right)))
    stream.write(stereo_signal.tobytes())
    stream.stop_stream()
    stream.close()
    pa.terminate()


if __name__ == "__main__":
    main()