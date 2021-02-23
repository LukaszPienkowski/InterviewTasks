## Replacing num 1 - 1000 with its Roman equivalent

def ChangeArabicIntoRoman(ArabicNum):
    romantransforms = {'1': "I", '2': "II", '3': "III", '4': "IV", '5': "V", '6': "VI", '7': "VII", '8': "VIII", '9': "IX"} 
    romantransformd = {'1': "X", '2': "XX", '3': "XXX", '4': "XL", '5': "L", '6': "LX", '7': "LXX", '8': "LXXX", '9': "XC"}
    romantransformt = {'1': "C", '2': "CC", '3': "CCC", '4': "CD", '5': "D", '6': "DC", '7': "DCC", '8': "DCCC", '9': "CM"}
    stringnum = str(ArabicNum)
    lengthnum = len(stringnum)
    resultstr = ""
    if lengthnum == 1:
       resultstr = romantransforms[stringnum[0]]
    elif lengthnum == 2:
        resultstr = romantransformd[stringnum[0]] + romantransforms[stringnum[1]]
    elif lengthnum == 3:
        resultstr = romantransformt[stringnum[0]] + romantransformd[stringnum[1]] + romantransforms[stringnum[2]] 
    else:
        resultstr = "M"
    

    return(resultstr)

print(ChangeArabicIntoRoman(217))

