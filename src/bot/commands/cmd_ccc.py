from bot.commands.commands import CommandExecutor
from bot.models import Command


class CommandCCC(CommandExecutor):
    from random import shuffle

    ccc_chars = shuffle(["カ", "ク", "ケ", "コ"])
    ccc_format = "{0}ニ{1}リーム{2}ロッ{3}"

    def get_names(self):
        return ["ccc"]

    def get_help(self):
        return "Usage: カニクリームコロッケを作ります。こちらの診断と同じです。\n" \
               "http://shindanmaker.com/324852\n" \
               "ccc"

    def reply_backend(self, command: Command, _status: dict):
        self.shuffle(self.ccc_chars)
        return self.ccc_format.format(*self.ccc_chars)