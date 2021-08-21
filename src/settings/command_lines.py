import argparse
from argparse import ArgumentParser


class SparkCommandLine(ArgumentParser):
    def __init__(self):
        super(SparkCommandLine, self).__init__()
        self.spark_executor_cores = self.add_argument('--spark_executor_cores', required=False, default=4)


class BaseCommandLine(ArgumentParser):
    """

    """
    def __init__(self):
        super(BaseCommandLine, self).__init__()
        self.job_name = self.add_argument('--job_name', required=True)
        self.environment = self.add_argument('--environment', required=True)
        self.region = self.add_argument('--region', required=True)

