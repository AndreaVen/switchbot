FROM python:3.8.10

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY outdoor_meter.py .
COPY switchbot.py .
COPY data_writer.py .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
