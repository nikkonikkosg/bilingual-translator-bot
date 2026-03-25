import requests

class TranslationService:
    def __init__(self):
        self.google_translate_api_key = 'YOUR_GOOGLE_TRANSLATE_API_KEY'
        self.azure_api_key = 'YOUR_AZURE_TRANSLATOR_API_KEY'
        self.openai_api_key = 'YOUR_OPENAI_API_KEY'
        self.gemini_api_key = 'YOUR_GEMINI_API_KEY'

    def google_translate(self, text, target_language):
        url = f'https://translation.googleapis.com/language/translate/v2?key={self.google_translate_api_key}'
        data = {
            'q': text,
            'target': target_language
        }
        response = requests.post(url, json=data)
        return response.json() if response.status_code == 200 else None

    def azure_translate(self, text, target_language):
        url = f'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={target_language}'
        headers = {
            'Ocp-Apim-Subscription-Key': self.azure_api_key,
            'Content-type': 'application/json'
        }
        body = [{'text': text}]
        response = requests.post(url, headers=headers, json=body)
        return response.json() if response.status_code == 200 else None

    def openai_translate(self, text, target_language):
        url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
        headers = {
            'Authorization': f'Bearer {self.openai_api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'prompt': f'Translate the following text to {target_language}: {text}',
            'max_tokens': 60
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json() if response.status_code == 200 else None

    def gemini_translate(self, text, target_language):
        url = f'https://api.gemini.com/v1/translate?api_key={self.gemini_api_key}'
        data = {
            'text': text,
            'target_language': target_language
        }
        response = requests.post(url, json=data)
        return response.json() if response.status_code == 200 else None
