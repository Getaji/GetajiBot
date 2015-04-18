__author__ = 'Margherita'


def request_about(title: str="ユリ熊嵐", lang: str="ja", is_uncy: bool=False):
    """
    指定したWikipediaの記事の概要を返します。
    :param title: 記事の名前
    :param is_uncy: アンサイクロペディアを使うか
    :return: 概要 存在しない場合はNone
    """
    import re

    try:
        if is_uncy:
            endpoint = "http://{lang}.uncyclopedia.info/api.php?"
        else:
            endpoint = "http://{lang}.wikipedia.org/w/api.php?"
        response = request_page(titles=title, prop="extracts", redirects=1, explaintext=1, lang=lang, endpoint=endpoint)
        content_json = response.json()
        pages_dict = content_json["query"]["pages"]
        if "-1" in pages_dict:
            return None
        about = str(list(pages_dict.values())[0]["extract"])
        about = about.split("\n", 1)[0]
        about = re.sub("<.+>", "", about)
    except Exception:
        import logging
        import traceback
        logging.error(traceback.format_exc())
        about = None

    return about


def request_page(fmt: str="json", action: str="query",
                 lang: str="ja", endpoint: str="http://{lang}.wikipedia.org/w/api.php?",
                 **kwargs):
    import requests
    kwargs["format"] = fmt
    kwargs["action"] = action
    return requests.get(endpoint.format(lang=lang), params=kwargs)