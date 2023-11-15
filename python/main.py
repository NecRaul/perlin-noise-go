import sys
import os
import shared


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py directory_path")
    else:
        directory_path = sys.argv[1]
        if not os.path.isdir(directory_path):
            print("Invalid directory path.")
            return
        results = shared.read_directory(directory_path)
        for result in results:
            print(f"Mean average in seconds for size {result.name}: {result.average}")


if __name__ == "__main__":
    main()
