FROM python:3.5

WORKDIR /

COPY requirements requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY nerus nerus
COPY setup.py .
RUN pip install --no-cache-dir -e .

ENTRYPOINT ["nerus-ctl"]
