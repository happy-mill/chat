FROM python:alpine
ENV OPENAI_KEY=
ENV TG_KEY=
RUN pip install aiogram openai
COPY . ./app
CMD ["python", "./app/main.py"]