import pdfplumber


def extract_text_from_pdf(file_path):
    pages_text = []
    with pdfplumber.open(file_path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ''
            if text.strip():
                pages_text.append(f'--- Page {index} ---\n{text}')
        return '\n\n'.join(pages_text), len(pdf.pages)
