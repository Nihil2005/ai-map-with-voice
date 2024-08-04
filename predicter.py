import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('my_model.keras')

# Print a summary of the model architecture
model.summary()
