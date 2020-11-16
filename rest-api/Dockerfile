  
FROM tiangolo/uwsgi-nginx-flask:python3.8



COPY ./app /app

RUN cd /app 

RUN pip install -r requirements.txt 

RUN cd ..