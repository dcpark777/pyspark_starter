from shared.logging import Log4j
from settings.spark_configuration import SparkConfiguration
from settings.job import Job
import typing
from settings.command_lines import BaseCommandLine, SparkCommandLine


class CommandLine(BaseCommandLine, SparkCommandLine):
    def __init__(self):
        super(CommandLine, self).__init__()
        self.in_path = self.add_argument('--in_path', required=True)

    def parse(self, args: list[str]):
        print("Parsing args")
        args = vars(self.parse_args(args))
        print(args)
        return args


class ReconcilerJob(Job):
    def __init__(self, spark, log, job_args):
        super(ReconcilerJob, self).__init__()
        self.command_line = CommandLine().parse(job_args)
        self.spark = spark
        self.log = log

        self.environment = self.command_line.get('environment')
        self.region = self.command_line.get('region')
        self.in_path = self.command_line.get('in_path')


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