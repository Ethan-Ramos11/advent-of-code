
def read_in(path):
    lst_one, lst_two = [], []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            b = line.split(" ")
            lst_one.append(int(b[0]))
            lst_two.append(int(b[-1]))

    return lst_one, lst_two


def find_distance(file_path):
    lst_one, lst_two = read_in(file_path)
    lst_one.sort()
    lst_two.sort()

    distance = 0
    for i in range(len(lst_one)):
        distance += abs(lst_one[i] - lst_two[i])
    return distance


def generate_keys(lst):
    dict = {}
    for num in lst:
        if num not in dict:
            dict[num] = 0
    return dict


def find_similarity_score(file_path):
    lst_one, lst_two = read_in(file_path)
    occurence = generate_keys(lst_one)
    for num in lst_two:
        if num in occurence:
            occurence[num] += 1
    score = 0
    for n, val in occurence.items():
        score += n * val
    return score


print(find_distance("dayOneInput.txt"))
print(find_similarity_score("dayOneInput.txt"))
