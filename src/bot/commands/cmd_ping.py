from bot.commands.commands import CommandExecutor
from bot.models import Command


class CommandPing(CommandExecutor):
    def get_names(self):
        return ["commands", "cmds"]

    def get_help(self):
        return "Usage: pongと返します。\n" \
               "ping"

    def reply_backend(self, command: Command, _status: dict):
        return "pong"