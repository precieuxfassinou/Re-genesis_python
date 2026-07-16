xfile= open('mbox.txt')
count = 0
for cheese in xfile:
        count = count + 1
        print(cheese)
print('Line count:', count)
