print ('////////////////////question 1///////////////////')
num = 0
def counter(num):
    while num <= 150:
        num = num + 1
        print(num)
counter(num)

print('//////////////question 2/////////////////' )

quintus = 0
def count_by_five(quintus):
    while quintus < 1000:
        quintus = quintus + 5
        print(quintus)

count_by_five(quintus)

print('//////////////question 3/////////////////' )

def dojo_count():
    count = 0
    for count in range(100):
        count = count + 1
        if count % 10 == 0:
            print('Coding Dojo')
        elif count % 5 == 0:
            print('Coding')
        else:
            print(count)
dojo_count()

print('//////////////question 4/////////////////' )

def big_daddy():
    tot = 0
    for i in range(500000):
        i = i + 1
        if i % 2 == 0:
            continue
        else:
            tot = i + tot
    print('Total is',tot)
big_daddy()

print('//////////////question 5/////////////////' )

def countdown():
    i = 2018
    while i > 0:
        print(i)
        i = i - 4
countdown()

print('//////////////question 6/////////////////' )
def flexcount(lowNum,highNum,mult):
    for num in range(lowNum, (highNum + 1)):
        if num % mult == 0:
            print(num)
        else:
            continue
    
flexcount(2,9,3)
