def brackets(cur, open, closed, n):
    if len(cur) == 2*n:
        print(cur)
        return
    if open < n:
        brackets(cur + '(', open + 1, closed, n)
    if closed < open:
        brackets(cur + ')', open, closed + 1, n)

def gen(n):
    brackets("", 0, 0, n)

gen(int(input()))
