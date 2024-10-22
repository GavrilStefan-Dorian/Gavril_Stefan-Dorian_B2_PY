def ex1(a: list[int], b: list[int]) -> list:
    a, b = set(a), set(b)
    return [a & b, a | b, a - b, b - a]

def ex2(text: str) -> dict[str, int]:
    return {c : text.count(c) for c in text}

def ex3(first_dict: dict, second_dict: dict) -> bool:
    if hasattr(first_dict, 'keys') and hasattr(second_dict, 'keys'):
        if first_dict.keys() != second_dict.keys():
            return False
        return all(ex3(first_dict[i], second_dict[i]) for i in first_dict)

    if hasattr(first_dict, '__iter__') and hasattr(second_dict, '__iter__'):
        return all(ex3(i, j) for i, j in zip(first_dict, second_dict))

    return not (first_dict != second_dict)

def ex4_build_xml_element(tag: str, content: str, **html_elements) -> str:
    result = '<%s'%tag
    for element in html_elements:
        result +=  ' %s = \"%s\" '%(element, html_elements[element])
    result += '> %s </%s>'%(content, tag)
    return result

def ex5(rules: set[tuple[str, ...]], d: dict[str, str]) -> bool:
    rules_keys = {rule[0] for rule in rules}
    dict_keys = set(d.keys())
    if rules_keys != dict_keys:
        print("Either key not present in dictionary, or in rules!")
        return False

    for rule in rules:
        value = d[rule[0]]
        if (not value.startswith(rule[1])
                or rule[2] not in value[len(rule[1]) + 1 : -len(rule[3]) if len(rule[3]) else None]
                or not value.endswith(rule[3])):
            return False
    return True

def ex6(lst: list) -> tuple[int, int]:
    new_set1 = set(lst)
    for x in new_set1:
        lst.remove(x)
    new_set2 = set(lst)
    return len(new_set2), len(new_set1 - new_set2)
    # [1,1,1,2,2,3,4,4,5,5,5,6] - 4 dupes, 2 uniques, 12 len
    # [1,2,3,4,5,6] - 6 len
    # [1,1,2,4,5,5]
    # [1,2,4,5]


def ex7(*sets: set) -> dict[str, set]:
    result = {}
    for i, set1 in enumerate(sets):
        for j, set2 in enumerate(sets):
            if i < j:
                key = "%s | %s"%(str(set1), str(set2))
                result[key] = set1 | set2
                key = "%s & %s"%(str(set1), str(set2))
                result[key] = set1 & set2
                key = "%s - %s" % (str(set1), str(set2))
                result[key] = set1 - set2
                key = "%s - %s" % (str(set2), str(set1))
                result[key] = set2 - set1
    return result

def ex8(mapping: dict[str, str]) -> list[str]:
    if "start" not in mapping:
        raise ValueError("start key not in mapping!")
    lst = []
    value = mapping["start"]
    while value not in lst:
        lst += value
        value = mapping[value]
    return lst

def ex9(*pos_args, **kwargs) -> int:
    return len([x for x in kwargs.values() if x in pos_args])


def main():
    print('=======EX1=======')
    print(ex1([1,2,3,4,5,6],[3,4,5,6,7,8]))

    print('=======EX2=======')
    print(ex2('Ana has apples.'))

    print('=======EX3=======')
    print(ex3({"a": 1,"b": {"x": 10, "y": 20},"c": [1, 2, 3]},
              {"a": 1,"b": {"x": 10, "y": 20},"c": [1, 2, 3]}))

    print('=======EX4=======')
    print(ex4_build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= "some-id"))

    print('=======EX5=======')
    print(ex5(rules={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
              d= {"key1": "come inside, it's too cold out", "key2": "start in the middle of winter", "key3": "this is not valid"}))

    print('=======EX6=======')
    print(ex6([1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6]))

    print('=======EX7=======')
    for pair in ex7({1,2}, {2,3}, {3,4}).items():
        print(pair)

    print('=======EX8=======')
    print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

    print('=======EX9=======')
    print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == '__main__':
    main()