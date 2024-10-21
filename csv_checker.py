import glob
import os
import csv

def is_uft_8_withBOM(filename:str):
    bt = None
    with open(filename, mode='rb') as file:
        bt = file.read(3)

    return bt == b'\xef\xbb\xbf'

def get_lines(filename:str):
    lines = 0
    with open(filename, mode='r', encoding="utf-8") as file:
        lines = [1 for i in csv.reader(file) if len(i) > 0]

    return sum(lines) - 1

def main():
    csv_files = glob.glob('./input/**/*.csv', recursive=True)

    res = [["file name", "isUft-8WithBOM", "lines"]]
    warns = []

    print("file name, isUft-8WithBOM, lines")
    for csv_file in csv_files:
        lines = 0
        is_withBom = is_uft_8_withBOM(csv_file)
        if is_withBom:
            lines = get_lines(csv_file)
        else:
            warns.append(f"!!!!!!!!!!! {csv_file} is NOT UTF-8 with BOM !!!!!!!!!!!")

        print(f"{csv_file},{is_withBom},{lines}")
        res.append([csv_file, is_withBom, lines])

    with open("./output.csv", mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(res)
    print("\n")
    [print(i) for i in warns]

if __name__ == "__main__":
    main()