import numpy


class Result:
    def __init__(self, name, seconds, count, seconds_array):
        self.name = name.split("/")[-1].split(".")[0]
        self.seconds = seconds
        self.count = count
        self.seconds_array = seconds_array
        self.average = round(numpy.mean(seconds_array), 9)
