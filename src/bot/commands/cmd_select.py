from bot.commands.commands import CommandExecutor
from bot.models import Command
from bot.utils import range_some
from random import randint


class CommandSelect(CommandExecutor):
    def get_names(self):
        return ["select"]

    def get_help(self):
        return "Usage: 複数の単語から指定個数ランダムで選択します。\n" \
               "--no-spacingを指定すると単語の間を詰めます。\n" \
               "select <個数> <単語1> <単語2> ... [--no-spacing]"

    def reply_backend(self, command: Command, _status: dict):
        if command.get_params_size() < 2:
            return self.get_help()
        elif not command.get_param(0).isdigit():
            return "個数は整数で指定してください。"
        else:
            quantity = int(command.get_param(0))
            if quantity < 1:
                return "個数は1以上で指定してください。"
            else:
                words = command.params[1:]
                size = len(words)
                selected_params = [words[randint(0, size - 1)] for x in range_some(quantity, 0)]
                delimiter = "" if command.contains_option("--no-spacing") else " "
                return "selected( {params} )".format(params=delimiter.join(selected_params))