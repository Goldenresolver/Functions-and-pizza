#Jason Polanco
#11/30/19
# A program that caculates the cost per square inch of a circular pizza
# given its diameter and price, use functions to complete it.

#define functions
#return type: float
#parameters: none
# This function prompts user for input, using while loops for input validation
#must be positive numbers

def GetPrice():
    pricePizza=0

    while pricePizza <=0:
        pricePizza= int(input("Please enter the price of the pizza"))

        if pricePizza <=0:
                print("Please enter a positve number")

    return pricePizza


#define functions
#return type: float
#parameters: none
# This function prompts user  for input  using while loops for input validation
#must be positive numbers



def PizzaInches():

     pizzaInches= 0


     while pizzaInches <=0:

        pizzaInches= int(input("\nPlease enter the pizza inches: "))

        
        pizzaRadius= pizzaInches/2

        if pizzaInches <=0:
                print("\nPlease enter a positive number")

     return pizzaRadius

#define functions
#return type: float
#parameters: one
# This function returns the area of a pizza with given radius



def GetAreaofPizza(r):

    pizzaArea= (3.14)*(r)**2

    return pizzaArea


#define functions
#return type: float
#parameters:  2 floats(costofpizza,Area)
# This function returns the cost of a pizza with  a given radius


def GetCostPerSqin(costofpizza,Area):

    costofPizza= costofpizza/Area

    return costofPizza
         


#return type: None
#Parameters: None
#This function displays an introduction
def Intro():
    print("\nWelcome to the pizza program!")

#return type: float
#Parameters: None
#This function prompts user for input  using while loops for input validation
# must be positive numbers

def GetPrice():
    pricePizza=0

    while pricePizza <=0:
        pricePizza= int(input("\nPlease enter the price of the pizza:"))

        if pricePizza <=0:
                print("\nPlease enter a positve number")

    return pricePizza

#return type: None
#Parameters: 2 floats(areaPizza, costPizza)
#This function displays the two values passed to it
def PrintInfo(areaofpizza,costofpizza):

  print("\nArea of pizza",areaofpizza)
  print("\nCost of pizza",costofpizza)

  return areaofpizza,costofpizza

def main():
     #declare and initialize variables
     #float, myPizzaprice,myPizzaArea,myPizzaRadius,myCostperSqInch.

    try:
        myPizzaprice=0
        myPizzaArea=0
        myPizzaRadius=0
        myCostperSqInch=0

        #call(invoke) Intro function 
        Intro()

      
        #call a function to prompt for a price and store in myPizzaprice
        myPizzaprice= GetPrice()

        #call a function to prompt for pizza inches and radius and store in mypizzaRadius

        mypizzaRadius = PizzaInches()

         #invoke a function to store the area of pizza in myPizzaArea
        myPizzaArea = GetAreaofPizza(mypizzaRadius)

        #call a function to display the results of the above calculations
        displayinfo = PrintInfo(myPizzaArea,myCostperSqInch)
        


        
     #call a function to store the cost of the pizza and display it
        myCostperSqInch =GetCostPerSqin(myPizzaprice,myPizzaArea)

        print("\nCost of pizza per square inch",round(myCostperSqInch,3))

    except ValueError:
        print("Please enter a valid number")
        main()
    
main()
    
