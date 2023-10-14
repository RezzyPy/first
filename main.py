import heapq
import numpy

# stack - list
def reverse(starterFile, reversedFile):
    """
    Using a stack to implement this function by popping the element of the list and writing it to the destination file


    :param starterFile:Passed in file
    :param reversedFile: File written to.
    """
    input = []

    # open passed file and append each line to a list "line."
    with open(starterFile, "r") as f:
        for line in f:
            input.append(line)
    f.close()
    count = 0
    # Open a file to write to, while the length of the list is > 0. Pop an element and write it to the file.
    with open(reversedFile, "w") as f:
        while len(input) > 0:
            if count < 100000:
                f.write(input.pop())
                count += 1
            else:
                break


# USet - dictionary
def removeDuplication(originalFile, noDupeFile):
    """
    Using a dictionary, set the key equal to the value. Because there can not be duplicate keys in a dictionary this
    will get rid of duplicate lines in the file.

    :param originalFile:Passed in file.
    :param noDupeFile: File written to.
    """
    dict = {}
    # open file and use a dictionary, set key equal to value for every line. Strips \n from the file as well.
    with open(originalFile, "r") as f:
        for line in f:
            dict[line.strip("\n")] = [line.strip("\n")]
    f.close()
    # These keys are then written to a new file, free of duplicates.
    with open(noDupeFile, "w") as f:
        for i in dict.keys():
            f.write(i)
            f.write("\n")
    f.close()

#This class is used when two lines are of the same length and need to be sorted.
class Line:
    def __init__(self, value, length):
        self.value = value
        self.length = length

    def __lt__(self, other):
        return self.length < other.length


# priority queue
def sortByLengthLines(OGFile, sortedFile):
    """
    This function is implemented through a priority queue. First the file has duplicates removed like in the previous
    method. Then heapq sorts the function by size in ascending order.

    :param OGFile: Passed in file.
    :param sortedFile: File written to.
    """
    # remove duplicates like in removeDuplication()
    dict = {}

    with open(OGFile, "r") as f:
        for line in f:
            dict[line.strip("\n")] = [line.strip("\n")]
    f.close()
    with open("problem3dupe.txt", "w") as f:
        for i in dict.keys():
            f.write(i)
            f.write("\n")
    f.close()

    input = []

    #stores lines of the file in the list input[] after Line class does its function.
    with open('problem3dupe.txt', "r") as f:
        for lines in f:
            t = Line(lines, len(lines))
            input.append(t)
    f.close()
    # transforms list into a heap
    heapq.heapify(input)

    with open(sortedFile, "w") as f:
        while len(input) > 0:
            # heappop is used to pop the smallest value. This value is then written to the file. The file ascends from size shortest to longest.
            a = heapq.heappop(input).value
            f.write(a)
    f.close()


def main():
    reverse("input-1.txt", "Destination1.txt")
    removeDuplication("log.txt", "Destination2.txt")
    sortByLengthLines("log.txt", "Destination3.txt")

class List():
    def __init__(self, num):
        pass

class SSets():
    def __init__(self, num):
        pass

class USets():
    def __init__(self, num):
        pass


main()
