"""
To make a profit, a local store marks up the prices of its items by a certain
percentage. Write a C++ program that reads the original price of the item sold, 
the percentage of the marked-up price, and the sales tax rate. The program then
outputs the original price of the item, the percentage of the mark-up, the store’s
selling price of the item, the sales tax rate, the sales tax, and the final price of the
item. (The final price of the item is the selling price plus the sales tax.)
"""

# input: original price, percentage of mark-up price, sales tax rate
# output: original price, percentage of the mark-up, selling price and sales tax rate
# final price = selling price + sales tax

originalprice = float(input("Enter original price of the item sold: "))
profitpercentage = float(input("Enter profit ppercentage: "))
taxrate = float(input("Enter tax rate: "))

print("The original price is %.2f" %originalprice)
print("The item was increase at a percentage of %.2f" %profitpercentage)

sellingprice = originalprice * (1 + (profitpercentage / 100))
print("The selling price of the item is %.2f" %sellingprice)

salestax = sellingprice * (taxrate / 100)
print("The tax on the sales is %.2f" %salestax)

finalprice = sellingprice + salestax
print("The final cost then becomes %.2f %x" %finalprice %finalprice)