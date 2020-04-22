#Given a string, write a python function to 
#return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.

#lex_auth_0127136253311385601197

def check_occurence(string):
    #start writing your code here
    string = string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
