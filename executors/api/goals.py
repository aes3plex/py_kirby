from base import *


def run():
    data = {"theFitCriterion": "TBC",
            "theConcerns": [],
            "theEnvironmentName": "Psychosis",
            "thePriority": "High",
            "theDefinition": "Anonymous clinical data"}

    return execute('post', get_url(__file__), data)


