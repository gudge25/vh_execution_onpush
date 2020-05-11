# Container image that runs your code
FROM python:3.8.2-slim-buster

RUN pip install requests

ADD runExecution.py /runExecution.py
CMD ["/runExecution.py"]
ENTRYPOINT ["python"]