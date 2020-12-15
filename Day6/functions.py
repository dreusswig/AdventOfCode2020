def countDifferentLetters(string):
    appearances = []
    count = 0
    for c in string:
        if c in appearances:
            continue
        else:
            appearances.append(c)
            count += 1
    return appearances, count

def countSameLetters(array):
    i = len(array)
    if i < 1:
        raise Exception("Empty array")
    elif i == 1:
        tmp_list = list(set(array[0]) & set(array[0]))
        return tmp_list, len(tmp_list)
    else:
        tmp_list = array[0]
        j = 1
        while j < i:
            tmp_list = list(set(tmp_list) & set(array[j]))
            j += 1
        return tmp_list, len(tmp_list)