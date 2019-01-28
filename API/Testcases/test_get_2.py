import pytest
from allure import title, description, story, severity
from base import *
from Executors.api.users import get_2


@title("get_2")
@description("Description")
@severity('Critical')
def test_run():
	with step("Base checks"):
		t = get_2.run()
		base_assert(t, 'get')
		with step("Request data"):
			base_attachments(t)
