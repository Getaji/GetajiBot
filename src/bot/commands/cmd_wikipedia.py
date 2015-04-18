from bot.commands.commands import CommandExecutor
from bot.models import Command
from bot import wikipedia


class CommandWikipedia(CommandExecutor):

    def __init__(self):
        super().__init__(return_help_if_empty=True)

    def get_names(self):
        return ["wikipedia", "wp"]

    def get_help(self):
        return "Usage: 指定したwikipedia記事の概要を返します。\n" \
               "-langを指定するとその言語で取得します。\n" \
               "wikipedia|wp <記事名> [-lang <言語>]"

    def reply_backend(self, command: Command, _status: dict):
        name = "_".join(command.params)
        lang = command.get_prop("-lang", "ja")
        response = wikipedia.request_about(name, lang)
        if response is None:
            if lang is not "ja":
                return "言語「{0}」の記事「{1}」は見つかりませんでした。".format(lang, name)
            else:
                return "記事「{0}」は見つかりませんでした。".format(name)
        else:
            return "Wikipedia「{0}」".format(response)