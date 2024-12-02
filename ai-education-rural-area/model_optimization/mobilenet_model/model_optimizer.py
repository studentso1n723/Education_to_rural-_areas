import tensorflow as tf
from openvino.inference_engine import IECore

# Load the TensorFlow model
model = tf.keras.applications.MobileNetV2(weights='imagenet')
model.save("mobilenet_model")

# Convert to OpenVINO IR (run in command line using Model Optimizer)
# mo --input_model mobilenet_model/saved_model.pb --framework tensorflow --output_dir optimized_model
