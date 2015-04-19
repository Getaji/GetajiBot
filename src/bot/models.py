__author__ = 'Margherita'

import re
import sys
from bot.event import EventMutable

# commands and helps
commands = {}
helps = {}

on_status_event = EventMutable()
on_unfavorite_event = EventMutable()
on_initialize_event = EventMutable()


version = "0.2.0"
environment = "local" if "--locally" in sys.argv else "remote"
recent_change = "あんふぁぼふぁぼ～\n" \
                "\";;\"以降をコメントアウトするように。\n" \
                "shuffleコマンドに回数指定パラメータ-timesを追加。"


def get_change(newline_if_newline: bool=False):
    return (("\n" if newline_if_newline else "") + recent_change).replace("\n", "\n・")


def add_command(name: str, consumer):
    commands[name] = consumer


def add_cmd_help(name: str, help_str: str):
    helps[name] = help_str

pattern_reply = re.compile("^@[\w]+$")
pattern_hashtag = re.compile("^[#＃][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー]+$")


def parse2command(string: str):
    split_string = string.split(" ")
    return Command(split_string[0], split_string[1:])


class Command:
    def __init__(self, name: str, params):
        self.name = name

        b_params = []           # 仮パラメータ
        b_options = []          # 仮オプション
        prev_key = None         # 直前がプロパティのキーだったか
        b_props = {}            # 仮プロパティ
        in_quote_params = []    # ダブルクォートで括られたまだ格納されていないパラメータ
        is_quoted_prev = False  # 前回までにクォートが開始されているか
        is_commented = False    # 直前がコメントアウトか
        for param in params:
            # comment-out
            if is_commented:
                break

            try:
                comment_i = param.index(";;")
                param = param[:comment_i]
                is_commented = True
                if param == "":
                    break
            except ValueError:
                pass

            # off reply and hashtag
            if pattern_reply.match(param):
                param = "@." + param[1:]
            elif pattern_hashtag.match(param):
                param = "#." + param[1:]

            # quote
            if param.startswith("\""):
                is_quoted_prev = True
            if is_quoted_prev:
                in_quote_params.append(param)
                if param.endswith("\""):
                    from bot.utils import trim
                    param = " ".join(in_quote_params)
                    param = trim(param, 1, 1)
                    is_quoted_prev = False
                else:
                    continue

            # option and property
            if param.startswith("--"):
                b_options.append(param)
            elif prev_key is not None:
                b_props[prev_key] = param
                prev_key = None
            elif param.startswith("-"):
                prev_key = param
            else:
                b_params.append(param)

        if prev_key is not None:
            b_props[prev_key] = None

        self.params = b_params
        self.options = b_options
        self.props = b_props

    def get_param(self, index: int, default_value: object=None):
        try:
            return self.params[index]
        except IndexError:
            return default_value

    def __getitem__(self, item):
        return self.get_prop(item)

    def get_prop(self, key: str, default: object=None):
        try:
            return self.props[key]
        except KeyError:
            return default

    def contains_option(self, option: str):
        return option in self.options

    def is_empty_params(self):
        return len(self.params) == 0

    def get_params_size(self):
        return len(self.params)