import datetime
#current_year=datetime.date.today().year
first_year=int(input("Enter the first year:"))
final_year=int(input("Enter the final year:"))
if final_year<first_year:
    print("Final Year Must Be Greater than Current Year.")
else:
    print(f"Leap Years From{first_year}to{final_year}")
    for year in range(first_year,final_year+1):
        if(year%4==0 and year%100!=0)or(year%400==0):
            print(year)
