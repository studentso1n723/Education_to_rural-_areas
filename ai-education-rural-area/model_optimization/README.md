# AI for Education in Rural Areas

This project aims to build an AI-powered education platform that can work offline and provide multilingual support to rural communities. The system uses optimized AI models for edge devices and serves educational content in multiple languages.

## Components

1. **Model Optimization**: Optimizes TensorFlow models for offline use using Intel's OpenVINO toolkit.
2. **Multilingual Translation**: Translates educational content into multiple languages using Hugging Face's MarianMT.
3. **Flask Backend**: Serves translated educational content through a REST API.

## How to Run

1. **Model Optimization**:
   - Follow the instructions in `model_optimization/README.md` to convert the TensorFlow model to OpenVINO.
   
2. **Multilingual Translation**:
   - Install dependencies: `pip install -r multilingual_translation/requirements.txt`
   - Run the translation script: `python multilingual_translation/translate_model.py`
   
3. **Flask API**:
   - Install Flask: `pip install -r flask_backend/requirements.txt`
   - Start the Flask app: `python flask_backend/app.py`
