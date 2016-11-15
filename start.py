from sys import exit

print "hello"

def crystal():
    print "This is new, what do you think? good or bad?"

    choice = raw_input("> ")

    if choice == "good":
        print "okay."
        good()

    elif choice == "bad":
        print "okay."
        bad()

    else:
        print "Pick one."

def good():
    print "Glad we like it."

def bad():
    print "well we need to get used to it."

crystal()
