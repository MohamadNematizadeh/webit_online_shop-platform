FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.text

COPY . .

EXPOSE 8000
CMD ["sh","-c","python manage.py migrate && python manage.py runserver runserver 0.0.0.0:8000"]