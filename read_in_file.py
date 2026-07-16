inputf = input('Enter the file name: ')
xfile= open(inputf)
count = 0
for cheese in xfile:
        count = count + 1
        cheese = cheese.rstrip()
        print(cheese)
print('\nLine count:', count)
