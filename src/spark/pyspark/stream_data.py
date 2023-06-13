import os

from app.spark_app import SparkApp
from transform.spark_stream import SparkStreamer
from transform.spark_transform import SparkTransformer
from schema.customer_schema import schema

# Kafka Configs
LISTEN_EVENTS_TOPIC = "customer_shopping_data"
KAFKA_PORT = "9092"
KAFKA_ADDRESS = os.getenv("KAFKA_ADDRESS", "localhost")
GCP_GCS_BUCKET = os.getenv("GCP_GCS_BUCKET", "istanbul-retail-sales")
GCS_STORAGE_PATH = f"gs://{GCP_GCS_BUCKET}"

# Spark configs
APP_NAME = "customer_shopping_app"

spark_app = SparkApp(APP_NAME)
# initialize a spark session
gcs_conf = spark_app.get_spark_gcs_conf(sa_name="spark-sa")
sc = spark_app.create_or_get_spark_context(gcs_conf=gcs_conf, sa_name="spark-sa")
spark = spark_app.create_or_get_spark_session(spark_context=sc)
spark.streams.resetTerminated()

spark_streamer = SparkStreamer(
    spark,
    KAFKA_ADDRESS,
    KAFKA_PORT,
    LISTEN_EVENTS_TOPIC,
)
spark_transformer = SparkTransformer()

# listen events stream
listen_events = spark_streamer.create_kafka_read_stream()
listen_events = spark_transformer.stream_transform(
    listen_events, schema[LISTEN_EVENTS_TOPIC])

# write a file to storage every 2 minutes in parquet format
listen_events_writer = spark_transformer.create_file_write_stream(listen_events,
                                                f"{GCS_STORAGE_PATH}/{LISTEN_EVENTS_TOPIC}",
                                                f"{GCS_STORAGE_PATH}/checkpoint/{LISTEN_EVENTS_TOPIC}"
                                                )

listen_events_writer.start()

spark.streams.awaitAnyTermination()