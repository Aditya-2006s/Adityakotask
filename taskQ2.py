"""Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give
them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask
if they want "Chicken" or "Fish"""
a=input(" veg or nonveg")
if a=="veg":
    b=input("salad or pasta")
    if b=="salad":
        print=("you are served salad")
    elif b=="pasta":
        print=(" you are served pasta")
    else:
        print= ("there is no option available")
elif a=="nonveg":
    b=input("chicken or fish")
    if b=="chicken":
        print(" you are served chicken")
    elif b=="fish":
        print("you are served fish")
    else:
        print=("there is no option avaiable sir")
else:
    print("veg or nonveg" )


  
    
    
 
 