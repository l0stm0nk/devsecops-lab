FROM python:3.11

WORKDIR /app

COPY app/ .

RUN pip install -r requirements.txt

# Bad practice: running as root, debug on, secret in ENV
ENV SECRET_KEY=supersecret123
ENV FLASK_DEBUG=1

EXPOSE 5000

CMD ["python", "app.py"]
