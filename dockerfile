FROM python:3.7
WORKDIR /usr/src/myapp
COPY . /usr/src/myapp
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
