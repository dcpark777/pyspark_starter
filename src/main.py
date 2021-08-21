import argparse
import importlib
import os
import sys
import time
from collections import deque

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

from shared.logging import Log4j

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
    print("IN THE MAIN")
    parser = argparse.ArgumentParser()
    parser.add_argument('--job_name', required=True)
    args = parser.parse_known_args()
    job_name = args[0].job_name
    forward_args = deque(args[1])
    print(job_name)

    forward_args.extendleft([job_name, '--job_name'])
    print(forward_args)

    job_module = importlib.import_module('jobs.%s.%s' % (job_name, job_name))
    job_module.main(forward_args)