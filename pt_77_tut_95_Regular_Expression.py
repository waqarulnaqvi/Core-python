import re
txt='''A regular expression (shortened as regex or regexp;[1] sometimes referred to as rational expression[2][3]) is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory.

The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-Processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax Lrocessing.

Regular expressions are used in search engines, in search and replace dialogs of word processors and text editors, in text processing utilities such as sed and AWK, and in lexical analysis. Regular expressions are supported in many programming languages.'''
# pattern="into"
# match=re.search(pattern,txt)
# print(match)


# pat="[AWR]+\w+"
# pat="[AWR]."#any character except new line.
# pat="[AWR]..e"#any character except new line.
pat="[AWR]..()[er]"#any character except new line.
matches =re.finditer(pat,txt)
for match in matches:
    print(match)
    # print(match.span())
    # print(type(match.span()))
    # print(txt[match.span()[0]:match.span()[1]])


# pattern=r"[A-Z]+rocessing"
# matches =re.finditer(pattern,txt)
# for match in matches:
#     # print(match)
#     # print(match.span())
#     # print(type(match.span()))
#     print(txt[match.span()[0]:match.span()[1]])


