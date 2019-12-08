# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Moonlander
# Term:         Winter 2019


import moonlander

assert moonlander.update_acceleration(1.62, 5) == 0
assert moonlander.update_acceleration(10, 2) == -6
assert moonlander.update_acceleration(10, 9) == 8.0

assert moonlander.update_altitude(500.00, 1.0, 2) == 502.0
assert moonlander.update_altitude(200.00, 2.0, 4) == 204.0
assert moonlander.update_altitude(600.00, 4.0, 8) == 608.0
assert moonlander.update_altitude(-300.00, 4.0, 8) == 0.0

assert moonlander.update_velocity(2.0, 1.0) == 3.0
assert moonlander.update_velocity(3.0, 5.0) == 8.0
assert moonlander.update_velocity(5.2, 8.5) == 13.7

assert moonlander.update_fuel(400, 4) == 396
assert moonlander.update_fuel(356, 6) == 350
assert moonlander.update_fuel(673, 3) == 670
