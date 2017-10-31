FROM python:2.7

RUN pip install cython==0.27.0
RUN pip install chorde
RUN pip install sharedbuffers

WORKDIR /
