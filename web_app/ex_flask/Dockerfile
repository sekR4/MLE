FROM python:3.8-buster

EXPOSE 3001/tcp

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./worldbank.py" ]