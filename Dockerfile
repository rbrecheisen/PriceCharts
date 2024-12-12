FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y vim curl dos2unix \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /data/static \
    && mkdir -p /data/filesets \
    && mkdir -p /data/uploads/{0..9} && chmod 777 -R /data/uploads

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip setuptools wheel && pip install -r /requirements.txt --verbose

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN dos2unix /docker-entrypoint.sh && chmod +x /docker-entrypoint.sh

COPY src/pricecharts /src

WORKDIR /src

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/docker-entrypoint.sh"]