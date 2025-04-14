
def read_in(path):
    lst_one, lst_two = [], []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            b = line.split(" ")
            lst_one.append(int(b[0]))
            lst_two.append(int(b[-1]))

    return lst_one, lst_two


def find_distance():
    lst_one, lst_two = read_in("dayOneInput.txt")
    lst_one.sort()
    lst_two.sort()

    distance = 0
    for i in range(len(lst_one)):
        distance += abs(lst_one[i] - lst_two[i])
    return distance


print(find_distance())
