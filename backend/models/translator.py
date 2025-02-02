from deep_translator import GoogleTranslator

def translate_text(text: str, target_language: str = 'en') -> str:
    if not text.strip():
        return "Error: No text provided for translation."

    try:
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        return f"Translation Error: {str(e)}"
