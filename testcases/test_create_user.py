import pytest
from allure import title, description, story, severity
from base import *
from executors.api import users


@title("Creating user")
@description("Post method testing")
@severity('Critical')
@story('POOOST')
def test_run():
    with step("Now we posting"):
        t = users.run()
        base_assert(t)
        with step("Request data"):
            base_attachments(t)
