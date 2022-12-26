import os
import logging
from scipy.io.wavfile import write
from spleeter.audio.adapter import AudioAdapter
from spleeter.separator import Separator

class Spleeter:
    separator = Separator("spleeter:2stems")
    audio_loader = AudioAdapter.default()
    __sample_rate = 44_100

    @classmethod
    def __get_vocals(cls, audio_path: str):
        """Return None if there is no sound in the video file, else, return only the vocals."""
        try:
            # Get the original sound
            waveform, _ = cls.audio_loader.load(path=audio_path, sample_rate=cls.__sample_rate)
        except StopIteration:
            logging.info(f"The file {audio_path} does not seem to contain any sound.")
            return None
        else:
            # Perform the separation
            prediction = cls.separator.separate(waveform=waveform)
            # Get vocals
            return prediction["vocals"] # return a np.ndarray

    @classmethod
    def remove_music(cls, audio_path: str, output_path: str, remove_original: bool = True) -> None:
        """
        Remove the music from an audio and save the vocals in the output_path in WAV format.

        TODO: check if WAV files are supported for "audio_path"
        audio_path: path of the MP3 file
        output_path: complete path for the WAV output file
        """
        if not os.path.exists(audio_path):
            return

        if (vocals := cls.__get_vocals(audio_path=audio_path)) is None:
            raise ValueError(f"Cannot get vocals from: {audio_path}")
        # Save the waveform in a ".wav" file
        write(filename=output_path, rate=cls.__sample_rate, data=vocals)
        if remove_original and audio_path != output_path:
            os.remove(audio_path)
