from bot.commands.commands import CommandExecutor
from bot.kc_db import aircraft_mounts
from bot.models import Command


class CommandKCMount(CommandExecutor):

    def __init__(self):
        super().__init__(return_help_if_empty=True)

    def get_names(self):
        return ["kc_mount"]

    def get_help(self):
        return "Usage: 艦載機搭載数を返します。複数指定可能です。\n" \
               "kc_mount <艦娘名1> <艦娘名2> ..."

    def reply_backend(self, command: Command, _status: dict):
        if command.get_params_size() == 1:
            return self.__mount_single(command)
        else:
            return self.__mount_multi(command)

    def __mount_single(self, command: Command):
        fleetgirl_name = command.get_param(0)
        mounts = aircraft_mounts.get(fleetgirl_name, None)
        if mounts is None:
            return "「" + fleetgirl_name + "」" + "は存在しないか登録されていない艦娘です"
        else:
            return fleetgirl_name + str(mounts)

    def __mount_multi(self, command: Command):
        post_text = "複数艦娘の搭載数"
        for fleetgirl_name in command.params:
            mounts = aircraft_mounts.get(fleetgirl_name, None)
            if mounts is None:
                text = fleetgirl_name + "(存在しないか未登録)"
            else:
                text = fleetgirl_name + str(mounts)
            post_text += "\n" + text
        return post_text