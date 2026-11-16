from typing import List

def read_integers() -> List[int]:
    num = input()
    numbers = num.split(",")
    arr = []
    for numb in numbers:
        arr.append(int(numb))

    return arr    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
