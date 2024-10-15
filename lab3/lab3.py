def ex1(n: int) -> list[int]:
    i, j, k = 0, 1, 0
    fib = []
    for _ in range(n):
        fib.append(i)
        i, j = j, i + j
    return fib

def ex2(nums: list[int]) -> list[int]:
    return [x for x in nums if len([y for y in range(2, x//2 + 1) if x%y == 0]) == 0]

def ex3(a: list[int], b: list[int]) -> tuple:
    a, b = set(a), set(b)
    return a & b, a | b, a - b, b - a

def ex4(notes: list[str], moves: list[int], start: int) -> list[str]:
    return [notes[(start := start + x) % len(notes)] for x in [0] + moves]

def ex5(matrix: list[list[int]]) -> list[list[int]]:
    return [[x if i <= j else 0 for (j, x) in enumerate(row)] for (i, row) in enumerate(matrix)]

def ex6(*lists: list, x: int) -> list[int]:
    total_list = [a for lst in lists for a in lst]
    result = []
    [result.append(a) for a in total_list if total_list.count(a) == x and a not in result]
    return result

def ex7(nums: list[int]) -> tuple[int, int]:
    palindromes = [x for x in nums if str(x) == str(x)[::-1]]
    return len(palindromes), max(palindromes)

def ex8(strings: list[str], x: int = 1, flag: bool = True) -> list[list[str]]:
    return [[char for char in string if (ord(char) % x == 0) == flag] for string in strings]

def ex9(matrix: list[list[int]]) -> list[tuple[int, int]]:


    # for (i, row) in enumerate(matrix):
    #     for (j, val) in enumerate(row):
    #         print([(matrix[k][j], i, j) for k in range(0, i) if matrix[k][j] >= val])

    return [(i, j) for (i, row) in enumerate(matrix) for (j, x) in enumerate(row)
            if len([matrix[k][j] for k in range(0, i) if matrix[k][j] >= x]) > 0]

def ex10(*lists: list) -> list[tuple[int, ...]]:
    max_len = max([len(lst) for lst in lists])
    return [tuple(lst[i] if i < len(lst) else None for lst in lists) for i in range(max_len)]

def ex11(str_tuples: list[tuple[str, str]]) -> list[tuple[str, str]]:
    str_tuples.sort(key = lambda x: x[1][2])
    return str_tuples

def ex12(words: list[str]) -> list[list[str]]:
    # # Method 1:
    # result = [[]]
    # i = 0
    # words.sort(key = lambda x: x[-2:])
    # last_two = words[0][-2:]
    # for word in words:
    #     if word[-2:] == last_two:
    #         result[i].append(word)
    #     else:
    #         i += 1
    #         last_two = word[-2:]
    #         result.insert(i, [])
    #         result[i].append(word)
    #
    # return result

    # # Method 2:
    return [[word for word in words if word[-2:] == key] for key in {word[-2:] for word in words}]



def main():
    print("======EX 1======")
    print(ex1(10))

    print("======EX 2======")
    print(ex2([1, 5, 10, 21, 17, 19, 23, 25]))

    print("======EX 3======")
    print(ex3([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]))

    print("======EX 4======")
    print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

    print("======EX 5======")
    for row in ex5([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]):
        print(row)

    print("======EX 6======")
    print(ex6([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x = 2))
    print(ex6([1,2,3], [2,3,"test",4],[4,5,6], [4,1, "test"], x = 2))


    print("======EX 7======")
    print(ex7([121, 122221, 123, 45, 545, 1]))

    print("======EX 8======")
    print(ex8(["test", "hello", "lab002"], x = 2, flag = False))

    print("======EX 9======")
    print(ex9([
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
    ]))

    print("======EX 10======")
    print(ex10( [1,2,3], [5,6,7,8], ["a", "b", "c"]))

    print("======EX 11======")
    print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

    print("======EX 12======")
    print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))

if __name__ == "__main__":
    main()