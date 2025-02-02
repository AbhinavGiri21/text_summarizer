from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, summary_type: str = 'medium') -> str:
    if not text.strip():
        return "Error: No text provided for summarization."

    summary_length = {
        'short': (50, 100),
        'detailed': (250, 350),
        'medium': (100, 150)
    }

    min_length, max_length = summary_length.get(summary_type, (100, 150))
    
    word_count = len(text.split())

    if word_count < 50:
        return "Error: Text too short to summarize. Provide at least 50 words."

    max_length = min(max_length, word_count)

    try:
        summary_output = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
        
        if not summary_output:
            return "Error: Summarization failed. No output generated."

        return summary_output[0].get('summary_text', "Error: Unable to extract summary.")

    except Exception as e:
        return f"Summarization Error: {str(e)}"
