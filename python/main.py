import sys
import os
import numpy
import shared


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py directory_path mean/plot")
    else:
        directory_path = sys.argv[1]
        if not os.path.isdir(directory_path):
            print("Invalid directory path.")
            return
        argument = sys.argv[2]
        results = shared.read_directory(directory_path)

        if argument.lower() == "mean":
            for result in results:
                print(
                    f"Mean average in seconds for size {result.name}: {result.average}"
                )
        elif argument.lower() == "plot":
            max_length = max(len(result.seconds_array) for result in results)

            padded_arrays = [
                numpy.pad(
                    result.seconds_array,
                    (0, max_length - len(result.seconds_array)),
                    "constant",
                    constant_values=numpy.nan,
                )
                for result in results
            ]

            combined_array = numpy.vstack(padded_arrays)

            # TODO Add matploblib functionality
        else:
            print("Incorrect argument! Argument should either be mean or plot!")


if __name__ == "__main__":
    main()
