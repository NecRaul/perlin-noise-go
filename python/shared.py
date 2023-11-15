import os
import numpy
from result import Result


def read_directory(directory_path):
    file_names = [
        file_name
        for file_name in os.listdir(directory_path)
        if file_name.endswith(".txt")
    ]
    sorted_file_names = sorted(file_names)
    results = []
    for file_name in sorted_file_names:
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            total_seconds, count, seconds_array = read_file(file_path)
            result = Result(file_name, total_seconds, count, seconds_array)
            results.append(result)
    return results


def read_file(file_path):
    total_seconds = 0
    count = 0
    seconds_list = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            seconds = time_to_seconds(line.strip())
            seconds_list.append(seconds)
            total_seconds += seconds
            count += 1
    seconds_array = numpy.array(seconds_list)
    return total_seconds, count, seconds_array


def time_to_seconds(time_str):
    if "us" in time_str:
        microseconds = time_str.replace("us", "")
        total_seconds = float(microseconds) / 1000000
    elif "ms" in time_str:
        milliseconds = time_str.replace("ms", "")
        total_seconds = float(milliseconds) / 1000
    elif "m" in time_str:
        minutes, seconds = time_str.split("m")
        if "s" in seconds:
            seconds = seconds.replace("s", "")
            if "." in seconds:
                minutes = int(minutes)
                seconds = float(seconds)
                total_seconds = minutes * 60 + seconds
            else:
                seconds = int(seconds)
                total_seconds = minutes * 60 + seconds
        else:
            total_seconds = int(minutes) * 60
    elif "s" in time_str:
        seconds = time_str.replace("s", "")
        if "." in seconds:
            total_seconds = float(seconds)
        else:
            total_seconds = int(seconds)
    else:
        raise ValueError("Unrecognized time format")

    return total_seconds
