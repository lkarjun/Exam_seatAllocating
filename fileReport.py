
def createFile(seatallocating, classroom, rows):
    fileName = classroom+'.txt'
    with open(fileName, 'w') as file:
        file.write(f'Classroom:  {classroom.upper()}')
        for row in range(rows):
            file.write(f'\n\nRow: {row+1}')
            file.write('\n\n')
            for key, value in seatallocating[row].items():
                file.write(f'{key}. {value.upper()}      ')
    
    print('Ok.................................')