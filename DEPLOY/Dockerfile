FROM python:3.10-slim

RUN useradd --uid 1111 job_fetcher

WORKDIR /jobfetcher

COPY requirements.txt .
COPY .env .
COPY job_cli/ job_cli/
COPY services/ services/
COPY utils/ utils/

RUN pip install --no-cache-dir -r requirements.txt

USER job_fetcher

ENTRYPOINT ["python", "-m", "job_cli"]
CMD ["fetch", "job", "--departement", "07", "--type-contrat", "CDI", "--limit", "50"]
