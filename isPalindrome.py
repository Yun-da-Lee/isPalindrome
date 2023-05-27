
def isPalindrome_my_code(num:int)->bool:
    if num < 0:
        return False
    else:
        toString = str(num)
        toString_pos = []
        for i in toString:
            toString_pos.append(i)
        toString_reverse=toString_pos[::-1]
        reversedString = "".join(str(i) for i in toString_reverse)
        if toString == reversedString:
            return True
        else:
            return False


def isPalindrome_best_memory_saving(num:int)->bool:
    x = str(num)
    if len(x) == 0:
        return True
    if len(x) == 1:
        return True
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True


def isPalindrome_best_runtime(num:int)->bool:
    x = str(num)
    return x == x[::-1]


if __name__ == "__main__":
    num = 121
    my_result = isPalindrome_my_code(num)
    best_runtime = isPalindrome_best_runtime(num)
    best_memory_saving = isPalindrome_best_memory_saving(num)
    print('result:',my_result)
    print('result:', best_runtime)
    print('result:', best_memory_saving)