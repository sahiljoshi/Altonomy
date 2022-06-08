FROM python:3

WORKDIR /usr/app/

COPY market_data_connector/requirements.txt ./
RUN pip install  -r requirements.txt

COPY . .


