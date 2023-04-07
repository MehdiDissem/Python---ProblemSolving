# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    return ' '.join(recurStrEval(s, '', []))
     
def recurStrEval(str, temp_str, str_arr):
    if not str:
        str_arr.append(temp_str)
        return str_arr
    if str[0].isupper():
        str_arr.append(temp_str)
        temp_str = str[0]
        return recurStrEval(str[1:], temp_str, str_arr)
    if str[0].islower():
        temp_str += str[0]
        return recurStrEval(str[1:], temp_str, str_arr)