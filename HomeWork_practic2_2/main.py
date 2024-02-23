from Vector import Vector


def readFile(a_file):
    vectors = []
    with open(a_file, 'r') as f:
        for line in f:
            try:
                data = line.split()
                data = list(map(float, data))
                vectors.append(Vector(data))
            except AssertionError:
                pass
        return vectors


def maxDimension(a_list):
    listOfChamps = [a_list[0]]
    for vector in a_list[1:]:
        if vector.dimension() > listOfChamps[0].dimension():
            listOfChamps.clear()
            listOfChamps.append(vector)
        elif vector.dimension() == listOfChamps[0].dimension():
            listOfChamps.append(vector)
    if len(listOfChamps) == 1:
        return listOfChamps[0]
    else:
        champ = listOfChamps[0]
        for vector in listOfChamps[1:]:
            if vector.length() < champ.length():
                champ = vector

        return champ


def maxLength(a_list):
    listOfChamps = [a_list[0]]
    for vector in a_list[1:]:
        if vector.length() > listOfChamps[0].length():
            listOfChamps.clear()
            listOfChamps.append(vector)
        elif vector.length() == listOfChamps[0].length():
            listOfChamps.append(vector)
    if len(listOfChamps) == 1:
        return listOfChamps[0]
    else:
        champ = listOfChamps[0]
        for vector in listOfChamps[1:]:
            if vector.dimension() < champ.dimension():
                champ = vector

        return champ


def meanLength(a_list):
    suma = 0
    for vector in a_list:
        suma += vector.length()
    return suma/len(a_list)


def vectorWithMaxComp(a_list):
    champs_list = [a_list[0]]
    for vector in a_list[1:]:
        if vector.max_comp() > champs_list[0].max_comp():
            champs_list.clear()
            champs_list.append(vector)
        if vector.max_comp() == champs_list[0].max_comp():
            champs_list.append(vector)
    if len(champs_list) == 0:
        return champs_list[0]
    else:
        champ = champs_list[0]
        for vector in champs_list[1:]:
            if vector.min_comp() < champ.min_comp():
                champ = vector
        return champ

def vectorWithMinComp(a_list):
    champs_list = [a_list[0]]
    for vector in a_list[1:]:
        if vector.min_comp() < champs_list[0].min_comp():
            champs_list.clear()
            champs_list.append(vector)
        elif vector.min_comp() == champs_list[0].min_comp():
            champs_list.append(vector)
        if len(champs_list) == 0:
            return champs_list[0]
        else:
            champ = champs_list[0]
            for vector in champs_list[1:]:
                if vector.max_comp() > champs_list[0].min_comp():
                    champ = vector
            return champ



if __name__ == '__main__':
    for file in ("input01.txt", "input02.txt", "input03.txt"):
        print(vectorWithMinComp((readFile(file))))