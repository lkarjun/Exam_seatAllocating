
#creates a simple text file 
import csv

def createFile(seatallocating, classroom, rows):
    fileName = classroom+'.txt'
    with open(fileName, 'w') as file:
        file.write(f'Classroom:  {classroom.upper()}')
        for row in range(rows):
            file.write(f'\n\nRow: {row+1}')
            file.write('\n\n')
            for key, value in seatallocating[row].items():
                file.write(f'{key}. {value.upper()}      ')
    
    print('Ok done...')

#creates csv file

def createCsv(seatallocating, classroom, num_seats):
    fileName = classroom+'.csv'
    keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    with open(fileName, 'w') as f:
        writer = csv.DictWriter(f, fieldnames = keys[:num_seats])
        writer.writeheader()
        for tvalue in range(len(seatallocating)):
            writer.writerow(seatallocating[tvalue])

    print('Ok done...')

