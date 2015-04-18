from bot.commands.commands import CommandExecutor


class CommandInfo(CommandExecutor):

    def __init__(self):
        from bot.models import version, environment, get_change
        self.version = version
        self.environment = environment
        self.change = get_change(True)

    def get_names(self):
        return ["info"]

    def get_help(self):
        return "Usage: botの情報を返します。\n" \
               "info"

    def reply_backend(self, command, _status):

        info_format = "Getaji-Bot v{ver}\n" \
                      "環境: {env}\n" \
                      "直近の更新: {recent}"
        return info_format.format(
            ver=self.version,
            env=self.environment,
            recent=self.change
        )