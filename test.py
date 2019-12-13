test_list = []
test = [0,0,0]
i = 1
while i <= 3:
    test[1] = i
    print(test)
    test_list.append(test)
    i = i+1
print(test_list)


test_list = []
test = [0, 0, 0]
i = 1
while i <= 3:
    test2 = test[:]
    test2[1] = i
    test_list.append(test2)
    print(test_list)
    i = i+1
print(test_list)