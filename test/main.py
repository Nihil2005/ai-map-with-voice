import numpy as np
import tensorflow as tf
import librosa

# Load the model
MODEL_PATH = r'C:\Users\nihil\OneDrive\Desktop\ISRO\my_model.keras'
model = tf.keras.models.load_model(MODEL_PATH)

# Define commands if you have them
COMMANDS = ['zoom in', 'zoom out', 'show roads', 'hide satellite']

def preprocess_audio(file_path):
    """Preprocess audio file for prediction."""
    audio, sr = librosa.load(file_path, sr=16000)  # Adjust sample rate as needed
    audio = librosa.util.fix_length(audio, 16000)  # Ensure audio length is consistent
    audio = np.expand_dims(audio, axis=-1)  # Add channel dimension
    audio = np.expand_dims(audio, axis=0)   # Add batch dimension
    return audio

def predict_command(file_path):
    """Predict the command from an audio file."""
    audio = preprocess_audio(file_path)
    prediction = model.predict(audio)
    command_index = np.argmax(prediction)
    return COMMANDS[command_index]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python predict.py <path_to_audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    command = predict_command(audio_file)
    print(f"Predicted command: {command}")
