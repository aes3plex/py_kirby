import pytest
from allure import title, description, story, severity
from base import *
from executors.api import epics


@title("Get epics")
@description("Method for getting epics")
@severity('Critical')
@story('HuaHana')
def test_run():
    with step("Base checks"):
        t = epics.run()
        base_assert(t)
        with step("Request data"):
            base_attachments(t)
