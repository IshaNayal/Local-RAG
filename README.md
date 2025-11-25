My Local RAG Chatbot Project


https://github.com/user-attachments/assets/527c173a-1582-4058-958b-115e184751bd

Project Description

I built an awesome local Retrieval Augmented Generation (RAG) chatbot using Python, Olama, Langchain, Streamlit, and FAISS DB! This project came from my realization that standalone large language models (LLMs) have limits—they can give wrong or unsourced answers since their training data isn’t fully controllable. My RAG chatbot fixes that by delivering accurate, sourced responses, and I’m excited to share how it works!

The star of this project is the "Agentic RAG" approach, which I found to be a huge step up from basic "naive RAG." Naive RAG struggles with follow-up questions because the database doesn’t track the conversation, but my Agentic RAG uses an agent to rewrite queries based on chat history. This keeps everything contextual and the answers spot-on, even as the convo flows!

Here’s how I set it up: I used Olama to run LLMs locally, picking a chat model (like a tool-calling Llama 3.2) and an embedding model based on my hardware. Embeddings were a big "aha" for me—these multi-dimensional numbers capture text meaning, letting my chatbot find semantically similar content instead of just keywords.

My data pipeline is robust and covers everything:





Data Scraping: I used Bright Data to scrape Wikipedia based on topics I set in a keywords.txt file (like "Python" or "Langchain"), controlling depth with options like pages=1 for direct articles or more.



Text Chunking: Long articles get split into smaller, 1000-character chunks for easier retrieval.



Embedding Generation: Each chunk turns into a numerical embedding.



Data Ingestion: Chunks and embeddings go into FAISS DB, my local vector store.







one_scraping_wikipedia.py: Starts the Wikipedia scrape with Bright Data, saving a snapshot.txt to track progress.



two_chunking_embedding_ingestion.py: Fetches scraped data, chunks it, creates embeddings, and loads them into Chroma DB.



three_chatbot.py: Launches a Streamlit interface, tying the LLM, retrieval from FAISS DB, and agentic logic for accurate, sourced replies.

To get it running, I set up a virtual environment, installed dependencies from requirements.txt, and tweaked an .env file with my models and Bright Data API key. I love how I can swap in other LLM providers like OpenAI or Anthropic just by updating the .env!

The result? My chatbot gives precise, sourced answers, way better than a plain LLM. I’m thrilled with this local, controllable AI—it’s perfect for reliable, custom projects!

Highlights





🤖 Agentic RAG Rocks: My Agentic RAG beats naive RAG by keeping convo context and rewriting queries for great follow-ups.



💻 Local LLMs with Olama: I run models locally with Olama, choosing chat and embedding models to fit my setup.



📊 Full Data Pipeline: Scraping Wikipedia, chunking text, making embeddings, and storing in Chroma DB—my pipeline’s solid!



🧠 Embeddings Power: I learned embeddings use multi-dimensional numbers for meaning, enabling smart searches.





🌐 Custom Topics: I edited keywords.txt to pick topics like Python, tailoring my chatbot without code changes.



✅ Sourced Answers: My demo shows accurate replies with sources, fixing LLM flaws.

Key Takeaways


🧠 Better Chats with Agentic RAG: I see why naive RAG struggles—Agentic RAG uses chat history for relevant, flowing responses.



🔒 Local Power: Running LLMs locally with Olama gives me privacy, no API costs, and full control—great for sensitive use!



🏗️ Strong Pipeline: My scraping-to-ingestion pipeline, with Bright Data and chunking, makes this scalable and reliable.



🎯 Embeddings Are Key: Multi-dimensional embeddings let my database match meaning, not just words—super cool!



⚙️ Flexible Design: I can tweak models or topics via .env and keywords.txt for easy customization.



🚀 Streamlit Speed: Streamlit made my UI quick and simple, letting me focus on the RAG logic.



✅ Fixing LLMs: My RAG system beats LLM issues like wrong facts, giving reliable, sourced answers for real use.



