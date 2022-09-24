FROM python:3.8.6

LABEL MAINTAINER="Bekhruz yoshlikmedia@gmail.com"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# RUN pip install pip setuptools wheel
RUN pip install -r requirements.txt
# RUN pip install spacy

RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

COPY . /app

CMD python -u app.py