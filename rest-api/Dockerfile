FROM python:3.8.1

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY .  .

EXPOSE 5000

CMD ["python" , "./rest_api.py"]