from bot.commands.commands import CommandExecutor
from bot.models import Command, commands


class CommandCmds(CommandExecutor):
    def get_names(self):
        return ["commands", "cmds"]

    def get_help(self):
        return "Usage: コマンドの一覧を表示します。\n" \
               "--newlineを付加すると改行して表示します。\n" \
               "commands|cmds [--newline]"

    def reply_backend(self, command: Command, _status: dict):
        if command.contains_option("--newline"):
            return "コマンド一覧\n" + "\n".join(commands.keys())
        else:
            return "コマンド一覧(" + ", ".join(commands.keys()) + ")"