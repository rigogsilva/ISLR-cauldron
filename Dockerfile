FROM swernst/cauldron:current-miniconda

MAINTAINER rigogsilva@gmail.com

COPY requirements.txt /build/requirements.txt

RUN pip3 install -r /build/requirements.txt
