import re


def clean_extracted_text(text):
    """Light cleaning only. Keep Malayalam text unchanged as much as possible."""
    if not text:
        return ''
    text = text.replace('\x00', '')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
