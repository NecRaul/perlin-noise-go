import sys
import os
import numpy
import matplotlib.pyplot as plt
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
            plt.figure(figsize=(7, 7))
            for i in reversed(range(combined_array.shape[0])):
                plt.plot(combined_array[i], label=f"{2**(i+6)}")

            if "mt" and "io" in directory_path:
                plt.title("100 executions of multithreaded algorithm (with IO)")
            elif "mt" in directory_path:
                plt.title("100 executions of multithreaded algorithm (without IO)")
            elif "st" and "io" in directory_path:
                plt.title("100 executions of singlethreaded algorithm (with IO)")
            elif "st" in directory_path:
                plt.title("100 executions of singlethreaded algorithm (without IO)")

            plt.xlabel("Executions")
            plt.ylabel("Seconds")
            plt.legend()
            plt.show()
        else:
            print("Incorrect argument! Argument should either be mean or plot!")


if __name__ == "__main__":
    main()
