from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startwith('#'), f):
        print(line, end='')
