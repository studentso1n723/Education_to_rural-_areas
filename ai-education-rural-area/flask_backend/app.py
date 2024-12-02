from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

model_name = 'Helsinki-NLP/opus-mt-en-es'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(text, target_lang='es'):
    inputs = tokenizer.encode(text, return_tensors="pt")
    translated = model.generate(inputs, max_length=512)
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translation

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text", "")
    target_lang = data.get("target_lang", "es")
    
    if text:
        translated_text = translate_text(text, target_lang)
        return jsonify({"original_text": text, "translated_text": translated_text})
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
