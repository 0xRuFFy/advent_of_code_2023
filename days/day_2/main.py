
TOTAL_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def helper_1(line: str) -> int:
    split = line.split(":")
    g_id = int(split[0].removeprefix("Game "))

    sets = split[1].split(";")
    for set in sets:
        local_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        cubes = set.split(",")
        for cube in cubes:
            s = cube.strip().split(" ")
            color, amount = s[1], s[0]
            local_cubes[color] += int(amount)

        print(local_cubes)
        if local_cubes["red"] > TOTAL_CUBES["red"] or local_cubes["green"] > TOTAL_CUBES["green"] or local_cubes["blue"] > TOTAL_CUBES["blue"]:
            return 0
        

    return g_id


def main() -> None:
    with open("data/games.txt", "r") as file:
        lines = file.readlines()[:100]
        print(sum(map(helper_1, lines)))


if __name__ == "__main__":
    main()
