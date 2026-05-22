from django.db import transaction
from apps.core.constants import DOCUMENT_STATUS_EXTRACTED, DOCUMENT_STATUS_AI_PROCESSED, DOCUMENT_STATUS_FAILED
from apps.extraction.services import create_extracted_text_for_document
from apps.ai_processing.services import process_document_with_ai
from apps.registration.services import create_or_update_registration_draft


@transaction.atomic
def process_uploaded_document(document):
    """Phase-1 pipeline: PDF → text → AI JSON → registration draft."""
    try:
        extracted = create_extracted_text_for_document(document)
        document.status = DOCUMENT_STATUS_EXTRACTED
        document.error_message = ''
        document.save(update_fields=['status', 'error_message', 'updated_at'])

        ai_result = process_document_with_ai(document, extracted.raw_text)
        document.status = DOCUMENT_STATUS_AI_PROCESSED
        document.save(update_fields=['status', 'updated_at'])

        draft = create_or_update_registration_draft(document, ai_result.structured_data)
        return draft
    except Exception as exc:
        document.status = DOCUMENT_STATUS_FAILED
        document.error_message = str(exc)
        document.save(update_fields=['status', 'error_message', 'updated_at'])
        raise
