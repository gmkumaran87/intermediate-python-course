no_tc = int(input('Please enter no of test cases '))
str = []
odd_chr = even_chr = ''

for i in range(no_tc):
    str.append(input('Enter your word: '))
for word in str:
    odd_chr = even_chr = ''
    for i, w in enumerate(word):
        if i == 0 or i % 2 == 0:
            even_chr += w
        elif i %2 != 0:
            odd_chr += w
    print(f'{even_chr}  {odd_chr}')
