def ex1():
    def calc_gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    print("======Ex. 1======")
    nums = input("Please enter numbers: ").split()
    nums = [int(num) for num in nums]
    gcd = calc_gcd(nums[0], nums[1])

    for num in nums[2:]:
        gcd = calc_gcd(gcd, num)

    print("GCD is: %d" % gcd)

def ex2():
    print("======Ex. 2======")

    s = input("Please input string: ").lower()
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1

    print("No. vowels: %d" % count)

def ex3():
    print("======Ex. 3======")

    s1, s2 = input("Please enter two strings: ").split()

    # print(s2.count(s1)) # doesn't count overlaps

    count = 0
    for i in range(0, len(s2) - len(s1) + 1):
        if s2[i:i + len(s1)] == s1:
            count += 1

    print(count)

def ex4():
    print("======Ex. 4======")

    s = input("Please input a string UppCamelCase: ")
    s_new = ""

    for i in s:
        if i.isupper():
            if i != s[0]:
                s_new += "_"
            s_new += i.lower()
        else:
            s_new += i

    print(s_new)

def ex5():
    print("======Ex. 5======")

    def is_palindrome(x: int) -> int:
        return x == int(str(x)[::-1])

    num = input("Please input num to check if palindrome: ")
    if type(num) != int:
        raise Exception("Please enter an integer")

    num = int(num)
    print(is_palindrome(num))


def ex6():
    print("======Ex. 6======")

    def extract_first_number(x: str) -> int:
        i = 0
        result = 0
        while not x[i].isdigit():
            i += 1
        while x[i].isdigit():
            result = result * 10 + int(x[i])
            i += 1
        return result

    s = "An apple is 123 USD wow inflation"
    print(extract_first_number(s))
    s = "abc123abc456"
    print(extract_first_number(s))


def ex7():
    print("======Ex. 7======")

    def bit_count(x: int) -> int:
        count = 0
        while x:
            count += x % 2
            x //= 2
        return count

    print(bit_count(24))


def ex8():
    print("======Ex. 8======")

    def word_count(x: str) -> int:
        return len(x.split())


    print(word_count("I have Python exam"))

def main():
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
    ex8()


if __name__ == "__main__":
    main()