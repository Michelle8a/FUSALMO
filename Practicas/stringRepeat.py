'''Write a function that accepts a non-negative integer n and a string s as 
parameters, and returns a string of s repeated exactly n times.'''

def repeat_str(repeat, string):
    if repeat > 0:
        final = ""
        for n in range(repeat):
            final += string
        return final
    else:
        return ""
    

def repeat_str(repeat, string):
    return string * repeat