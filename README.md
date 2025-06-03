local RAG with Ollama
Prerequisites
Python 3.11+
Installation
1. Clone the repository:
git clone https://github.com/ThomasJanssen-tech/Local-RAG-with-Ollama
cd Local-RAG-With-Ollama
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
4. Install libraries
pip install -r requirements.txt
5. Add Bright Data API Key
Get your $15 Bright Data credits: https://brdta.com/tomstechacademy
Rename the .env.example file to .env
Add your Bright Data API key
If you want to use ChatGPT or Anthropic models, add an API key (not required for Ollama)
Executing the scripts
Open a terminal in VS Code

Execute the following command:

python run 1_scraping_wikipedia.py
python run 2_chunking_embedding_ingestion.py
streamlit run 3_chatbot.py
Further reading
https://www.ibm.com/think/topics/vector-embedding
https://ollama.com/blog/embedding-models
https://python.langchain.com/docs/integrations/vectorstores/chroma/
https://python.langchain.com/docs/integrations/text_embedding/ollama/
https://ollama.com/library/mxbai-embed-large
https://ollama.com/library/qwen3
