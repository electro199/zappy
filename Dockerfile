FROM python:3.10-bullseye@sha256:52a58113e1cf1e0987de24226a60aff16cb235068cdbaf4a1a8f9585ae42463b
LABEL org.opencontainers.image.authors="Jason Cameron <jason@jasoncameron.dev>"
LABEL org.opencontainers.image.source="https://github.com/LewisProjects/Ogiroid"
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r -no-cache-dir requirements.txt 
COPY . .
CMD ["python3", "main.py"]
