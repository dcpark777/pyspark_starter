from settings.command_lines import BaseCommandLine, SparkCommandLine
import typing

class CommandLine(BaseCommandLine, SparkCommandLine):
    def __init__(self):
        super(CommandLine, self).__init__()
        self.in_path = self.add_argument('--in_path', required=True)

    def parse(self, args: list[str]):
        print("Parsing args")
        args = vars(self.parse_args(args))
        print(args)
        return args