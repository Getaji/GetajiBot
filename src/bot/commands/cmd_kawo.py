__author__ = 'Margherita'

from bot.commands.commands import CommandExecutor


class CommandKawo(CommandExecutor):

    __kawo_chars = "┏┓┗┛━┃┣┫┻┳╋"

    def __init__(self):
        super().__init__(return_help_if_empty=True)

    def get_names(self):
        return ["kawo"]

    def get_help(self):
        return "Usage: ┃━┏┃語に翻訳します。半角空白を含むことも可能です。\n" \
               "kawo <文字列>"

    def reply_backend(self, command, _status):
        text = " ".join(command.params)
        return "".join(list(map((lambda x: self.__kawo_chars[ord(x) % 11]), text)))