'''
Jean Pierre Taico
CS 100 103
HW 11
'''

#Problem 1

def safeOpen(filename):
    try:
        openFile = open(filename)
        return openFile
    except FileNotFoundError:
        return None

print(safeOpen('ghost.txt'))


#Problem 2

def safeFloat(x):
    try:
        print(float(x))
    except ValueError:
        print(float(0.0))
        
safeFloat('abc')
 
#Problem 3
def averageSpeed():
    filename = input('Enter file name: ')
    file = safeOpen(filename)
    if file == None:
        print('File not found, try again.')
        ''' Second Chance '''
        filename = input('Enter file name: ')
        file = safeOpen(filename)
        if file == None:
            print('File not found, the program quits.')
            return None
    
    readNums = file.readlines()
    avgSpeed = []
    for numbers in readNums:
        val = numbers.split()
        for i in val:
            if safeFloat(i) and float(i) > 2.0:
                avgSpeed.append(float(i))
                
    print('Average speed is ' + str(sum(avgSpeed)/len(avgSpeed)) + ' miles per hour.')
    
averageSpeed()
                
    
    

    