with open('/etc/passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    while line:
        print(line, end = '')
        line = text(f, None)

    with open('/etc/passwd') as f:
        lines = (line for line in f if not line.startswith('#'))

