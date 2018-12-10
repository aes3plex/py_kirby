import pytest
from allure import title, description, story, severity
from base import *
from executors.api import vulnerabilities


@title("Get vulnerabilities")
@description("Method for getting vulnerabilities")
@severity('Critical')
@story('HuaHana')
def test_run():
    with step("Base checks"):
        t = vulnerabilities.run()
        base_assert(t)
        with step("Request data"):
            base_attachments(t)
