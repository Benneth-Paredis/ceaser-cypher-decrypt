#Author Benneth Paredis
#Date 18-11-2022


#Alphabet only letters
alphabet = {
        'a' : 0, 
        'b' : 1, 
        'c' : 2, 
        'd' : 3, 
        'e' : 4, 
        'f' : 5, 
        'g' : 6, 
        'h' : 7, 
        'i' : 8, 
        'j' : 9, 
        'k' : 10, 
        'l' : 11, 
        'm' : 12, 
        'n' : 13, 
        'o' : 14, 
        'p' : 15, 
        'q' : 16, 
        'r' : 17, 
        's' : 18, 
        't' : 19, 
        'u' : 20, 
        'v' : 21, 
        'w' : 22, 
        'x' : 23, 
        'y' : 24, 
        'z' : 25
}

#convert array of char to string
def convert(s): 
    new = ""

    for x in s:
        new += x
    return new

#gets value out of alphabet given a key
def get_val(ky):
    for key, value in alphabet.items():
        if ky == key:
            return value
 
    return "value doesn't exist"

#gets key out of alphabet given a value
def get_key(val):
    for key, value in alphabet.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# decrypts ceaser cipher and returns all possible results
def decryptCode(text):

    result = []
    for n in range(26):
        subresult = []

        for index in range(len(text)):
            newValOfLetter = (get_val(text[index]) + n) % 26
            shiftedLetter = get_key(newValOfLetter)
            subresult.append(shiftedLetter)
        subresult = convert(subresult)
        result.append(subresult)
    return result


