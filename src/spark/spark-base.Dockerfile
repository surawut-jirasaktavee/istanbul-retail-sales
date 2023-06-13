FROM premdocker2022/spark-cluster-base:java-17-jre

ENV SPARK_VERSION=3.3.2
ENV HADOOP_VERSION=3

RUN apt-get update \
    && ACCEPT_EULA=Y apt-get upgrade -y \
    && apt-get install -y git \
    && apt-get install wget

ENV HOME=/istanbul-retail

RUN mkdir -p ${HOME}
RUN mkdir -p ${HOME}/spark && cd ${HOME}/spark

RUN cd ${HOME}/spark \
    && wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && tar xzfv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

ENV SPARK_HOME="${HOME}/spark/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}"
ENV PATH="${SPARK_HOME}/bin:${PATH}"

ENV PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
ENV PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"

ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV PYSPARK_PYTHON=python3

RUN mkdir -p ${SPARK_HOME}/logs

WORKDIR ${SPARK_HOME}
