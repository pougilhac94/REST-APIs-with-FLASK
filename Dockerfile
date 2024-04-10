FROM python:3.11
WORKDIR /app
COPY requirements_new.txt .
RUN pip install --no-cache-dir --upgrade -r requirements_new.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]