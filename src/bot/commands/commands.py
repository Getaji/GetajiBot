__author__ = 'Margherita'

from bot import twitters
from bot.models import Command
from bot.models import add_command, add_cmd_help


class CommandExecutor(object):

    def get_names(self):
        raise NotImplementedError

    def get_help(self):
        raise NotImplementedError

    def __is_return_help_if_empty(self):
        return False

    def execute(self, command: Command, _status: dict):
        if self.__is_return_help_if_empty() and command.is_empty_params():
            self.reply(self.get_help(), _status)
            return

        self.reply(self.reply_backend(command, _status), _status)

    def reply_backend(self, command: Command, _status: dict):
        return ""

    def reply(self, text: str, _status: dict):
        twitters.reply(text, _status["user"], _status["id"])


def add_command_executor(executor: CommandExecutor):
    for name in executor.get_names():
        add_command(name, executor.execute)
        add_cmd_help(name, executor.get_help())