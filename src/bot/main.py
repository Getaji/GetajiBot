import sys

from bot.commands.cmd_ccc import CommandCCC
from bot.commands.cmd_dice import CommandDice
from bot.commands.cmd_help import CommandHelp
from bot.commands.cmd_info import CommandInfo
from bot.commands.cmd_kawo import CommandKawo
from bot.commands.cmd_ping import CommandPing
from bot.commands.cmd_select import CommandSelect
from bot.commands.cmd_shuffle import CommandShuffle
from bot.commands.cmd_commands import CommandCmds
from bot.commands.cmd_kc_mount import CommandKCMount
from bot.commands.cmd_terminate import CommandTerminate
from bot.commands.cmd_wikipedia import CommandWikipedia
from bot.commands.cmd_shuffle_words import CommandShuffleWords

import logging

from bot.commands.commands import add_command_executor
from bot.twitters import *
from bot.models import get_change
from bot.models import (
    on_status_event,
    on_unfavorite_event
)
from bot.unfavofavo import on_unfavofavo
from bot.mylogger import get_logger

# ######### Initialize logger ########## #
log = get_logger(__name__)

# ######### Register event observers ########## #
log.info("Registering event observers...")
on_status_event.add_observer(on_status)
on_unfavorite_event.add_observer(on_unfavofavo)

# ######### Register commands ########## #
log.info("Registering commands...")
add_command_executor(CommandCCC())
add_command_executor(CommandCmds())
add_command_executor(CommandDice())
add_command_executor(CommandHelp())
add_command_executor(CommandInfo())
add_command_executor(CommandKawo())
add_command_executor(CommandPing())
add_command_executor(CommandKCMount())
add_command_executor(CommandShuffle())
add_command_executor(CommandShuffleWords())
add_command_executor(CommandSelect())
add_command_executor(CommandTerminate())
add_command_executor(CommandWikipedia())

# ######### Initial Process ########## #
log.info("Connecting twitter...")
twitter.account.update_profile(name="Getaji@bot稼働中")
log.info("名前の変更に成功")
if "--silent" in sys.argv:
    log.info("サイレントモードのため起動ツイートは投稿しない。")
else:
    post_bot_msg("起動しました\n"
                 "直近の更新: " + get_change(True))
    log.info("botの起動ツイートに成功")

models.on_initialize_event.fire()


# ######### Main loop ########## #
def run():
    for status in twitter_stream.user():
        if "friends" in status:
            log.info("UserStreamの接続に成功")
            continue
        if "event" in status:
            if status["event"] == "unfavorite":
                on_unfavorite_event.fire(status)
            continue
        if "user" in status and "text" in status:
            try:
                on_status_event.fire(status)
            except Exception:
                import traceback
                import logging

                logging.error(traceback.format_exc())
                log.info("回復不可能なエラーが発生。終了する。")
                post_bot_msg("回復不可能なエラーが発生しました。終了します。")
                twitter.account.update_profile(name="Getaji@bot停止中")
                log.info("名前の変更に成功")
                import sys
                sys.exit(-1)