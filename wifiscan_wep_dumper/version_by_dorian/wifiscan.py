import re
shakes = open("wifi.csv", "r")
for line in shakes:
    if re.match("(.)WEP(.)", line):
        print(line)