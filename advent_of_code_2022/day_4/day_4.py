
counter = 0
with open('input.txt') as f:
    lines = f.readlines()
    for _ in lines:
        elf1 = [_ for _ in range(int(_.split(',')[0].split('-')[0]), int(_.split(',')[0].split('-')[1])+1)]
        elf2 = [_ for _ in range(int(_.split(',')[1].split('-')[0]), int(_.split(',')[1].split('-')[1])+1)]
        if set(elf2).issubset(elf1) == True:
            counter += 1
        elif set(elf1).issubset(elf2) == True:
            counter +=1



print(counter)


counter = 0
with open('input.txt') as f:
    lines = f.readlines()
    for _ in lines:
        elf1 = [_ for _ in range(int(_.split(',')[0].split('-')[0]), int(_.split(',')[0].split('-')[1])+1)]
        elf2 = [_ for _ in range(int(_.split(',')[1].split('-')[0]), int(_.split(',')[1].split('-')[1])+1)]
        x = [_ for _ in elf1 if _ in elf2]
        if len(x) != 0:
            counter += 1



print(counter)