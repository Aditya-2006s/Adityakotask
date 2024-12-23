price= float(input("Enter the price of an item:"))
if price>=1000:
    discount=(price/100)*10
    print(" the price after discount is ",price-discount)
elif price>=500:
    discount=(price/100)*5
    print("the price after discount is ", price-discount)
else :
    print(" the final price is :" , price)


    
 
