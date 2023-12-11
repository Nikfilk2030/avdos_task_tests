from typing import List


class Paper:
    def __init__(self, coord, time) -> None:
        self.coord = int(coord)
        self.time = int(time)


def read_input(number, file) -> List[Paper]:
    coins: List[Paper] = []

    for _ in range(number):
        info = file.readline().split()
        if len(info) == 2:
            coins.append(Paper(coord=info[0], time=info[1]))
        else:
            raise Exception('Error on @pchelka_zh duty. test is incorrect')

    coins.sort(key=lambda x: x.coord)
    return coins


def find_time(coins: List[Paper]) -> str:
    # friendly reminder: you should write code too!
    pass


def evaluate_test_case(file, test_number: int):
    line = file.readline().strip().split()
    if not line:
        return False

    number = int(line[-1])
    coins = read_input(number, file)

    print(f"Testing Case #{test_number}...")
    expected_result = file.readline().strip()

    actual_result = find_time(coins)
    if actual_result != expected_result:
        print(f"Error in Case #{test_number}: Expected - {expected_result}, Actual - {actual_result}")
    else:
        print(f"Case #{test_number} Passed!")

    assert actual_result == expected_result

    return True


def main():
    with open("test.txt", "r") as file:
        test_number = 1
        while evaluate_test_case(file, test_number):
            test_number += 1


if __name__ == "__main__":
    main()
