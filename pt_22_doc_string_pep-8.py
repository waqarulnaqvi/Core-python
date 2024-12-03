# k=34 #if you uncomment it then frist doc string will become none.
# doc string change karke program ke output change kiye ja sakte hai but comment change karke program ke output change ni kiye ja skate hai
"""hello Have a good day"""
print(__doc__)
def square(n):
    k=23
    """Doc string must be written in the fast line of the function"""
    """Takes in a number n1, returns the square of n"""
    '''Takes in a number n, returns the square of n'''
    print(n**2)
def square1(n):
    """Doc string must be written in the fast line of the function"""
    """Takes in a number n1, returns the square of n"""
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
print(square1.__doc__)

"""What is PEP-8?
PEP 8 is a document that provides guidelines and best practice on how to write Python code.It was written in 2001 by Guido van Rossum,Barry Warsaw,and Nick Coghlan. The primary focus of PEP 8 is to improve the readibility and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them.A PEP is a document that describes new features proposed for Python and documents aspects of Python ,like design and style, for the community.-
"""
"""import this ->Enter
You will see the poem :
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
"""This poem is an easter jo intentionally daala gya hai python me and it does not have any use in python programming. """