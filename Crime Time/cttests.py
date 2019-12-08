# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Crime Time
# Term:         Winter 2019 


import crimetime

assert crimetime.Crime(1, "ROBBERY") == crimetime.Crime(1, "ROBBERY")
assert crimetime.Crime(2, "ROBBERY") != crimetime.Crime(1, "ROBBERY")
assert crimetime.Crime(11, "ROBBERY") != crimetime.Crime(1, "OTHER")

assert str(crimetime.Crime(1, "ROBBERY")) == \
    "{0}\t{1}\t{2}\t{3}\t{4}\n".format(1, "ROBBERY", None, None, None)
assert str(crimetime.Crime(14, "ROBBERY")) == \
    "{0}\t{1}\t{2}\t{3}\t{4}\n".format(14, "ROBBERY", None, None, None)
assert str(crimetime.Crime(13, "ROBBERY")) == \
    "{0}\t{1}\t{2}\t{3}\t{4}\n".format(13, "ROBBERY", None, None, None)

updated = [crimetime.Crime(5, "ROBBERY"), crimetime.Crime(6, "ROBBERY")]
crimetime.update_crimes(updated, ["5	Tuesday	01/06/2015	13:00", \
    "6	Wednesday	04/06/2015	1:00"])
assert updated[0].day_of_week == "Tuesday"
assert updated[0].month == "January"
assert updated[0].hour == "1PM"
assert updated[1].day_of_week == "Wednesday"
assert updated[1].month == "April"
assert updated[1].hour == "1AM"

crime1 = crimetime.Crime(1, "ROBBERY")
crime1.set_time("Wednesday", "3", "14")
assert crime1.month == "March"
assert crime1.day_of_week == "Wednesday"
assert crime1.hour == "2PM"

crime2 = crimetime.Crime(1, "ROBBERY")
crime2.set_time("Wednesday", "4", "0")
assert crime2.month == "April"
assert crime2.hour == "12AM"

crime2.set_time("Wednesday", "4", "12")
assert crime2.hour == "12PM"

crime2.set_time("Wednesday", "4", "2")
assert crime2.hour == "2AM"

assert crimetime.create_crimes([("150166475	ROBBERY	ROBBERY, ARMED WITH \
    A GUN"), "150018434	LARCENY / THEFT	GRAND THEFT FROM LOCKED AUTO", \
    "150018616	ROBBERY	ROBBERY ON THE STREET WITH A GUN"]) == \
    [crimetime.Crime(150166475, "ROBBERY"), crimetime.Crime(150018616, \
    "ROBBERY")]
assert crimetime.create_crimes(["4	LARCENY / THEFT	GRAND THEFT FROM \
    LOCKED AUTO"]) == []
assert crimetime.create_crimes(["5	ROBBERY	ROBBERY, ARMED WITH A GUN", \
    "0	LARCENY / THEFT	GRAND THEFT FROM LOCKED AUTO"]) == [crimetime.Crime(5, \
    "ROBBERY")]

assert crimetime.sort_crimes([crimetime.Crime(16, "ROBBERY"), \
    crimetime.Crime(15, "ROBBERY")]) == [crimetime.Crime(15, "ROBBERY"), \
    crimetime.Crime(16, "ROBBERY")]
assert crimetime.sort_crimes([crimetime.Crime(5, "ROBBERY"), crimetime.Crime( \
    1, "ROBBERY"), crimetime.Crime(6, "ROBBERY")]) == [crimetime.Crime(1, \
    "ROBBERY"), crimetime.Crime(5, "ROBBERY"), crimetime.Crime(6, "ROBBERY")]
assert crimetime.sort_crimes([crimetime.Crime(2, "ROBBERY"), crimetime.Crime( \
    1, "ROBBERY")]) == [crimetime.Crime(1, "ROBBERY"), crimetime.Crime(2, \
    "ROBBERY")]

assert crimetime.find_crime([crimetime.Crime(2, "ROBBERY"), crimetime.Crime(3, \
    "ROBBERY"), crimetime.Crime(4, "ROBBERY")], 3) == crimetime.Crime(3, \
    "ROBBERY")
assert crimetime.find_crime([crimetime.Crime(1, "ROBBERY"), crimetime.Crime(5, \
    "ROBBERY"), crimetime.Crime(7, "ROBBERY")], 1) == crimetime.Crime(1, \
    "ROBBERY")
assert crimetime.find_crime([crimetime.Crime(3, "ROBBERY"), crimetime.Crime(4, \
    "ROBBERY"), crimetime.Crime(5, "ROBBERY")], 5) == crimetime.Crime(5, \
    "ROBBERY")
assert crimetime.find_crime([crimetime.Crime(3, "ROBBERY"), crimetime.Crime( \
    4, "ROBBERY"), crimetime.Crime(5, "ROBBERY")], 50) is None

assert crimetime.get_mode(["Wednesday", "Wednesday", "Tuesday"]) == "Wednesday"
assert crimetime.get_mode(["4PM", "2PM", "2PM", "2PM", "2PM", "5PM"]) == "2PM"
assert crimetime.get_mode(["4PM", "4PM", "4PM", "2PM", "2PM", "2PM"]) == "4PM"








