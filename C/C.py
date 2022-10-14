import sys

num = sys.stdin.readline().strip()
last = None
for i in range(int(num)):
    current = sys.stdin.readline().strip()
    if current != last:
        print(current)
    last = current
