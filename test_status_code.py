from requests import post
from hamcrest import assert_that, equal_to
import pytest

BASE_URL = 'http://httpbin.org/status/'


class TestStatusCode:
    def get_code(self, code):
        code = str(post(BASE_URL + code).status_code)
        return code

    @pytest.mark.parametrize("test_input,expected", [
        ("100", "100"),
        ("200", "200"),
        ("302", "302"),
        ("400", "400"),
        ("401", "401"),
        ("403", "403"),
        ("500", "500"),
        ("503", "503"),
        ("666", "400"),
        ("123456", "400")
    ])
    def test_code(self, test_input, expected):
        assert_that(self.get_code(test_input), equal_to(expected))
