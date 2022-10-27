FROM python:3.6
COPY ./Django-crud-application-master Django-crud-application-master
WORKDIR /Django-crud-application-master
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
# RUN python manage.py migrate
RUN echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
#Pip command without proxy setting
RUN pip install -r requirements.txt
#Use this one if you have proxy setting
RUN pip --proxy http://[proxy:port] install -r requirements.txt
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]