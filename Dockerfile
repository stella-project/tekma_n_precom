FROM python:3.7

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 app.py