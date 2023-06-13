FROM premdocker2022/spark-base:3.3.2

# -- Runtime

ARG spark_master_web_ui=8081

EXPOSE ${spark_master_web_ui}
CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-worker.out