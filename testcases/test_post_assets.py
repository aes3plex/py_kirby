import pytest
from allure import title, description, story, severity
from base import *
from executors.api import assets


@title("Add a new asset")
@description("Method for adding new asset")
@severity('Critical')
@story('HuaHana')
def test_run():
    with step("Base checks"):
        t = assets.run()
        base_assert(t)
        with step("Request data"):
            base_attachments(t)
