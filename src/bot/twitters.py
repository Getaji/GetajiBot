from twitter import *
from bot import models
from bot.mylogger import get_logger
from datetime import datetime
from pytz import timezone
import json

# Logger
log = get_logger(__name__)

# Twitter connection
config = json.load(open("config.json"))
__auth = OAuth(
    config["token"], config["token_secret"],
    config["consumer_key"], config["consumer_secret"])

twitter_stream = TwitterStream(
    auth=__auth,
    domain="userstream.twitter.com")

twitter = Twitter(auth=__auth)


# Functions
def create_reply_text(text: str, user: dict):
    return "@" + user["screen_name"] + " " + text


def reply(text: str, user: dict, in_reply_to: dict=-1):
    joined_text = create_reply_text(text, user)
    if len(joined_text) > 140:
        joined_text = joined_text[:137] + "..."
    twitter.statuses.update(
        status=joined_text,
        in_reply_to_status_id=in_reply_to
    )
    log.info("Replied: {text}".format(
        user=user["screen_name"],
        text=joined_text
    ))


def post_bot_msg(msg: str):
    twitter.statuses.update(status="[BOT][{time}] {msg}".format(
        time=get_formatted_time(),
        msg=msg
    ))
    log.info("Posted bot message:{text}".format(text=msg))


# Time
now = datetime.now(timezone("Asia/Tokyo"))


def get_formatted_time():
    return now.strftime("%Y/%m/%d-%H:%M:%S")


# Inner methods
def on_command(_status: dict):
    split_text = _status["text"].split(" ")
    command = models.Command(split_text[1], split_text[2:])

    consumer = models.commands.get(command.name)
    if consumer is not None:
        log.info("========================================")
        log.info("Executing command: " + str(split_text))
        consumer(command, _status)
        log.info("Executed command: " + str(split_text))
        log.info("----------------------------------------")


def on_status(_status: dict):
    text = _status["text"]
    if text.startswith("@Getaji") and not ("( ´◔ ‸◔`)" in _status["source"]):
        on_command(_status)