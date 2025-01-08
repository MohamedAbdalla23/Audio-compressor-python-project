from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy as np

def plot_audio_signal(audio, title):
    # Convert the audio to a NumPy array
    samples = np.array(audio.get_array_of_samples())

    # Create a time axis in seconds
    time_axis = np.arange(0, len(samples)) / audio.frame_rate

    # Plot the audio signal
    plt.figure()
    plt.plot(time_axis, samples)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

def simple_compressor(input_file, output_file,
                      threshold_db=-30, attack_ms=1,
                      release_ms=200, ratio=4, makeup_gain_db=15):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Plot the original audio signal
    plot_audio_signal(audio, 'Original Audio Signal')

    # Apply compression
    compressed_audio = audio.compress_dynamic_range(
        threshold=threshold_db,
        attack=attack_ms,
        release=release_ms,
        ratio=ratio
    )

    # Plot the compressed audio signal
    plot_audio_signal(compressed_audio, 'Compressed Audio Signal')

    # Apply makeup gain
    compressed_audio += makeup_gain_db

    # Plot the final compressed audio signal
    plot_audio_signal(compressed_audio, 'Final Compressed Audio Signal')

    # Export the compressed audio
    compressed_audio.export(output_file, format="wav")

    # Play the compressed audio
    play(compressed_audio)

# Example usage
input_file = "looperman-l-5346995-0301554-hard-trap-drums-with-808.wav"
output_file = "output_compressed_audio.wav"
simple_compressor(input_file, output_file)