from bot.commands.commands import CommandExecutor
from bot.models import Command


class CommandDice(CommandExecutor):
    import re
    from random import randrange

    dice_pattern = re.compile("^(\d+)[dD](\d+)(([\\+\\-])(.+))?$")

    def __is_return_help_if_empty(self):
        return True

    def get_names(self):
        return ["dice"]

    def get_help(self):
        return 'Usage: TRPG書式でダイスを振ります。\n' \
               '個数を省略すると1個として扱います。\n' \
               'dice <個数D面数[+-固定値]>\n' \
               '例: dice 2D6+2 // 六面ダイスを2つ振り固定値2を加算する'

    def reply_backend(self, command: Command, _status: dict):
        dice = command.params[0]
        if not dice.startswith("d") or not dice.startswith("D"):
            dice = "1" + dice
        match_result = self.dice_pattern.match(dice)

        if match_result is None:
            return self.get_help()

        (quantity, surface_n, _, operator, fix_value) = match_result.groups()
        quantity = int(quantity)
        surface_n = int(surface_n)

        if operator is None and fix_value is not None:
            return "error:固定値の符号は+か-で指定してください。"
        if fix_value is not None and not fix_value.isdigit():
            return "error:固定値は整数で指定してください。"
        if operator is not None and fix_value is None:
            return "error:固定値は整数で指定してください。"
        fix_value = 0 if (fix_value is None) else int(fix_value)
        fix_value = 1 if (operator is "+") else -1 * fix_value

        if quantity < 1 or surface_n < 1:
            return "error:個数、面数は1以上を指定してください。"
        if quantity > 132:
            return "error:個数が多すぎます。"
        return dice + self.create_dice_result(quantity, surface_n, fix_value)

    def create_dice_result(self, quantity, surface_n, fix_value):
        results = [str(self.randrange(0, surface_n) + fix_value) for x in range(quantity)]
        return "(" + ",".join(results) + ")"