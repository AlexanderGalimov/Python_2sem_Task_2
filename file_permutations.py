def read_two_dimensional_list(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    f.close()

    return data


def write_two_dimensional_list(data, file):
    f = open(file, 'w')
    for i in range(len(data)):
        for j in range(len(data[0])):
            f.write(str(data[i][j]) + " ")
        f.write("\n")
    f.close()
