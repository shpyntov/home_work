from requests import get
from hamcrest import assert_that, equal_to
from random import randint
import pytest

BASE_URL = 'http://httpbin.org/delay/'


class TestDelay:
    def get_delay(self, requested_delay):
        time = int(get(BASE_URL + str(requested_delay)).elapsed.total_seconds())
        return time

    @pytest.mark.parametrize("requested_delay,expected_delay", [
        (randint(-20, -1), 0),
        (0, 0),
        (5, 5),
        (randint(11, 20), 10)
    ])
    def test_delay(self, requested_delay, expected_delay):
        assert_that(self.get_delay(requested_delay), equal_to(expected_delay))
