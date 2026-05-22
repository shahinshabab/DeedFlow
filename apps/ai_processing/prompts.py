SYSTEM_PROMPT = """
You are an assistant that extracts structured data from Kerala document registration PDFs.
Return only data that is present or strongly implied in the document.
The website UI is English, but the document content may contain Malayalam.
Keep Malayalam names, places, and descriptions as they appear when possible.
Use empty strings for missing scalar values and empty arrays for missing lists.
""".strip()


def build_registration_extraction_prompt(extracted_text):
    return f"""
Extract registration draft data from this PDF text.

PDF TEXT:
{extracted_text[:30000]}
""".strip()
