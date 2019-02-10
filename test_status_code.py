from requests import get
from hamcrest import assert_that, equal_to, not_

BASE_URL = 'http://httpbin.org/status/'


class TestStatusCode:
    def get_code(self, code):
        code = str(get(BASE_URL + code).status_code)
        return code

    def test_code_403(self):
        assert_that(self.get_code('403'), equal_to('403'))

    def test_code_123(self):
        assert_that(self.get_code('123456'), not_(equal_to('123456')))
