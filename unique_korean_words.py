import os
import re
from glob import glob
from tqdm import tqdm


def contains_korean(text):
    return bool(re.search(r"[가-힣]", text))


CSV_FILE_DIRS = ["/Users/junhyung/Downloads/202505_주소DB_전체분-utf-8"]


def main():

    d = set()

    for csv_file_dir in CSV_FILE_DIRS:

        files = glob(os.path.join(csv_file_dir, "*.txt"))

        for file in tqdm(files):
            with open(file, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()

            for line in tqdm(lines):
                strings = line[:-1].split("|")

                for string in strings:
                    if contains_korean(string):
                        d.add(string)

            print(f"d word size : {len(d)}")

    # Save the unique Korean words to a file
    with open("unique_korean_words.txt", "w", encoding="utf-8") as f:
        for word in sorted(d):
            f.write(word + "\n")


if __name__ == "__main__":
    main()
