for i in range(1, 50+1):
    if i % 3 == 0 or i % 5 == 0:
        print('fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0), end=' ')
    else:
        print(i, end=' ')
print('\nfizzbuzz done!')
