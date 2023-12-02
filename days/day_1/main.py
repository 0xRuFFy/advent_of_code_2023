
names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def helper_1(line: str) -> int:
   ds = list(filter(str.isdigit, line))
   first = int(ds[0])
   last = int(ds[-1])
   return int(f"{first}{last}")

def helper_2(line: str) -> int:
   ds = []
   for i, n in enumerate(line):
      if n.isdigit():
         ds.append(int(n))
      for j, name in enumerate(names):
         if line[i:].startswith(name):
            ds.append(j + 1)

   return int(f"{ds[0]}{ds[-1]}")


def main() -> None:
   with open("data/document.txt", "r") as file:
      lines = file.readlines()
      print(sum(map(helper_1, lines)))
      print(sum(map(helper_2, lines)))

if __name__ == "__main__":
    main()

