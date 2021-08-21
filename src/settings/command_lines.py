from argparse import ArgumentParser


class BaseCommandLine(ArgumentParser):
    """CommandLine parser for arguments required by all jobs."""
    def __init__(self):
        super(BaseCommandLine, self).__init__()
        self.job_name = self.add_argument('--job_name', required=True)
        self.environment = self.add_argument('--environment', required=True)
        self.region = self.add_argument('--region', required=True)


class SparkCommandLine(ArgumentParser):
    """CommandLine parser for optional spark configuration arguments"""
    def __init__(self):
        super(SparkCommandLine, self).__init__()
        self.spark_executor_cores = self.add_argument('--spark_executor_cores', required=False, type=int, default=4)
        self.spark_executor_memory = self.add_argument('--spark_executor_memory', required=False, type=str, default='15g')


