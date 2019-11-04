def main():
    initial = open("stunme.sav", "r").readlines()
    initial[0]="name: stunned\n"
    output = open("stunned.sav", "w")
    ourunit = False
    maxhp = ""
    for line in initial:
        if "faction: 0" in line:
            ourunit = True
        elif "faction: " in line and "faction: 0" not in line:
            ourunit = False
        elif "health:" in line:
            maxhp = line[line.find(":")+2:]
        if "stunlevel" in line and ourunit is False:
            line = line[:line.find(":")+2] + "1" + maxhp
        output.write(line)
    output.close()


if __name__ == '__main__':
    main()
