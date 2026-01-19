FROM python:3.12
WORKDIR / app
COPY "interest.py"
CMD ["python", "interest.py"]