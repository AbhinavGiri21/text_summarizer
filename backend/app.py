from flask import Flask, request, jsonify
from flask_cors import CORS
from models.summarizer import summarize_text
from models.translator import translate_text
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary_type = data.get('type', 'medium')  # short, medium, or detailed
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    summary = summarize_text(text, summary_type)
    return jsonify({'summary': summary}), 200

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    target_language = data.get('language', 'en')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    translated_text = translate_text(text, target_language)
    return jsonify({'translated_text': translated_text}), 200

if __name__ == '__main__':
    app.run(debug=True)
