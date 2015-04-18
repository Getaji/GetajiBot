from random import randint
from bot.twitters import reply

unfavorite_face = (
    "ヾ(╯◔ ◡ ◔╰)ﾉ”",
    "(ノ)・ω・(ヾ)",
    "٩(๑╹ヮ╹)۶",
    "ヾ(╯⊙ ⊱ ⊙╰ )ﾉ”",
)


def on_unfavorite(status: dict):
    face = unfavorite_face[randint(0, len(unfavorite_face) - 1)]
    text = "あんふぁぼふぁぼ～{face}".format(face=face)
    status_id = status["target_object"]["id"]
    reply(text, status["source"], status_id)