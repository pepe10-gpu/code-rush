import time
import random as r
def listp(ammount):
    i = 0
    while i != ammount:
        x = r.randint(1,6)
        correct_code = "blank"
        if x == 1:
            print("""Set T to the first item in f
            f = [647, 1874, 1846]
            [code goes here]""")
            correct_code = "T = f[0]"
        elif x == 2:
            print("""Print the first 3 items in f
            f = [7.57, 4.48, 46.3, 548.1, 4186.36]
            [code goes here]""")
            correct_code = "print(f[0:2])"
        elif x == 3:
            print("""Remove the fourth item in f
            f = [\"Yoinked\", \"#7719\", \"On\", \"On\", \"Discord.\"]
            [code goes here]""")
            correct_code = "del f[3]"
        elif x == 4:
            print("""Save the Third item in \"f\" onto \"a\"
            f = [\"This\", \"Took\", \"A\", \"Long\", \"While\"]
            [code goes here]""")
            correct_code = "a = f[2]"
        elif x == 5:
            print("""Print the final item in \"f\" using negative indexing
            f = [\"I\", \"Hope\", \"People\", \"Enjoy\", \"This\"]
            [code goes here]""")
            correct_code = "print(f[-1])"
        elif x == 6:
            print("""Print the length of \"f\"
            f = [\"To\", \"Learn\", \"Python\", \"Or\", \"Other\", \"Uses\"]
            [code goes here]""")
            correct_code = "print(len(f))"
        submitted = str(input("""Answer:
"""))
        if submitted == correct_code:
            print("Correct!")
        else:
            print("No, it was " + correct_code)
    print("Well, those are all the puzzles you chose!")
def conditionp(ammount):
    i = 0
    while i != ammount:
        x = r.randint(1,4)
        correct_code = "blank"
        if x == 1:
            print("""Check if f contains T
            T = \"fastest\"
            f = \"Your goal is to find the fastest code to solve the puzzle\"
            If [code goes here]:""")
            correct_code = "f has T"
        elif x == 2:
            print("""Repeat the function \"f\" 50 times
            i = 0
            While [code goes here]:
                f(i)
                i = i + 1""")
            correct_code = "i != 50"
        elif x == 3:
            print("""Check if \"f\" is 20
            f = g * multiplier
            if [code goes here]:""")
            correct_code = "f == 20"
        elif x == 4:
            print("""Loop the code for how long \"f\" is
            i = 0
            f = [\"This\", \"Is\", \"A\", \"Good\", \"Idea\", \"Right\"]
            While [code goes here]:
                y(f)
                i = i + 1""")
            correct_code = "i != len(f)"
        submitted = str(input("""Answer:
"""))
        if submitted == correct_code:
            print("Correct!")
        else:
            print("No, it was " + correct_code)
    print("Well, those are all the puzzles you chose!")

def otherp(ammount):
    i = 0
    while i != ammount:
        x = r.randint(1,3)
        correct_code = "blank"
        if x == 1:
            print("""Import a library named \"mouse\" named as \"m\"
            import time
            [code goes here]""")
            correct_code = "import mouse as m"
        elif x == 2:
            print("""Call a function named \"f\" and use 7 as the only parameter
            if x == y:
                [code goes here]""")
            correct_code = "f(7)"
        elif x == 3:
            print("""Open a file called \"timings.txt\" in read-only mode
            import random
            timings = [code goes here]""")
            correct_code = "open(\"timings.txt\",\"r\")"
            correct_code = "i != len(f)"
            submitted = str(input("""Answer:
"""))
        if submitted == correct_code:
            print("Correct!")
        else:
            print("No, it was " + correct_code)
    print("Well, those are all the puzzles you chose!")








how = 0
print("Welcome! This is the alternative version of code rush, code story. If you would like to go through unfiltered puzzles, open code-rush.py .")
print("Current puzzles: lists, conditions, others")
puzzletype = str(input("Which would you like to play?"))
while True:
    if puzzletype == "lists":
        how = int(input("How many?"))
        listp(how)
    elif puzzletype == "conditions":
        how = int(input("How many?"))
        conditionp(how)
    elif puzzletype == "others":
        how = int(input("How many?"))
        otherp(how)
    else:
        print("Send either \"lists\", \"conditions\" or \"others\".")
