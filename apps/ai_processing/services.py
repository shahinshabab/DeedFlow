import json
from django.conf import settings
from openai import OpenAI
from .models import AIProcessingLog
from .prompts import SYSTEM_PROMPT, build_registration_extraction_prompt
from .schema import REGISTRATION_SCHEMA, EMPTY_REGISTRATION_DATA
from .validators import normalize_registration_data


def _fallback_structured_data():
    data = EMPTY_REGISTRATION_DATA.copy()
    data['notes'] = 'OPENAI_API_KEY is not set. This is fallback demo data. Edit manually.'
    return data


def process_document_with_ai(document, extracted_text):
    if not settings.OPENAI_API_KEY:
        data = _fallback_structured_data()
        return AIProcessingLog.objects.create(
            document=document,
            model_name='fallback',
            structured_data=data,
            raw_response=json.dumps(data, ensure_ascii=False),
            success=True,
        )

    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    prompt = build_registration_extraction_prompt(extracted_text)

    try:
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': prompt},
            ],
            text={
                'format': {
                    'type': 'json_schema',
                    'name': 'kerala_registration_draft',
                    'schema': REGISTRATION_SCHEMA,
                    'strict': True,
                }
            },
        )
        raw_text = response.output_text
        data = normalize_registration_data(json.loads(raw_text))
        return AIProcessingLog.objects.create(
            document=document,
            model_name=settings.OPENAI_MODEL,
            structured_data=data,
            raw_response=raw_text,
            success=True,
        )
    except Exception as exc:
        return AIProcessingLog.objects.create(
            document=document,
            model_name=settings.OPENAI_MODEL,
            structured_data={},
            raw_response='',
            success=False,
            error_message=str(exc),
        )
