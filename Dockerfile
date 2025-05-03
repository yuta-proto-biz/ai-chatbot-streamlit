FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install spacy
RUN python -m spacy download ja_core_news_sm

COPY . .

CMD ["streamlit", "run", "chatbot_mock.py"]