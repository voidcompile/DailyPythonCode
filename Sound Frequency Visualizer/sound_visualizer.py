import numpy as np
import matplotlib.pyplot as plt

# Optional: play sound
try:
    import sounddevice as sd
    HAS_SOUND = True
except ImportError:
    HAS_SOUND = False


def generate_sine_wave(freq, duration, amplitude=1.0, sample_rate=44100):
    """
    Generate a sine wave with given frequency, duration, and amplitude.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return t, wave


def main():
    print("🎵 Sound Frequency Visualizer 🎵")
    
    try:
        freq = float(input("Enter frequency in Hz (e.g., 440): "))
        duration = float(input("Enter duration in seconds (e.g., 2): "))
        amplitude = float(input("Enter amplitude (0.1 to 1.0): "))
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
        return

    # Generate waveform
    t, wave = generate_sine_wave(freq, duration, amplitude)

    # Plot waveform
    plt.figure(figsize=(10, 4))
    plt.plot(t[:1000], wave[:1000])  # show only first 1000 samples for clarity
    plt.title(f"Sine Wave: {freq} Hz")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    # Play sound if sounddevice is available
    if HAS_SOUND:
        print("🔊 Playing sound...")
        sd.play(wave, 44100)
        sd.wait()
    else:
        print("⚠️ sounddevice not installed. Only showing the graph.")


if __name__ == "__main__":
    main()
