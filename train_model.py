import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam

# Load data
def load_data():
    data = np.load('data.npz')
    return data['X_train'], data['X_test'], data['y_train'], data['y_test']

X_train, X_test, y_train, y_test = load_data()

# Define model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(40, 32, 1)),  # Adjust input_shape to match your feature dimensions
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(np.unique(y_train)), activation='softmax')  # Number of classes should match the number of unique labels
])

model.compile(optimizer=Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model in Keras format
model.save('my_model.keras')
