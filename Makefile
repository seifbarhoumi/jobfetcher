.PHONY: install test  run docker-build docker-run setup-cron list-cron stop-cron start-cron

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python -m job_cli fetch job --type-contrat CDI --departement 07 --limit 50

docker-build:
	docker build -t jobfetcher .

docker-run:
	docker run --rm jobfetcher fetch job --type-contrat CDI --departement 07 --limit 50

# Setup Cron Job to run daily at 6 AM
setup-cron:
	@echo "0 6 * * * /bin/bash $(PWD)/cron_fetch.sh >> $(PWD)/cron.log 2>&1" | crontab -
	@echo "✅ Cron job scheduled at 6 AM daily."

# List active cron jobs
list-cron:
	@crontab -l

# Remove cron job
stop-cron:
	@crontab -r
	@echo "🛑 Cron job removed."

# Start cron service// Docker
start-cron:
	@service cron start
	@echo "🚀 Cron service started."
