FROM python:3
WORKDIR /flask

ADD . /flask

RUN pip install --upgrade cython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
