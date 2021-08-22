import pytest

from src.settings.job_factory import JobFactory
from tests.test_spark_configuration import get_spark_session
from tests.test_logging import get_test_log

def test_job_factory():
    spark = get_spark_session()
    log = get_test_log()
    job_type = "ReconcilerJob"
    args = ['--job_name', 'test_reconciler',
            '--job_type', job_type,
            '--environment', 'qa',
            '--region', 'us-east-1',
            '--in_path', 'path']
    job = JobFactory.get_job(job_type, spark, log, args)
    spark.stop()

    with pytest.raises(Exception):
        job = JobFactory.get_job('FakeJob', spark, log, args)
        spark.stop()

