FROM python:3.11
WORKDIR /app
COPY requirements_new.txt .
RUN pip install --no-cache-dir --upgrade -r requirements_new.txt
COPY . .
RUN flask db upgrade
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]