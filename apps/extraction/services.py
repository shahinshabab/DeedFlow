from .models import ExtractedText
from .pdf_extractor import extract_text_from_pdf
from .malayalam_cleaner import clean_extracted_text


def create_extracted_text_for_document(document):
    raw_text, page_count = extract_text_from_pdf(document.file.path)
    cleaned = clean_extracted_text(raw_text)
    extracted, _ = ExtractedText.objects.update_or_create(
        document=document,
        defaults={
            'raw_text': raw_text,
            'cleaned_text': cleaned,
            'page_count': page_count,
        },
    )
    return extracted
