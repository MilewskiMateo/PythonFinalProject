FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir supervisor
RUN pip install --no-cache-dir rq
RUN pip install --no-cache-dir requests

ENTRYPOINT ["/bin/bash", "-c", "supervisord -c /usr/src/app/supervisord.conf -n"]