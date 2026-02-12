FROM marketsquare/robotframework-browser:latest

USER root
WORKDIR /opt/robotframework/tests

ENV PYTHONPATH="/opt/robotframework/tests"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN rfbrowser init

COPY . .

CMD ["robot", "-d", "results", "tests/"]