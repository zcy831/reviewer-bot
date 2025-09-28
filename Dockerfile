FROM python:3.8.8

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

RUN mkdir -p /opt/web/fastapi
RUN mkdir -p /opt/web/fastapi/log

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--log-level", "info", "--proxy-headers", "--forwarded-allow-ips", "*"]
# CMD ["gunicorn", "main:app", "-c", "./gunicorn.py"]
# CMD ["python3", "./main.py"]
