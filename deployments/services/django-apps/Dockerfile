FROM python:3.8.3-alpine

USER app

WORKDIR /home/app

RUN groupadd -g $GID -o app  && \
    useradd -g $GID -u $UID  -mr -d /home/app -o -s /bin/bash app && \
    mkdir /home/app/static && \
    chown -R app:app /home/app/static

ENV PATH "$PATH:/home/app/.local/bin"

RUN pip install --upgrade pip
COPY --chown=app:app requirements.txt .
RUN pip install -r /home/app/requirements.txt

COPY --chown=app:app . .

EXPOSE 8000-8084

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]

