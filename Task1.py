def load_data(file_path: str) -> list[list[str]]:
    """
    Load data from a file and return a 2D list of characters

    :param file_path: the path to the file

    :return: a 2D list of characters
    """
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def build_vertical_lines(data: list[list[str]]) -> list[str]:
    """
    Build vertical lines from the data
    """
    lines = [""] * len(data[0])
    for row in data:
        for i, column in enumerate(row):
            lines[i] += column
    return lines


def build_left_to_top_diagonal_lines(data: list[list[str]]) -> list[str]:
    """
    Build left-to-top diagonal lines from the data
    """
    lines = []
    for i in range(len(data)):
        line = ""
        for j in range(i, -1, -1):
            line += data[j][i-j]
        lines.append(line)
    for i in range(1, len(data[0])):
        line = ""
        for j in range(len(data)-1, i-1, -1):
            line += data[j][i+len(data)-1-j]
        lines.append(line)
    return lines


def build_top_to_right_diagonal_lines(data: list[list[str]]) -> list[str]:
    """
    Build top-to-right diagonal lines from the data
    """
    lines = []
    for i in range(len(data[0]), -1, -1):
        line = ""
        for j in range(i, len(data[0])):
            line += data[j-i][j]
        lines.append(line)
    for i in range(1, len(data)):
        line = ""
        for j in range(i, len(data)):
            line += data[j][j-i]
        lines.append(line)
    return lines[1:]


def build_lines(data: list[list[str]]) -> list[str]:
    """
    Build lines from the data

    :param data: a 2D list of characters

    :return: a list of lines
    """
    lines = []
    for row in data:
        lines.append("".join(row))
    lines += build_vertical_lines(data)
    lines += build_left_to_top_diagonal_lines(data)
    lines += build_top_to_right_diagonal_lines(data)
    # Add the revers of each line
    lines += [line[::-1] for line in lines]
    return lines


def count_occurrences(lines: list[str], word: str) -> int:
    """
    Count the number of occurrences of a word in the lines

    :param lines: a list of lines
    :param word: the word to search for

    :return: the number of occurrences of the word
    """
    return sum([line.count(word) for line in lines])


def main():
    data = load_data("input.txt")
    data = load_data("dummy_data.txt")
    lines = build_lines(data)
    print(count_occurrences(lines, "XMAS"))

if __name__ == "__main__":
    main()