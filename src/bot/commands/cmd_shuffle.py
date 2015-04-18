from bot.commands.commands import CommandExecutor
from bot.models import Command


class CommandShuffle(CommandExecutor):

    from bot.utils import range_some, shuffle_f

    def __init__(self):
        super().__init__(return_help_if_empty=True)

    def get_names(self):
        return ["shuffle", "shf"]

    def get_help(self):
        return "Usage: 文字列をシャッフルします。\n" \
               "-timesを指定するとその回数分シャッフルします。\n" \
               "最大回数は100回です。\n" \
               "shuffle|shf <文字列> [-times <回数>]"

    def reply_backend(self, command: Command, _status: dict):
        times = command.get_prop("-times", "1")
        times = self.times_check(times)
        shuffled_text = self.shuffle_f_times(list(command.get_param(0)), times)
        return "".join(shuffled_text)

    def times_check(self, times: str):
        times = int(times) if times.isdigit() else 1
        if times < 1:
            times = 1
        elif 100 < times:
            times = 100
        return times

    def shuffle_f_times(self, lis: list, times: int):
        for i in self.range_some(times, 0):
            lis = self.shuffle_f(lis)
        return lis