
import sys

print("Hallo")


for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin *****{line}*****')
print("Done")

with open('prova', 'r') as f:
    print(f.read())
