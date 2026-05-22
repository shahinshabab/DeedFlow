ROLE_ADMIN = 'Admin'
ROLE_STAFF = 'Staff'

DOCUMENT_STATUS_UPLOADED = 'uploaded'
DOCUMENT_STATUS_EXTRACTED = 'extracted'
DOCUMENT_STATUS_AI_PROCESSED = 'ai_processed'
DOCUMENT_STATUS_REVIEWED = 'reviewed'
DOCUMENT_STATUS_COMPLETED = 'completed'
DOCUMENT_STATUS_FAILED = 'failed'

DOCUMENT_STATUS_CHOICES = [
    (DOCUMENT_STATUS_UPLOADED, 'Uploaded'),
    (DOCUMENT_STATUS_EXTRACTED, 'Extracted'),
    (DOCUMENT_STATUS_AI_PROCESSED, 'AI Processed'),
    (DOCUMENT_STATUS_REVIEWED, 'Reviewed'),
    (DOCUMENT_STATUS_COMPLETED, 'Completed'),
    (DOCUMENT_STATUS_FAILED, 'Failed'),
]

REGISTRATION_DOCUMENT_TYPES = [
    ('sale_deed', 'Sale Deed'),
    ('settlement_deed', 'Settlement Deed'),
    ('partition_deed', 'Partition Deed'),
    ('release_deed', 'Release Deed'),
    ('mortgage_deed', 'Mortgage Deed'),
    ('other', 'Other'),
]
