from pyspark.sql import SparkSession
from src.settings.spark_configuration import SparkConfiguration

def get_spark_session():
    spark = SparkSession.builder\
        .master("local[*]")\
        .config("spark.executor.memory", "2g")\
        .config("spark.executor.cores", 1)\
        .config("spark.app.name", "TestSparkSession")\
        .getOrCreate()
    return spark

def test_spark_session():
    command_line = {
        'spark_executor_cores': 1,
        'spark_executor_memory': '2g',
        'job_name': 'TestSparkJob'
    }
    spark = SparkConfiguration().configure_spark_session(command_line)
    spark.stop()
