import re

class Extension:
    def __init__(self, matches):
        self.matches = matches

    def extension(self):
        match self.matches:
            case ".zip":
                return "application/zip"
            case ".gif":
                return "image/gif"
            case ".jpeg" | ".jpeg":
                return "image/jpeg"
            case ".png":
                return "image/png"
            case ".pdf":
                return "application/pdf"
            case ".txt":
                return "text/plain"
            case ".pdf":
                return "application/pdf"
            case ".zip":
                return "application/zip"
            case _:
                return "application/octet-stream"



def main():
    file = get_extension(get_input("File name: "))
    print(file.extension())


def get_input(inp):
    return input(inp).lower().strip()


def get_extension(file):
    if matches := re.search(r"^.+(\.[a-z]{3,4})$", file):
        return Extension(matches.group(1))
    else:
        raise ValueError("Invalid file format")


main()
