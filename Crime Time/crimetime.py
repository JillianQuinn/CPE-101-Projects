# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Crime Time
# Term:         Winter 2019 


class Crime:

    def __init__(self, crime_id, category):
        self.crime_id = crime_id
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        return self.crime_id == other.crime_id

    def __repr__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}\n".format(self.crime_id, self.category, \
            self.day_of_week, self.month, self.hour)

    def set_time(self, day_of_week, month, hour):
        self.day_of_week = day_of_week
        month_list = ["January", "February", "March", "April", "May", "June", \
            "July", "August", "September", "October", "November", "December"]
        self.month = month_list[int(month) - 1]
        if int(hour) == 0:
            self.hour = "12AM"
        elif int(hour) < 12:
            self.hour = "{0}AM".format(int(hour))
        else:
            if int(hour) == 12:
                self.hour = "12PM"
            else:
                self.hour = "{0}PM".format(int(hour) - 12)


def main():
    fp = open("crimes.tsv", "r")
    lines = fp.readlines()
    fp.close()
    crimes = create_crimes(lines[1:])
    sorted_crimes = sort_crimes(crimes)
    fp = open("times.tsv", "r")
    time_lines = fp.readlines()
    fp.close()
    update_crimes(sorted_crimes, time_lines[1:])
    fp = open("robberies.tsv", "w")
    fp.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")
    for i in sorted_crimes:
        fp.write("{0}".format(str(i)))
    fp.close()
    day_list = [i.day_of_week for i in sorted_crimes]
    month_list = [i.month for i in sorted_crimes]
    hour_list = [i.hour for i in sorted_crimes]
    print("{0:>31}{1}".format("NUMBER OF PROCESSED ROBBERIES: ", \
        len(sorted_crimes)))
    print("{0:>31}{1}".format("DAY WITH MOST ROBBERIES: ", \
        get_mode(day_list)))
    print("{0:>31}{1}".format("MONTH WITH MOST ROBBERIES: ", \
        get_mode(month_list)))
    print("{0:>31}{1}".format("HOUR WITH MOST ROBBERIES: ", \
        get_mode(hour_list)))


def create_crimes(lines):
    crime_list = []
    id_list = []
    full_crime = []
    for i in lines:
        full_crime = i.strip("\n").split("\t")
        ID = int(full_crime[0])
        if "ROBBERY" == full_crime[1] and ID not in id_list:
                crime_list.append(Crime(ID, full_crime[1]))
                id_list.append(ID)
    return crime_list


def sort_crimes(crimes):
    for i in range(len(crimes)):
        smallest = i
        for j in range(i + 1, len(crimes)):
            if crimes[smallest].crime_id > crimes[j].crime_id:
                smallest = j
        crime_i = crimes[i]
        crimes[i] = crimes[smallest]
        crimes[smallest] = crime_i
    return crimes


def update_crimes(crimes, lines):
    for time in lines:
        new_time = time.strip("\n").split("\t")
        ID = int(new_time[0])
        found_crime = find_crime(crimes, ID)
        if found_crime is not None:
            date = new_time[2].split("/")
            time_split = new_time[3].split(":")
            found_crime.set_time(new_time[1], int(date[0]), int(time_split[0]))


def find_crime(crimes, crime_id):
    low = 0
    high = len(crimes) - 1
    while low <= high:
        half = (low + high) // 2
        if int(crimes[half].crime_id) == crime_id:
            return crimes[half]
        elif int(crimes[half].crime_id) > crime_id:
            high = half - 1
        else:
            low = half + 1
    return None


def get_mode(List):
    mode = List[0]
    for i in List:
        if List.count(i) > List.count(mode):
            mode = i
    return mode


if __name__ == "__main__":
    main()

