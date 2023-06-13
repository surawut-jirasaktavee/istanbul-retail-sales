echo "Setting the right Airflow user"
mkdir -p ./dags ./logs ./plugins ./config
echo "AIRFLOW_UID=$(id -u)" > .env
echo GCP_PROJECT_ID=test >> .env
echo GCP_GCS_BUCKET=test >> .env

echo "Build airflow with docker compose..."
docker-compose build

echo "Running airflow-init..."
docker-compose up airflow-init

echo "Starting up airflow in detached mode..."
docker-compose up -d

echo "Airflow started successfully."
echo "Airflow is running in detached mode. "
echo "Run 'docker-compose logs --follow' to see the logs."

echo "Airflow UI can access with the following..."
echo "http://localhost:8080/home"