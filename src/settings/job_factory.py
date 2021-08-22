from .job_types import JobTypes
from jobs.reconciler import ReconcilerJob
from pyspark.sql import SparkSession
from settings.job import Job
from shared.logging import Log4j


class JobFactory:

    @staticmethod
    def get_job(job_type: str, spark: SparkSession, log: Log4j, job_args: list[str]) -> Job:
        assert job_type in JobTypes._member_names_, f'Invalid JobType provided: {job_type}'

        if job_type == "ReconcilerJob":
            return ReconcilerJob(spark, log, job_args)
        else:
            raise ValueError(f'Invalid JobType provided: {job_type}')