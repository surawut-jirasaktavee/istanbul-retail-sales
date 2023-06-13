# https://airflow.apache.org/docs/apache-airflow/2.5.3/howto/docker-compose/index.html
FROM apache/airflow:2.2.3-python3.9

ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW_VERSION=2.2.3

USER root
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get upgrade -y && \
    apt-get install -y git

# Ref: https://airflow.apache.org/docs/docker-stack/recipes.html
SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

ARG CLOUD_SDK_VERSION=322.0.0
ENV GCLOUD_HOME=/home/google-cloud-sdk

ENV PATH="${GCLOUD_HOME}/bin/:${PATH}"

RUN DOWNLOAD_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz" \
    && TMP_DIR="$(mktemp -d)" \
    && curl -fL "${DOWNLOAD_URL}" --output "${TMP_DIR}/google-cloud-sdk.tar.gz" \
    && mkdir -p "${GCLOUD_HOME}" \
    && tar xzf "${TMP_DIR}/google-cloud-sdk.tar.gz" -C "${GCLOUD_HOME}" --strip-components=1 \
    && "${GCLOUD_HOME}/install.sh" \
       --bash-completion=false \
       --path-update=false \
       --usage-reporting=false \
       --quiet \
    && rm -rf "${TMP_DIR}" \
    && gcloud --version

USER airflow
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir apache-airflow[google]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[apache-spark]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[opsgenie]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[cncf.kubernetes]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[postgres]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[dbt.cloud]==${AIRFLOW_VERSION} \
    # && pip install --no-cache-dir apache-airflow[airbyte]==${AIRFLOW_VERSION}

WORKDIR $AIRFLOW_HOME

EXPOSE 8090

USER root