from pyspark.sql.types import StructType,StructField, StringType, IntegerType

from pyspark.sql.types import (IntegerType,
                               StringType,
                               DoubleType,
                               StructField,
                               StructType,
                               TimestampType,
)

schema = {
    'customer_shopping_data': StructType([
        StructField("invoice_no", StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("gender", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("category", StringType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("price", DoubleType(), True),
        StructField("payment_method", StringType(), True),
        StructField("invoice_date", TimestampType(), True),
        StructField("shopping_mall", StringType(), True)
      ])
}