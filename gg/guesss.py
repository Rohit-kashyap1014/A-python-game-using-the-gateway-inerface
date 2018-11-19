

print 'Content-type: text/html'
print ''

import cgi
import random
field = cgi.FieldStorage()

cross = 0
circles = 0

if "val" in form:
    val = field.getvalue("answer")
else:
    val = ""
    for i in range(4):
        val += str(random.randint(0, 9))

if "guess" in field:
    guess = field.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == val[key]:
            cross += 1
        else:
            for answerDigit in val:
                if answerDigit == digit:
                    circles += 1
                    break
        
else:
    guess = ""
    
if "numberOfGuesses" in field:
    numberOfGuesses = int(field.getvalue("numberOfGuesses")) + 1
else:
    numberOfGuesses = 0

if numberOfGuesses == 0:
    msg = "I've chosen a 4 digit number. Can you guess it?"
elif cross == 4:
    msg = "Well done! You got in " + str(numberOfGuesses) + " guesses. <a href=''>Play again</a>"
else:    
    msg = "You have " + str(cross) + " correct digit(s) in the right place, and " + str(circles) + " correct digit(s) in the wrong place. You have had " + str(numberOfGuesses) + " guess(es)."

print '<h1>Mastermind</h1>'
print "<p>" + msg + "</p>"
print '<form method="post">'
print '<input type="text" name="guess" value="' + guess + '">'
print '<input type="hidden" name="answer" value = "' + val + '">'
print '<input type="hidden" name="numberOfGuesses" value = "' + str(numberOfGuesses) + '">'
print '<input type="submit" value="Guess!">'
print '</form>'