from requests import get
from hamcrest import assert_that, equal_to

BASE_URL = 'http://httpbin.org/delay/'


class TestDelay:
    def get_resp_time_by_delay(self, delay):
        time = int(get(BASE_URL + str(delay)).elapsed.total_seconds())
        return time

    def check_delay(self, delay):
        if delay <= 0:
            assert_that(self.get_resp_time_by_delay(delay), equal_to(0))
        elif 0 < delay <= 10:
            assert_that(self.get_resp_time_by_delay(delay), equal_to(delay))
        elif delay > 10:
            assert_that(self.get_resp_time_by_delay(delay), equal_to(10))

    def test_delay_minus10_sec(self):
        self.check_delay(-10)

    def test_delay_0_sec(self):
        self.check_delay(0)

    def test_delay_5_sec(self):
        self.check_delay(5)

    def test_delay_15_sec(self):
        self.check_delay(15)
