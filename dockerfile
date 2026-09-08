FROM python:3.12

WORKDIR function/

COPY my_function.py .

CMD ["python", "my_function.py"]


