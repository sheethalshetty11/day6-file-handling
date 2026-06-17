from datetime import datetime


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def count_lines(content):
    return len(content.splitlines())


def count_words(content):
    return len(content.split())


def count_characters(content):
    return len(content)


def display_report(filename, lines, words, chars):
    print("\n---- File Summary Report ----")
    print(f"File Name   : {filename}")
    print(f"Total Lines : {lines}")
    print(f"Total Words : {words}")
    print(f"Total Chars : {chars}")


def log_activity(filename, lines, words, chars):
    with open("activity_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(
            f"[{timestamp}] Processed {filename} - "
            f"Lines: {lines}, Words: {words}, Chars: {chars}\n"
        )


def main():
    filename = input("Enter file name: ")

    content = read_file(filename)

    if content is not None:
        lines = count_lines(content)
        words = count_words(content)
        chars = count_characters(content)

        display_report(filename, lines, words, chars)
        log_activity(filename, lines, words, chars)


if __name__ == "__main__":
    main()
