from pyspark.sql.functions import from_json, col, month, dayofmonth, col, year, udf


class SparkTransformer:
    
    def __init__(self, encode_type: str = "latin1", decode_type: str = "unicode-escape"):
        self.encode_type = encode_type
        self.decode_type = decode_type
        
    @udf
    def string_decode(self, text, encoding: str="utf-8"):
        """
        To bytes, required by "unicode-escape" and perform the actual octal-escaping decode then 1:1 mapping back to bytes
        finally decode original encoding
        
        Parameters:
        ----------
            text: str
                The text to be decoded
            encoding: str
                The encoding to be used, default is "utf-8"
        
        Returns:
        --------
            text: str
                The decoded text
        
        """
        
        
        if text:
            return (repr(text).encode(self.encode_type)
                    .decode(self.decode_type)
                    .encode(self.encode_type)       
                    .decode(encoding)
                    .strip("\""))

        else:
            return text
       
    def stream_transform(self, spark_stream, stream_schema):
        """
        Process stream to fetch on value from the kafka message.
        convert ts to timestamp format and produce year, month, day,
        hour columns
        
        Parameters:
        ----------
            stream : DataStreamReader
                The data stream reader for your stream
        Returns:
        ----------
            stream: DataStreamReader
        """

        # read only value from the incoming message and convert the contents
        # inside to the passed schema
        stream = (spark_stream
                .selectExpr("CAST(value AS STRING)")
                .select(from_json(col("value"), stream_schema).alias("data"))
                .select("data.*")
                )       

        # Add month, day, hour to split the data into separate directories
        stream = (stream
                .withColumn("invoice_year", year(col("invoice_date")))
                .withColumn("invoice_month", month(col("invoice_date")))
                .withColumn("invoice_day", dayofmonth(col("invoice_date")))
                )

        return stream
    
    def create_file_write_stream(
        self, 
        spark_stream,
        storage_path: str,
        checkpoint_path: str, 
        trigger: str="120 seconds", 
        output_mode: str="append",
        file_format: str="parquet"
        ):
        """
        Write the stream back to a file store
        
        Parameters:
        ----------
            stream : DataStreamReader
                The data stream reader for your stream
            file_format : str
                parquet, csv, orc etc
            storage_path : str
                The file output path
            checkpoint_path : str
                The checkpoint location for spark
            trigger : str
                The trigger interval
            output_mode : str
                append, complete, update
        """

        write_stream = (spark_stream
                        .writeStream
                        .format(file_format)
                        .partitionBy("invoice_month", "invoice_day")
                        .option("path", storage_path)
                        .option("checkpointLocation", checkpoint_path)
                        .trigger(processingTime=trigger)
                        .outputMode(output_mode))

        return write_stream