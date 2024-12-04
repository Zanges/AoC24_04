from Task1 import load_data


def is_center_of_x_mas(data: list[list[str]], x: int, y: int) -> bool:
    """
    check if the given point is the center of an X-Mas

    :param data: data is a 2D list of characters
    :param x: x is the x-coordinate of the point
    :param y: y is the y-coordinate of the point

    :return: True if the given point is the center of an X-Mas, False otherwise
    """
    if data[y][x] != "A":
        return False
    if x == 0 or x == len(data[0])-1 or y == 0 or y == len(data)-1:
        return False
    if (data[y-1][x-1] == "M" and data[y+1][x+1] == "S") or (data[y-1][x-1] == "S" and data[y+1][x+1] == "M"):
        if (data[y-1][x+1] == "M" and data[y+1][x-1] == "S") or (data[y-1][x+1] == "S" and data[y+1][x-1] == "M"):
            return True
    return False


def count_x_mas(data: list[list[str]]) -> int:
    """
    count the number of X-Mas in the data
    """
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if is_center_of_x_mas(data, x, y):
                count += 1
    return count


def main():
    data = load_data("input.txt")
    # data = load_data("dummy_data.txt")
    print(count_x_mas(data))


if __name__ == "__main__":
    main()