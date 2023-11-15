class Result:
    def __init__(self, name, seconds, count):
        self.name = name.split("/")[-1].split(".")[0]
        self.seconds = seconds
        self.count = count
        self.average = seconds / count
