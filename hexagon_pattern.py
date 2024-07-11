def print_hexagon_pattern(rows,cols):
    top = " ___    "

    upper_middle_extend = "/   \\___"
    upper_middle_end = "/   \\"

    lower_middle = "\\___/   "
    lower_middle_end = "\\___/"


    print(top * ((cols//2)+1))

    for r in range(rows):
       print(upper_middle_extend * (cols//2),end="")
       print(upper_middle_end)
       print(lower_middle * (cols//2),end="")
       print(lower_middle_end)
   

row = int(input("enter no. of rows: "))
column = int(input("enter no. of columns: "))
print_hexagon_pattern(row,column)
