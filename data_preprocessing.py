import numpy as np
import librosa
import os
from sklearn.model_selection import train_test_split

# Constants
SAMPLE_RATE = 16000
DURATION = 1  # seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

def load_audio_files(dataset_path):
    labels = []
    features = []

    for label_dir in os.listdir(dataset_path):
        label_path = os.path.join(dataset_path, label_dir)
        if os.path.isdir(label_path):
            for file_name in os.listdir(label_path):
                file_path = os.path.join(label_path, file_name)
                audio, sr = librosa.load(file_path, sr=SAMPLE_RATE)
                if len(audio) < SAMPLES_PER_TRACK:
                    # Pad with zeros if audio is shorter
                    audio = np.pad(audio, (0, SAMPLES_PER_TRACK - len(audio)), 'constant')
                else:
                    # Truncate if audio is longer
                    audio = audio[:SAMPLES_PER_TRACK]
                mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
                mfccs = np.expand_dims(mfccs, axis=-1)
                features.append(mfccs)
                labels.append(label_dir)

    return np.array(features), np.array(labels)

def preprocess_data(features, labels):
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, label_encoder

def save_data(X_train, X_test, y_train, y_test):
    np.savez('data.npz', X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

def load_data():
    data = np.load('data.npz')
    return data['X_train'], data['X_test'], data['y_train'], data['y_test']

if __name__ == "__main__":
    dataset_path = 'sample_dataset'
    features, labels = load_audio_files(dataset_path)
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(features, labels)
    save_data(X_train, X_test, y_train, y_test)
