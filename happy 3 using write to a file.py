def happy():
    return "Happy Birthday to you!|n"

# the magic of value returning functions is we have streamlined the
#program so that an entire verse is built in a single string expression.
# this line really illustrates the power and beauty of value returning functions.
# in this line we are calling happy() function twice
def verseFor(person):
    lyrics = happy()*2 + "Happy birthday, dear "+person+".\n"+happy()
    return lyrics
# in main() we are calling verseFor function within it it contains happy()
# using a loop and a list to invoke the function.
def main():
    outfile= open("Happy_Birthday.txt","w")
    for person in ["Fred","Lucy","Elmer"]:
         print(verseFor(person))
         # or we can use print(verseFor(person),file=outfile)
         outfile.write(verseFor(person))
         # or we can use 
    outfile.close()


main()
