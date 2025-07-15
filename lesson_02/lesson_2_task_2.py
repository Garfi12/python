def is_year_leap(year):

    if year % 4 == 0:
       print("Год", year, ":", "True")

    else: 
        print("Год " , year , ":" ,False)
        
is_year_leap(2021)
