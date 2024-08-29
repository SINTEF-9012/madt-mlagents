FROM python

ENV PYTHONUNBUFFERED 1
WORKDIR /stream

RUN apt-get update \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY RAG/* .
COPY RAG/tools/* tools/

CMD [ "streamlit", "run", "bot.py" ]