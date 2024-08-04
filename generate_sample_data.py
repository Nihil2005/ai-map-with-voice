from gtts import gTTS
import os

# Constants
DURATION = 1  # seconds
COMMANDS = ['zoom in', 'zoom out', 'show roads', 'hide satellite']
DATASET_PATH = 'sample_dataset'

def create_audio(command, filename):
    """ Create a TTS audio file for each command """
    tts = gTTS(text=command, lang='en')
    tts.save(filename)

def generate_dataset():
    """ Generate dataset of sample audio files """
    if not os.path.exists(DATASET_PATH):
        os.makedirs(DATASET_PATH)

    for command in COMMANDS:
        command_path = os.path.join(DATASET_PATH, command)
        if not os.path.exists(command_path):
            os.makedirs(command_path)

        for i in range(10):  # Create 10 samples per command
            filename = os.path.join(command_path, f'{command}_{i}.wav')
            create_audio(command, filename)

if __name__ == "__main__":
    generate_dataset()
