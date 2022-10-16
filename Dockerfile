FROM python:3.9.5-slim
RUN mkdir /app
COPY requirements.txt /app
RUN apt update && apt install curl -y
RUN apt install gdal-bin -y && apt install libgdal-dev -y
RUN apt install python3-gdal -y
RUN apt install binutils -y && apt install libproj-dev -y
RUN pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY django_map/ /app
WORKDIR /app
