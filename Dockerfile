FROM python:3.10.5-slim-bullseye
EXPOSE  5000
WORKDIR /app
COPY .  /app
RUN pip install -U pip && pip install -r requirements.txt
CMD ["python", "app.py"]