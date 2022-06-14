def bracket_validate(input_str):
    """(str) -> bool

    Return a bracket validation bool
    """
    opener = ["(", "[", "{"]
    closer = [")", "]", "}"]

    stack = []

    for i in input_str:
        if i in opener:
            if i == opener[0]:
                stack.append(closer[0])
            elif i == opener[1]:
                stack.append(closer[1])
            elif i == opener[2]:
                stack.append(closer[2])
        elif i in closer and not stack == []:
            if i != stack.pop():
                return "invalid"
            else:
                pass
        else:
            pass
    return "Valid use of brackets"


if __name__ != 'main':
    data = "nbd([{(hdn[njngf[]])}])"
    print(bracket_validate(data))
