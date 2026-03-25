# PROJECT_SETUP.md

## Project Setup Instructions

Follow these steps to set up the bilingual translator bot in your local environment and configure the necessary APIs.

### 1. Prerequisites
- Ensure you have Python 3.x installed.
- Install the following libraries:
  ```bash
  pip install googletrans==4.0.0-rc1
  pip install azure-cognitiveservices-translate
  pip install openai
  pip install requests
  ```

### 2. API Configuration Guides

#### Google Translate
- Create a project in the Google Cloud Platform.
- Enable the Google Translate API.
- Generate API credentials (API key).
- Set the API key in your environment variables:
  ```bash
  export GOOGLE_API_KEY='your_google_api_key'
  ```

#### Azure Translator
- Sign in to the Azure portal.
- Create a new Azure Translator resource.
- Obtain the key and endpoint from the resource.
- Set them in your environment variables:
  ```bash
  export AZURE_TRANSLATOR_KEY='your_azure_translator_key'
  export AZURE_TRANSLATOR_ENDPOINT='your_azure_translator_endpoint'
  ```

#### OpenAI
- Create an OpenAI account and go to the API section.
- Generate an API key.
- Set the API key in your environment variables:
  ```bash
  export OPENAI_API_KEY='your_openai_api_key'
  ```

#### Gemini
- Register for access to the Gemini API.
- Follow the instructions provided to obtain your API credentials.
- Set the credentials in your environment:
  ```bash
  export GEMINI_API_KEY='your_gemini_api_key'
  ```

### 3. Folder Structure Explanation
```plaintext
bilingual-translator-bot/
├── src/                      # Source code for the translator bot
│   ├── google_translator.py  # Google Translate integration
│   ├── azure_translator.py    # Azure Translator integration
│   ├── openai_translator.py   # OpenAI integration
│   └── gemini_translator.py   # Gemini integration
├── tests/                    # Test files
│   ├── test_google.py         # Tests for Google Translator
│   ├── test_azure.py          # Tests for Azure Translator
│   └── test_openai.py         # Tests for OpenAI Translator
├── requirements.txt           # Python package dependencies
└── README.md                  # Project overview and instructions
```

### 4. Usage Instructions
- To run the translator bot, simply execute:
  ```bash
  python src/main.py
  ```
- Ensure all API keys are properly set in your environment before running.

For more specific usage instructions and examples, check the documentation in the `/docs` folder once the project is set up.

---