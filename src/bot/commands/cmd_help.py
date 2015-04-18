from bot.commands.commands import CommandExecutor
from bot.models import Command, helps


class CommandHelp(CommandExecutor):

    def __is_return_help_if_empty(self):
        return True

    def get_names(self):
        return ["help"]

    def get_help(self):
        return "Usage: コマンドのヘルプを表示します。\n" \
               "help <コマンド>"

    def reply_backend(self, command: Command, _status: dict):
        help_cmd_name = command.params[0]
        try:
            return helps[help_cmd_name]
        except KeyError:
            return "コマンド \"{0}\"は存在しません。".format(help_cmd_name)