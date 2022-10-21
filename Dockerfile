FROM python:3

RUN git clone https://github.com/LucaTerranovaB/Buscaminas.git

WORKDIR /Buscaminas

RUN pip install -r requirements.txt

CMD ['python3', 'test_buscaminas.py']