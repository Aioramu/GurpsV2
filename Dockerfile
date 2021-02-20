FROM python:3.7.0-stretch
WORKDIR /code
COPY requirements.txt /code/

RUN pip install cython
RUN pip install -r requirements.txt --default-timeout=100 future

COPY . .
CMD ["python3"]
