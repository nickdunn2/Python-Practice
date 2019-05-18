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


print(convert_time_to_military(midnight_time))
print(convert_time_to_military(noon_time))
print(convert_time_to_military(am_time))
print(convert_time_to_military(pm_time))
print(convert_time_to_military(bad_time))
