import pytest
from allure import title, description, story, severity
from base import *
from executors.api import goals


@title("Add a new goal")
@description("Method for adding new goal")
@severity('Critical')
@story('HuaHana')
def test_run():
    with step("Base checks"):
        t = goals.run()
        base_assert(t)
        with step("Request data"):
            base_attachments(t)
