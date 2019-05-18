import unittest

midnight_time = '12:04:22AM'
noon_time = '12:25:52PM'
am_time = '05:15:35AM'
pm_time = '07:05:45pm'
bad_time = '431431431'


def convert_time_to_military(time):
    time = time.strip()
    no_am_pm = time[:-2]
    am_pm = time[-2:]
    if am_pm.upper() != 'AM' and am_pm.upper() != 'PM':
        return "Please provide a valid AM or PM time."
    h, m, s = map(int, no_am_pm.split(':'))
    h = h % 12 + ((am_pm.upper() == 'PM') * 12)

    return ('%02d:%02d:%02d') % (h, m, s)


class ActivityTests(unittest.TestCase):
    def test_midnight_time(self):
        """Should change 12 to 00 when it's the midnight hour"""
        self.assertEqual(convert_time_to_military(midnight_time), '00:04:22')

    def test_noon_time(self):
        """Should keep 12 as is when it's the noon hour"""
        self.assertEqual(convert_time_to_military(noon_time), '12:25:52')

    def test_am_time(self):
        """Should not add 12 hours when it's AM"""
        self.assertEqual(convert_time_to_military(am_time), '05:15:35')

    def test_pm_time(self):
        """Should add 12 hours when it's PM"""
        self.assertEqual(convert_time_to_military(pm_time), '19:05:45')

    def test_bad_time(self):
        """Should indicate an error when input string doesn't end with AM or PM."""
        self.assertEqual(convert_time_to_military(bad_time),
                         'Please provide a valid AM or PM time.')


unittest.main()
