from flask import Flask, request, jsonify
from flask_cors import CORS
from models.summarizer import summarize_text
from models.translator import translate_text

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary_type = data.get('type', 'medium')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    summary = summarize_text(text, summary_type)
    if summary.startswith("Error"):
        return jsonify({'error': summary}), 400

    return jsonify({'summary': summary}), 200

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    target_language = data.get('language', 'en')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    translated_text = translate_text(text, target_language)
    if translated_text.startswith("Error"):
        return jsonify({'error': translated_text}), 400

    return jsonify({'translated_text': translated_text}), 200

if __name__ == '__main__':
    app.run(debug=True)
