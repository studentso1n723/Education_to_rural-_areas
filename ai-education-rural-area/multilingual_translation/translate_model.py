from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-es'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(text, target_lang='es'):
    inputs = tokenizer.encode(text, return_tensors="pt")
    translated = model.generate(inputs, max_length=512)
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translation
