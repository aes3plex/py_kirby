from base import *


def run():
    data = {"theName" : "Psychosis",
            "theProperties" : {"name": "Confidentiality",
                               "value": "Low",
                               "rationale": "Clinical data is fully anonymised"}}

    return execute('post', get_url(__file__), data)
