indian=["samosa","daal","naan"]
chinese=["egg role","stickers","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a Dish Name: ")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("This is new Dish",dish)