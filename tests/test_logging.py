from src.shared.logging import Log4j
from tests.test_spark_configuration import get_spark_session
import os

def get_test_log():
    spark = get_spark_session()
    log = Log4j(spark, f'{os.getcwd()}/tests/log4j.properties')
    return log

def test_logging():
    spark = get_spark_session()
    log = Log4j(spark, f'{os.getcwd()}/tests/log4j.properties')
    spark.stop()
    log.info("info")
    log.error("error")
    log.warn("warn")
