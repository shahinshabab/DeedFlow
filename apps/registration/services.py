from .models import RegistrationDraft


def create_or_update_registration_draft(document, structured_data):
    draft, _ = RegistrationDraft.objects.update_or_create(
        document=document,
        defaults={
            'structured_data': structured_data or {},
            'reviewed_data': structured_data or {},
            'is_reviewed': False,
        },
    )
    return draft
