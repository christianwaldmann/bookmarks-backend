FROM python:3.11-slim-buster
EXPOSE 80
WORKDIR /App
COPY requirements.txt /App
RUN pip install -r requirements.txt
COPY . /App
CMD ["./start.sh"]
