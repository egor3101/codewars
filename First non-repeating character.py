"""Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character."""

import collections


answer =""
check_exist_answer = 0
check_amount_letter = collections.Counter(s.lower())
for key, value in check_amount_letter.items():
    if value == 1:
        check_exist_answer = 1
        answer = key
        for letter in s:
            if (letter.isupper()) and (letter == answer.upper()):
                answer = answer.upper()

                break

        break
print(answer)


