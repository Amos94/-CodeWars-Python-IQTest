def iq_test(string):
    #your code here

    numbers = string.split()
    noOdds, noEvens, position = 0, 0, 0

    for i in range (0, len(numbers)):
        if(int(numbers[i]) % 2 == 0):
            noEvens = noEvens + 1
        else:
            noOdds = noOdds + 1
    
    for i in range(0, len(numbers)):
        if(noOdds > noEvens):
            if (int(numbers[i]) % 2 == 0):
                position = i+1
        else:
            if (int(numbers[i]) % 2 != 0):
                position = i+1
    return position
