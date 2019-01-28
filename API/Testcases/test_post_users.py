import pytest
from allure import title, description, story, severity
from API.base import *
from API.Executors.api import post_users


@title("post_users")
@description("Description")
@severity('Critical')
def test_run():
	with step("Base checks"):
		t = post_users.run()
		base_assert(t, 'post')
		with step("Request data"):
			base_attachments(t)
