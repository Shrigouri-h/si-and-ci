
FROM python:3.12-slim

WORKDIR / app

COPY interest.py .

CMD ["python", "interest.py"]
