

open_list = ["(", "[", "{"]
close_list = [")", "]", "}"]

pair = {"(": ")", "{": "}", "[": "]"}
s = "([])"


def solution(s):
    if len(s) % 2 == 1:
        return False
    if s[0] not in open_list:
        return False
    input_list = [s[0]]
    for s_ in s[1:]:
        if s_ in open_list:
            input_list.append(s_)
        elif s_ in close_list:
            if len(input_list) == 0:
                return False
            last = input_list.pop()
            if pair[last] != s_:
                return False

    if len(input_list) != 0:
        return False
    else:
        return True


print(solution(s))
