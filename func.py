def surname(surnamee):
    for i in range(len(surnamee)):
        if i <= 4:
            print('*', end= '')
        else:
            print(surnamee[i], end='')
surname('   борисюк')