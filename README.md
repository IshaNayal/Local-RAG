local RAG with Ollama
Prerequisites
Python 3.11+
Installation
1. Clone the repository:
git clone https://github.com/IshaNayal/Local-RAG
cd Local-RAG-With-Ollama
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
4. Install libraries
pip install -r requirements.txt
5. Add Bright Data API Key
Rename the .env.example file to .env
Add your Bright Data API key
If you want to use ChatGPT or Anthropic models, add an API key (not required for Ollama)
Executing the scripts
Open a terminal in VS Code

Execute the following command:

python run 1_scraping_wikipedia.py
python run 2_chunking_embedding_ingestion.py
streamlit run 3_chatbot.py
