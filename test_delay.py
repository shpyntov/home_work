from requests import get
from hamcrest import assert_that, less_than

BASE_URL = 'http://httpbin.org/delay/'
TOLERANCE_TIME = 0.5 # технологическая погрешность


class TestDelay:
    def get_resp_time_by_delay(self, delay):
        time = get(BASE_URL + str(delay)).elapsed.total_seconds()
        return time

    def test_delay_5_sec(self):
        delay = 5
        assert_that(self.get_resp_time_by_delay(delay), less_than(delay + TOLERANCE_TIME))

    def test_delay_15_sec(self):
        delay = 15
        assert_that(self.get_resp_time_by_delay(delay), less_than(delay + TOLERANCE_TIME))

    def test_delay_0_sec(self):
        delay = 0
        assert_that(self.get_resp_time_by_delay(delay), less_than(TOLERANCE_TIME))

    def test_delay_minus10_sec(self):
        delay = -10
        assert_that(self.get_resp_time_by_delay(delay), less_than(TOLERANCE_TIME))
