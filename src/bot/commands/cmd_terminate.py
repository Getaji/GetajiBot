from bot.commands.commands import CommandExecutor
from bot.models import Command


class CommandTerminate(CommandExecutor):

    from bot.utils import get_logger

    log = get_logger(__name__)

    def get_names(self):
        return ["terminate"]

    def get_help(self):
        return "Usage: 管理者専用。Botを終了する。\n" \
               "terminate"

    def reply_backend(self, command: Command, _status: dict):
        if _status["user"]["screen_name"] == "Getaji":
            from bot import twitters
            import sys

            twitters.post_bot_msg("終了します。")
            twitters.twitter.account.update_profile(name="Getaji@bot停止中")
            self.log.info("終了する。")
            sys.exit(0)
        else:
            return "権限がありません。"