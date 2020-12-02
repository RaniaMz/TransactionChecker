FROM python:3
COPY . .
ENTRYPOINT ["python","main.py"]
