n = int(input())
string = '*' * n

for i in range(0, len(string)+1):
    print(f'{string[:i]: >{n}}')