FROM python3.8-alpine
RUN apk --update add bash nano
COPY ./ /var/www
RUN pip install -r /var/www/requirements.txt
WORKDIR /var/www/
CMD flask --app app run --host=0.0.0.0 --port=80
