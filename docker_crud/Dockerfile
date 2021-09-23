FROM python:3.8
ENV SECRET_KEY='django-insecure-nw^y+m^wmxza1asgk+)!ua2qx9)g+#v=6%76-9i8i(6eqiw94j'
WORKDIR ./stocks_products
COPY ./stocks_products /stocks_products
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]