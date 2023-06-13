class SparkStreamer:
    
    def __init__(self, spark, kafka_address: str, kafka_port: int, kafka_topic: str):
        self.spark_app = spark
        self.kafka_address = kafka_address
        self.kafka_port = kafka_port
        self.kafka_topic = kafka_topic
    
    def create_kafka_read_stream(self, starting_offset="earliest"):
        """
        Creates a kafka read stream
        
        Parameters:
        ----------
            spark : SparkSession
                A SparkSession object
            kafka_address: str
                Host address of the kafka bootstrap server
            topic : str
                Name of the kafka topic
            starting_offset: str
                Starting offset configuration, "earliest" by default 
        Returns:
        ----------
            read_stream: DataStreamReader
        """

        read_stream = (self.spark_app
                    .readStream
                    .format("kafka")
                    .option("kafka.bootstrap.servers", f"{self.kafka_address}:{self.kafka_port}")
                    .option("failOnDataLoss", False)
                    .option("startingOffsets", starting_offset)
                    .option("subscribe", self.kafka_topic)
                    .load())

        return read_stream