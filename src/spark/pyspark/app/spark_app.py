from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext


class SparkApp:
    
    def __init__(self, app_name: str, 
                #  master: str = "spark://spark-master:7077",
                 ):
        self.app_name = app_name
        # self.master = master

    def create_or_get_spark_session(self, spark_context):
        """
        Creates or gets a Spark Session
        Parameters:
            app_name : str
                Pass the name of your app
            master : str
                Choosing the Spark master, yarn is the default
        Returns:
            spark: SparkSession
        """
        
        spark = (SparkSession \
            .builder \
            .appName(self.app_name)
            .config(conf=spark_context.getConf()) \
            .getOrCreate())

        return spark
    
    def get_spark_gcs_conf(self, sa_name: str,
                       credentials_location: str = "../../credentials"
                       ):
       
        sa_credential = f"{credentials_location}/{sa_name}.json"
        
        conf = SparkConf() \
            .set("spark.jars", "./app/lib/gcs-connector-hadoop3-2.2.15.jar") \
            .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
            .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", sa_credential)
            # .setAppName(self.app_name) \
            # .setMaster(self.master) \
           
        return conf
   
    def create_or_get_spark_context(self, gcs_conf,
                                    sa_name: str,
                                    credentials_location: str = "../../credentials"
                                    ):
       
        sa_credential = f"{credentials_location}/{sa_name}.json"
       
        sc = SparkContext(conf=gcs_conf)
        
        hadoop_conf = sc._jsc.hadoopConfiguration()
        hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
        hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
        hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", sa_credential)
        hadoop_conf.set("fs.gs.auth.service.account.enable", "true")
        
        return sc
