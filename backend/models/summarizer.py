from transformers import pipeline

# Load the model (can be cached locally for efficiency)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, summary_type='medium'):
    # Set length parameters based on summary type
    if summary_type == 'short':
        min_length, max_length = 50, 100
    elif summary_type == 'detailed':
        min_length, max_length = 250, 350
    else:  # medium
        min_length, max_length = 100, 150
    
    # Generate summary
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']
