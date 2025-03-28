FROM python:3.12-bullseye

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev cron openssh-client flake8 locales vim

# Create the bot user and group
RUN groupadd -r bot && useradd -r -g bot bot

WORKDIR /bot

RUN mkdir /bot/static && mkdir /bot/media && chown -R bot:bot /bot && chmod 755 /bot

COPY --chown=bot:bot . .

RUN pip install -r requirements.txt

USER bot

CMD ["gunicorn", "-b", "0.0.0.0:8000", "djangoset.wsgi:application", "main.py"]


