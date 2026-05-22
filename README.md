# DeedFlow Starter

Phase-1 Django MVP for Kerala document registration automation.

Current apps included:
- core: shared helpers, mixins, constants
- accounts: login/logout/dashboard/profile
- documents: PDF upload and process pipeline trigger
- extraction: PDF text extraction
- ai_processing: extracted text to structured JSON
- registration: editable reviewed registration draft

Future apps are intentionally not created yet:
- calculations, estamp, filing_sheet, automation, workflow, notifications, reports, api, realtime

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Main flow

1. Login
2. Upload PDF
3. Click Process
4. Extract text using pdfplumber
5. Structure data using AI if OPENAI_API_KEY is set, otherwise fallback demo JSON
6. Review/edit final registration draft
