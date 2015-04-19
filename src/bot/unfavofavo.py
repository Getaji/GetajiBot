from random import randint
from bot.twitters import reply

unfavorite_face = (
    "ヾ(╯◔ ◡ ◔╰)ﾉ”",
    "(ノ)・ω・(ヾ)",
    "٩(๑╹ヮ╹)۶",
    "ヾ(╯⊙ ⊱ ⊙╰ )ﾉ”",
)


def on_unfavofavo(status: dict):
    status_id = status["target_object"]["id"]
    reply(get_unfavo_text(), status["source"], status_id)


def get_unfavo_text():
    return "あんふぁぼふぁぼ～{face}".format(face=random_face())


def random_face():
    return unfavorite_face[randint(0, 3)]