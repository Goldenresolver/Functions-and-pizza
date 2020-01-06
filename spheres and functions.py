#Jason Polanco
#A program that returns the surface area of a sphere having the given radius
# A program that returns the volume of a sphere having the given radius
#define main
def main():
    #intro
    print("This program will caculate the volume and surafce area of a sphere")

    #declare and intialize variables
    radii= float(input("\nPlease enter the radius: "))

    #create variable to accept the value from the function
    # and invoke the functions
    spArea= sphereArea(radii)

    #create variable to accept the value from the function
    # and round two spaces
    spVolume= round(sphereVolume(radii),2)

    #display the area and volume of the sphere.
    print("The area of the sphere:", spArea)
    print("The Volume of the sphere:", spVolume)
    
                 
    
    
# define the function
#declare and intialize variables
#purpose to calculate the sphere of a volume
#parameters: one
#return type: 1 float
def sphereArea(radius):
        sphere_Area= 0.0
        sphere_Area= 4*(3.14)*(radius)**2

        return sphere_Area
        
     



# define the function
#declare and intialize variables
# return type : 1 float
#purpose to calculate the sphere of a volume.
#parameters: one
def sphereVolume(radius):
    
        sphere_Volume=0.0
        sphere_Volume=4/3*(3.14)*(radius)**3

        return sphere_Volume


main()

