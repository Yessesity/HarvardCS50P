from charwrite import CharWrite
import csv


def main():
    binary = CharWrite.has_char()
    char = CharWrite.get_name(binary)
    char.write(binary)
    sheet = read(char)
    print(sheet)
    
            
def read(char):
    sheet = []
    with open(f"charsheet_{char}.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            sheet.append(row)
    return sheet


if __name__ == "__main__":
    main()
