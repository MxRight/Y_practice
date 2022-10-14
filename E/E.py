from collections import Counter

def anagramm(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    delta = c_a - c_b
    if len(delta) == 0 and len(a) == len(b):
        return '1'
    else:
        return '0'

with open('input.txt', 'r', encoding='utf-8') as f_in:
    a, b = f_in.readlines()

with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(anagramm(a, b))
