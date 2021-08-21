from shared.logging import Log4j
from settings.spark_configuration import SparkConfiguration
from settings.job import Job
from .command_line import CommandLine
import typing

class ReconcilerJob(Job):
    def __init__(self, command_line):
        super(ReconcilerJob, self).__init__()
        self.spark = SparkConfiguration.configure_spark_session(command_line)
        self.log = Log4j(self.spark)

        self.environment = command_line.get('environment')
        self.region = command_line.get('region')
        self.in_path = command_line.get('in_path')


    def run(self):
        self.log.info("WE ARE IN THE RECONCILER RUN")
        print(self.spark.sparkContext.getConf().getAll())
        print(self.environment)
        print(self.region)
        print(self.in_path)
        columns = ["language", "users_count"]
        data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
        rdd = self.spark.sparkContext.parallelize(data)
        dfFromRDD1 = rdd.toDF(columns)
        dfFromRDD1.printSchema()
        dfFromRDD1.show()
        self.spark.stop()


def main(args: list[str]) -> None:
    print("IN RECONCILER MAIN")
    print(args)
    command_line = CommandLine().parse(args)
    print(command_line)
    ReconcilerJob(command_line).run()