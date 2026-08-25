"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: AMELIA LITVAK
Date: SEPTEMBER 10, 2025
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.
    
    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.
    
    Examples: 
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'
    
    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    pos1 = s.find('(')
    # Search for the first close parens ')' AFTER the open parens
    pos2 = s.find(')', pos1)
    #Slice the string s between pos1 and pos2
    #Enforce the preconditions
    return s[pos1+1:pos2]


def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.
    
    Cornell network ids consist of 2 or 3 lower-case initials followed by a 
    sequence of digits.
    
    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False
    
    Parameter s: the string to check
    Precondition: s is a string
    """
    # isalpha, isdecimal
    if s[:2].isalpha() and s[:2].islower() and s[2:].isdecimal():
        return True
    elif s[:3].isalpha() and s[:3].islower() and s[3:].isdecimal():
        return True
    else:
        return False

