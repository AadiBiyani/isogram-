string = input("Enter a word:")
length = len(string)

def is_isogram(string):
    index = 0
    for i in range (length-1):
        if string[index] == string[index+1]:
            
            index = index + 0
            
        else:
            index = index +1
            
    if index == length-1:
        print ("the word is an isogram")
    else:
        print("the word is not an isogram")
    pass
                               
is_isogram(string)
