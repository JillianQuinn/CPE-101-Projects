# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Moonlander
# Term:         Winter 2019


def main():
    show_welcome()
    altitude = get_altitude()
    fuel = get_fuel()
    time = 0
    gravity = 1.62
    velocity = 0.00
    display_state(time, altitude, velocity, fuel, 0)
    while (fuel > 0 and altitude != 0):
       fuel_rate = get_fuel_rate(fuel)
       time += 1
       fuel = update_fuel(fuel, fuel_rate)
       acceleration = update_acceleration(gravity, fuel_rate)
       altitude = update_altitude(altitude, velocity, acceleration)
       velocity = update_velocity(velocity, acceleration)
       display_state(time, altitude, velocity, fuel, fuel_rate)


# write other functions below this line


def show_welcome():
    print("")
    print("Welcome aboard the Lunar Module Flight Simulator")
    print("")
    print("   To begin you must specify the LM's initial altitude")
    print("   and fuel level.  To simulate the actual LM use")
    print("   values of 1300 meters and 500 liters, respectively.")
    print("")
    print("   Good luck and may the force be with you!")
    print("")


def get_altitude():
    altitude = input("Enter the initial altitude of the LM (in meters): ")
    altitude = float(altitude)
    while (altitude > 9999 or altitude < 1):
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        altitude = input("Enter the initial altitude of the LM (in meters): ")
        altitude = float(altitude)
    return altitude


def get_fuel():
    fuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
    fuel = int(fuel)
    while fuel <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
        fuel = int(fuel)
    return fuel


def get_fuel_rate(fuel):
    fuel_rate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")
    fuel_rate = int(fuel_rate)
    while (fuel_rate < 0 or fuel_rate > 9):
        print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
        fuel_rate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")
        fuel_rate = int(fuel_rate)
    while (fuel_rate > fuel):
        fuel_rate = fuel
    return fuel_rate


def display_state(time, altitude, velocity, fuel, fuel_rate):
    if time == 0:
        print("\nLM state at retrorocket cutoff")
    if fuel <= 0:
        while(altitude > 0.00):
            print("OUT OF FUEL - Elapsed Time: {0:3}".format(time), "Altitude: {0:7.2f}".format(altitude), "Velocity: {0:7.2f}".format(velocity))
            time += 1
            fuel_rate = 0
            altitude = update_altitude(altitude, velocity, -1.62)
            velocity = update_velocity(velocity, -1.62)
    if fuel > 0 or altitude == 0:
        if (altitude == 0):
            print("\nLM state at landing/impact")
        print("{0:>13}".format("Elapsed Time:"), "{0:>4} s".format(time) + "\n{0:>13}".format("Fuel:"), "{0:>4} l".format(fuel))
        print("{0:>13}".format("Rate:"), "{0:>4} l/s".format(fuel_rate))
        print("{0:>13}".format("Altitude:"), "{0:>7.2f} m".format(altitude))
        print("{0:>13}".format("Velocity:"), "{0:>7.2f} m/s".format(velocity) + "\n")
        if altitude == 0:
            display_landing_status(velocity)


def display_landing_status(velocity):
    if (velocity >= -1 and velocity <= 0):
        print("Status at landing - The eagle has landed!")
    elif (velocity < -1 and velocity > -10):
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif (velocity <= -10):
        print("Status at landing - Ouch - that hurt!")


def update_acceleration(gravity, fuel_rate):
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return acceleration


def update_altitude(altitude, velocity, acceleration):
    altitude = altitude + velocity + (acceleration / 2)
    if (altitude < 0):
        return 0
    return altitude


def update_velocity(velocity, acceleration):
    velocity = velocity + acceleration
    return velocity


def update_fuel(fuel, fuel_rate):
    fuel = fuel - fuel_rate
    return fuel


# no additional code below this line
if __name__ == "__main__":
    main()

