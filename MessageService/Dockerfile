FROM python:3.11

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000
WORKDIR /usr/src

CMD [ "python", "app/main.py" ]