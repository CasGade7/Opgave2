f = open("Opgave2/app_log.txt", "r")
myLines = f.readlines()
for line in myLines:
    if 'ERROR' in line or 'WARNING' in line:
        c = open("Opgave2/EandW_log.txt", "a")
        c.write(line)
        c.close()