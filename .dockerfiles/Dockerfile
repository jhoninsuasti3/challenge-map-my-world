FROM public.ecr.aws/docker/library/python:3.9
ARG ENVIRONMENT=default
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y supervisor

# Copiar los archivos necesarios
COPY start-container.sh /usr/local/bin/start-container.sh
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY alembic.ini /app/
COPY alembic /app/alembic
RUN chmod +x /usr/local/bin/start-container.sh

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install "setuptools<58.0.0"
RUN pip install -r requirements.txt
COPY . /app/

EXPOSE 8000
EXPOSE 5555

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

#ENTRYPOINT ["start-container.sh"]
