from pprint import pprint as pp
from fileReport import createFile, createCsv

dec = lambda: '=' * 32

'''student exam seat assigning'''

class Student:

    
    def __init__(self, schl_code, examclass):

        if not schl_code[:2].isalpha():
            raise ValueError(f'{dec()} ITS AN NONEXISTING NUMBER {dec()}')
        if not schl_code[2:].isdigit():  
            raise ValueError(f'{dec()} INVALID ALLOCATED ROLL NUMBER {dec()}')


        self._schl_code = schl_code
        self._examclass = examclass
        row, seats = self._examclass.seating_plan()
        alloted_room = self._examclass.allocatedClass()
        self._seating = [alloted_room] + [{letter: None for letter in seats} for _ in row]

    def display(self):
        '''Display students seating'''
        print(dec())
        pp(self._seating)
        print(dec())

    def schoolCode(self):
        '''Display shoolcode'''
        print(dec())
        return self._schl_code
                
    def allocate_students(self, seat, student):
        '''Allocate student to class room'''
        rows, seat_letter = self._examclass.seating_plan()
        letter = seat[-1]
        if letter not in seat_letter:
            raise ValueError(f'{dec()} ITS AN INVALID SEAT ROW NUMBER {letter}{dec()}')
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except:
            raise ValueError(f'{dec()} ITS AN INVALID SEAT NUMBER{row}{dec()}')

        if row not in rows:
            raise ValueError(f'{dec()} INVALID ENRY....{dec()}')
        
        self._seating[row][letter] = student


class Examclass:
    
    def __init__(self, class_one, class_two, allocated_class, num_rows, num_seat_per_row):
        self._class_one = class_one
        self._class_two = class_two
        self._num_rows = num_rows 
        self._num_seat_per_row = num_seat_per_row
        self._allocated_class = allocated_class

    def allocatedClass(self):
        '''Display allocated class for Exam'''
        
        return self._allocated_class
        

    def allocatedClasses(self):
        '''Display allocated class of students'''

        dict = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th', 10: 'th'}
        print(dec())
        return f'TWO CLASSES WILL BE SEAT HERE THEY ARE {self._class_one}{dict[self._class_one]} and {self._class_two}{dict[self._class_two]}'

    def number_of_row(self):
        '''display number of row in exam room '''

        print(dec())
        return self._num_rows

    def seat_per_row(self):
        '''display seat per row in exam room'''
        print(dec())
        return self._num_seat_per_row
    
    def seating_plan(self):
        '''return seating plan allocated class'''
        print(dec())
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK' [:self._num_seat_per_row]) 



def main():
    schl_code = input('Enter School-code: ')
    #KV21
    cls_one = int(input('Enter Class_one: '))
    cls_two = int(input('Enter Class_two: '))
    #2 6 ! 2nd
    alt_cls = str(input('Enter exam class room for the classes: '))
    #8th-B
    num_row = int(input('Enter number of rows in allocated class: '))
    #4
    num_seats = int(input('Enter number of seat in a row: '))
    #2
    '''creating object'''
    obj1 = Student(schl_code, Examclass(class_one = cls_one, class_two = cls_two, allocated_class = alt_cls, num_rows =  num_row, num_seat_per_row = num_seats))
    
    altS = input('Do you want to allocate students...[Y/n]')
    
    total_count = num_row * num_seats

    if altS.lower() == 'y' :

        for i in range(1, total_count+1):
            sn = input(f'Enter the seat number of student {i}: ').upper()
            #1A
            name = input(f'Enter the name Student {i}: ')
            obj1.allocate_students(sn, name)
    else: 
        pass
    
    obj1.display()
    print(dec())
    fileReport = input('do you want to print the list to a txt file: [Y/n] ')
    if fileReport.upper() == 'Y':
        createFile(obj1._seating[1:], alt_cls, num_row)
    fileCsv = input('do you want to make csv file: [Y/n] ')
    if fileCsv.upper() == 'Y':
        createCsv(obj1._seating[1:], alt_cls, num_seats)
    print()
    print('Thank You...')
    print()



if __name__ == '__main__':
    main()



