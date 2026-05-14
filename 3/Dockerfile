FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 ca-certificates &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /script

COPY yadro.py .

ENTRYPOINT ["python3", "yadro.py"]