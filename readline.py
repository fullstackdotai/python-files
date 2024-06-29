filename = 'Iliad.txt'
with open(filename) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line))
        line = fp.readline()
        cnt += 1
