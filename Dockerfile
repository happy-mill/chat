FROM python:alpine
ENV OPENAI_KEY = "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"
ENV TG_KEY = "5911521678:AAFH_IAuxkDMrq6iWFjXe4SHqob9Ia3Dso0"
RUN pip install aiogram openai
COPY . ./app
CMD ["python", "./main.py"]