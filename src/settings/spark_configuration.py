from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import typing

class SparkConfiguration:
    def __init__(self):
        pass

    @staticmethod
    def configure_spark_session(command_line: dict):
        conf = SparkConf()
        print(f"COMMAND LINE: {command_line}")
        print(type(command_line))
        conf.set('spark.executor.cores', command_line.get('spark_executor_cores'))
        conf.set('spark.executor.memory', command_line.get('spark_executor_memory', '15g'))

        conf.set('appName', command_line.get('job_name'))
        conf.set('spark.app.name', command_line.get('job_name'))
        conf.set('spark.serializer', 'org.apache.spark.serializer.KryoSerializer')
        conf.set('spark.speculation', 'false')
        conf.set('spark.io.compression.codec', 'lz4')
        conf.set('spark.debug.maxToStringFields', '1000')
        conf.set('spark.logLineage', 'true')
        sc = SparkContext(conf=conf)
        spark = SparkSession(sc).builder.getOrCreate()
        return spark
