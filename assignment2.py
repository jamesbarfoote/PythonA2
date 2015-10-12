def add_vectors(vector_1, vector_2):
    """Returns a list object representing the result of adding two vectors together.

       Arguments:
       vector_1 -- list representing first vector
       vector_2 -- list representing second vector

       Error checking:
       Both arguments must be of type list.
       Both vectors must of the same length.
       Only vector elements of type int can be added together.

       >>> from assignment2 import add_vectors

>>> add_vectors(None, [1,2,3])
Error: first argument is not a list
>>> add_vectors([1,2,3],None)
Error: second argument is not a list
>>> add_vectors("fdfdsfd","fdfdsfds")
Error: first argument is not a list
Error: second argument is not a list
>>> add_vectors(None,None)
Error: first argument is not a list
Error: second argument is not a list
>>> add_vectors([0,2,3,4],[3])
Error: lengths of the two vectors are different
>>> add_vectors([3],[0,3,12,43,8])
Error: lengths of the two vectors are different
>>> add_vectors(["a",2],[2,4])
Error: attempted to add incompatible a to 2
>>> add_vectors([4,2],["b",4])
Error: attempted to add incompatible 4 to b
>>> add_vectors(["f",2],["b",4])
Error: attempted to add incompatible f to b
>>> add_vectors([3,"f"],["b",4])
Error: attempted to add incompatible 3 to b
>>> add_vectors([3,4],[5,"b"])
Error: attempted to add incompatible 4 to b
>>> add_vectors([3,4],[5,7])
[8, 11]
>>> add_vectors([2.0],[2])
Error: attempted to add incompatible 2.0 to 2
>>> add_vectors([1,2,3,4,5,6,7,8,9],[1,1,1,1,1,1,1,1,1])
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> type(add_vectors([23,4],[4,3]))
<class 'list'>

    """
    vec1 = vector_1
    vec2 = vector_2
    list1 = []
     #if neither vectors are lists then print saying that and return
    if not isinstance(vec1, list) and not isinstance(vec2, list):
        print("Error: first argument is not a list")
        print("Error: second argument is not a list")
        return

    if isinstance(vec2, list): #if the first vec is a list
        if isinstance(vec1, list): #if 2nd vector is a list
            if isinstance(vec1, list) and isinstance(vec2, list): #if 1st vector is and 2nd is
                if len(vec1) == len(vec2): #if the size of both vectors are the same
                    for x, val in enumerate(vec1):#iterate through the vectors where x is the counter
                            if isinstance(val, int) and isinstance(vec2[x], int):# if the current value in the each vector is an integer
                                list1.append(val + vec2[x])#add the two values and put the result in a list
                            else:
                                    print("Error: attempted to add incompatible", val, "to", vec2[x])
                                    return
                else:
                    if not len(vec1) == len(vec2): #if the lengths of the vectors are different
                        print("Error: lengths of the two vectors are different")
                        return
            else:
                if not (isinstance(vec1, list) and not (isinstance(vec2, list))): #if both the vectors are not lists
                    print("Error: first argument is not a list")
                    print("Error: second argument is not a list")
                    return

        else:
            if not isinstance(vec1, list) and isinstance(vec2, list): #if vector1 isnt a list but vector 2 is
                    print("Error: first argument is not a list")
                    return
    else:
        if isinstance(vec1, list) and not isinstance(vec2, list): #if vectors1 is a list but vector2 isnt
                    print("Error: second argument is not a list")
                    return

    return list1

def print_frequency(some_text):
    """Prints a table of letter frequencies within a string. 

       Non-letter characters are ignored.
       Table is sorted alphabetically.
       Letter case is ignored.
       Two blank spaces will separate the letter from its count.

       Returns None in all cases.

       Argument:
       some_text -- string containing the text to be analysed.

       Error checking:
       The argument must be a string object.

       This is a doctest for print_frequency

>>> from assignment2 import print_frequency

>>> print_frequency("ThiS is String with Upper and lower case Letters")
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2

>>> print_frequency(None)
Error: only accepts strings
>>> print_frequency(int)
Error: only accepts strings
>>> print_frequency(float)
Error: only accepts strings
>>> print_frequency("")
>>> print_frequency(" ")
>>> print_frequency("AAAAA")
a  5
>>> print_frequency("AbABAbABA")
a  5
b  4
>>> print_frequency("AbAZBAZbZABA!")
a  5
b  4
z  3
>>> print_frequency("AbAZBA*****98328504ZbZABA!")
a  5
b  4
z  3

    """
    count = 0
    list1 = []

    if isinstance(some_text, str): #if some_text is a string
        clist = some_text.lower()
        clist = sorted(clist) #sort the list alhabetically
        for i in clist: #iterate through the list
            if i.isalpha(): #if the next character is a letter
                if not list1.__contains__(i): #if the item isnt already in the other list
                    list1.append(i) #add the new item to the other list
                    print(i, "", clist.count(i)) #print out the letter and its count
    else:
        if not isinstance(some_text, str):
            print("Error: only accepts strings")
    return None

def verbing(some_text):
    """Returns a string where the each word has ing added to it if it is 3 or more characters or length and 
       ly to shorter words.

       Argument:
       some_text -- string containing the text to be analysed.

       Error checking:
       The argument must be a string object.
    """
    wList = []

    if some_text == "": #if there is nothing in the string then print out '' and return
        print("''")
        return

    if isinstance(some_text, str): #if some_text is a string
        list1 = some_text.split(" ")#then split the string and put it in a list
        for i in list1: #iterate through the string
            if len(i) < 3 and len(i) > 0: #if the length of the word is less than 3 then add ly
                wList.append(i + "ly")
            else:
                if len(i) >= 3: #else if the length is grater than 3 then add ing
                    wList.append(i + "ing")
        str(wList) #convert the list to a string
        return(" ".join(wList)) #return the string of all the words

    else:
        if not isinstance(some_text, str):#if the text isnt a string then print error message
            print("Error: only accepts strings")
            return



def verbing_file(file_name):
    """Returns the contents of a given file after applying the verbing function to each
       line in the file.

       Argument:
       file_name -- name of the file (assumed to exist in same directory from where the 
                    python script is executed.

       Error checking:
       The argument must be a string object.
       File must exist and be readable (note no need to distinguish these cases).    
    """
    if isinstance(file_name, str): #if the file_name is a string then open the file and read it into a single string and call the verbing method
        f = open(file_name)
        content = f.read()
        f.close()
        return verbing(content)
    else:
        if not isinstance(file_name, str): #else print the error message
            print("Error: only accepts strings")
    return None
