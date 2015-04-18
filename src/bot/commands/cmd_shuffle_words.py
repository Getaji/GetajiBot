from bot.commands.commands import CommandExecutor
from bot.models import Command

from bot.utils import shuffle_f


class CommandShuffleWords(CommandExecutor):

    def __init__(self):
        super().__init__(return_help_if_empty=True)

    def get_names(self):
        return ["shuffle_words", "shf_w"]

    def get_help(self):
        return "Usage: 複数の単語の順序をシャッフルします。\n" \
               "--no-spacingを指定すると単語の間を詰めます。\n" \
               "shuffle_words|shf_w <単語1> <単語2> ... [--no-spacing]"

    def reply_backend(self, command: Command, _status: dict):
        delimiter = "" if command.contains_option("--no-spacing") else " "
        text = delimiter.join(shuffle_f(command.params))
        return "shuffled( " + text + " )"