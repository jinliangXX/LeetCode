import sys

if __name__ == "__main__":
    str_input = list(map(str, sys.stdin.readline().strip().split()))
    result = dict()
    for str_item in str_input:
        char_start = str_item[0]
        result[char_start] = result.get(char_start, 0) + 1
        char_end = str_item[-1]
        result[char_end] = result.get(char_end, 0) - 1
    is_true = True
    for index in result:
        if result[index] != 0:
            is_true = False
            break
    print('true' if is_true else 'false')
