import os
import sys
import time
from collections import deque
from shared.logging import Log4j
from settings.job_factory import JobFactory
from settings.command_lines import CommandLine
from settings.spark_configuration import SparkConfiguration


if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

try:
    import pyspark
except:
    import findspark
    findspark.init()
    import pyspark


if __name__ == '__main__':
    # Capture all arguments except python script name `main.py`
    args = sys.argv[1:]
    command_line = CommandLine()
    # Parse BaseCommandLine and SparkCommandLine arguments
    command_line_args = command_line.parse_known_args(args)
    print(command_line_args)
    job_name = command_line_args[0].job_name
    job_type = command_line_args[0].job_type
    # job_args is a list of arguments that have not yet been parsed
    # These arguments are job-specific
    job_args = deque(command_line_args[1])
    print(f"Initializing Job Type: {job_type}")
    print(f"Job Name: {job_name}")
    print(f"Provided Arguments: {args}")

    # Initialize SparkSession using args parsed by SparkCommandLine
    spark = SparkConfiguration.configure_spark_session(vars(command_line_args[0]))
    # Initialize Log4J
    log = Log4j(spark)
    # Get Job and run
    job = JobFactory.get_job(job_type, spark, log, args)
    job.run()
    spark.stop()