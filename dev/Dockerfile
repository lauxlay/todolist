FROM python:3.7.5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 8080

CMD ["/bin/sh", "entrypoint.sh" ]