FROM python:3.8-slim
COPY ./BankApp /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python
RUN apt-get update -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install scikit-learn
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]