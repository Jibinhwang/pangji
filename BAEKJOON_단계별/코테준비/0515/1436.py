import sys

n = int(sys.stdin.readline())

string = '666'
count = 0

end = 666
while True:
    if string in str(end):
        count = count + 1
    if count == n:
        print(end)
        break
    else:
        end += 1
