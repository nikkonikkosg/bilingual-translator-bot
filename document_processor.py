import os
import docx
import pandas as pd

class DocumentProcessor:
    def __init__(self):
        pass

    def process_docx(self, file_path):
        """
        Process .docx file to extract text content.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        doc = docx.Document(file_path)
        text_content = ''
        for paragraph in doc.paragraphs:
            text_content += paragraph.text + '\n'
        return text_content

    def process_xlsx(self, file_path):
        """
        Process .xlsx file to extract data from the first sheet.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        df = pd.read_excel(file_path)
        return df

    def generate_bilingual_content(self, text, target_language):
        """
        Generate bilingual content based on input text.
        This is a placeholder for an actual translation implementation.
        """
        # Sample mock translation function
        translated_text = f"{text} \nTranslated to {target_language}: {text} (mock translation)"
        return translated_text

# Example usage
# dp = DocumentProcessor()
# doc_text = dp.process_docx('example.docx')
# df = dp.process_xlsx('example.xlsx')
# bilingual_output = dp.generate_bilingual_content(doc_text, 'Spanish')