def count_vietnamese_accented_letters(telex_input):
    patterns = ['aw', 'aa', 'dd', 'ee', 'oo', 'ow']
    count = 0
    i = 0
    while i < len(telex_input):
        if i + 1 < len(telex_input) and telex_input[i:i+2] in patterns:
            count += 1
            i += 2
        elif telex_input[i] == 'w':
            count += 1
            i += 1
        else:
            i += 1
        a = telex_input[i:i+2]
        print(a)
    return count

input_str = input('Nhap 1 chuoi ky tu: ')
print(count_vietnamese_accented_letters(input_str))
