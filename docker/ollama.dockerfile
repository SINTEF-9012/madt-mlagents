FROM ollama/ollama

RUN /usr/bin/ollama serve & sleep 5 && /usr/bin/ollama pull gemma2:2b 