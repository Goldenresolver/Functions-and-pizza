#Jason Polanco
#11/16/19
#A program that prints the lyrics of the song " Old MacDonald"
# Program will print the lyrics for five different animals
#declare and intialize variables

#define main
def main():
    #intro
    print(" Welcome to the old Macdonald sing along program!")
    #invoke the song functions with respective parameters
    song("dog","woof")
    print()

    #invoke the song functions with respective parameters
    song("cat","meow")
    print()
    #invoke the song functions with respective parameters
    song("cow","moo")
    print()

    #invoke the song functions with respective parameters
    song("chicken","cluck")
    print()
    song("goat","Baaa")


    
# define the function
#purpose: none
#parameters: two
#return type: none
# define the function give the function two parameters.
# display function with parameters. 
def song(animaL, sounD):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a",animaL,"Ee-igh, Ee-igh,Ee-igh, Oh!")
    print("With a",sounD,sounD,"here and a",sounD,sounD,"there.")
    print("Here a",sounD,"there a",sounD,"everyone a",sounD,sounD,".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")



main()
    
    
    
