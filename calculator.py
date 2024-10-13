from parser import *

class Report:
    RECC_BUDGET = 0.30
    YEAR = int(2023)
    
    def __init__(self, county, income, unit):
        if (0 < income):
            self.annual_income = float(income)
            self.income = float(income)/12
            self.county = county
            self.unit = unit
        else: 
            raise ValueError
        
    def set_inflation(self):
        inflate_dict = inflate_rate()
        inflation = 1
        for x in range(1,4):
            inflation *= 1 + float(inflate_dict[str(self.YEAR + 1)])
        return inflation
    
    def create_budget(self):
        inflation = self.set_inflation()-1 #pow(1.029, 3) - 1
        low_bound = self.income*self.RECC_BUDGET
        high_bound = self.income * (self.RECC_BUDGET + inflation)
        return low_bound, high_bound
    
    def find_options(self, low_dict, high_dict, pd_rent):
       options = f"\n    Based on that budget, you should look at these districts:"
       #https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
       sorted_low = sorted(low_dict.items())
       sorted_high = sorted(high_dict.items())

       if (len(low_dict) == 0) and (len(high_dict) == 0):
           sorted_rent = sorted(pd_rent.items(), key=lambda val: (val[1], val[0]))
           return f'''\nYour budget is too low to live comfortably in Fairfax County. The cheapest 
    place to live is {sorted_rent[0][0]}'''
       x = 1
       goal = 4
       if (len(low_dict) + len(high_dict) < 3):
           goal = len(low_dict) + len(high_dict)
       while x < goal:
            if len(low_dict) > x:
                district = sorted_low[0-x][1]
                rent = float(sorted_low[0-x][0])
                options += f"\n\toption {x}:  {district} (Avg. Rent: ${rent})"
            elif len(high_dict) > x - len(low_dict):
                y = x - len(low_dict)
                district = sorted_high[y][1]
                rent = float(sorted_high[x][0])
                options += f"\n\toption {x}:  {district} (Avg. Rent: ${rent})"
            x += 1
       return options
            
    def find_pd_budget(self, low_bound, high_bound, pd_rent):
        valid_low = {}
        valid_high = {}
        for x in pd_rent:
            if (float(pd_rent[x][1]) < low_bound):
                valid_low[pd_rent[x][1]] = x
            elif (float(pd_rent[x][1]) < high_bound):
                valid_high[pd_rent[x][1]] = x
            
        return self.find_options(valid_low, valid_high, pd_rent)
        
    def find_match(self, low_bound, high_bound, dicti):
        valid = {}
        for x in dicti:
            if (float(dicti[x][1]) < low_bound):
                valid[dicti[x][1]] = x
            elif (float(dicti[x][1]) < high_bound):
                valid[dicti[x][1]] = x
            else:
                return sorted(dicti.items(), key=lambda val: (val[1], val[0]))[0][0]
        #https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
        return sorted(valid.items())[-1][1]
        
    def find_report_range(self, unit, struct, age):
        avg = (unit + struct + age)/3
        med = [unit, struct, age]
        med.sort
        if (avg < int(med[1])):
            return f"{avg:.2f}-{med[1]:.2f}"
        elif (avg > int(med[1])):
            return f"{med[1]:.2f}-{avg:.2f}"
        else:
            return avg
        
    def __str__(self):
        low_bound, high_bound = self.create_budget()
        pd_budget = self.find_pd_budget(low_bound, high_bound, r_pd_rent())
        vacant_units = r_unit_vacancy()[self.unit][0]
        unit_rent = int(r_unit_rent()[self.unit][1])
        struct = self.find_match(low_bound, high_bound, r_struct_rent())
        age = self.find_match(low_bound, high_bound, r_age_rent())
        struct_rent = int(r_struct_rent()[struct][1])
        age_rent = int(r_age_rent()[age][1])
        report_range = self.find_report_range(unit_rent, struct_rent, age_rent)
        report = f'''    To live in {self.county} with an annual income of ${self.annual_income:.2f}, your monthly bill budget should be 
        between ${low_bound:.2f} and ${high_bound:.2f}. {pd_budget}
      The average rent for a {self.unit} would be ${unit_rent:.2f}. There are {vacant_units} vacant {self.unit} units.
      The structure that best matches your budget is "{struct}". Rent is on average ${struct_rent} per month. 
      The complex age that best matches your budget is "{age} years". Rent is on average ${age_rent} per month.  
    Based on the median of this data, you should find a rental unit between ${report_range}\n'''
        return report
    
    
#print(Report("Fairfax", 90000, "Studio"))

print(f"\nWelcome to HermitKeys -- the easy breezy way to find your next home!")
income = input("What is your annual income?       ")
unit_list = ["Studio", "1 Bedroom", "1 Bedroom/Den", "2 Bedrooms", "2 Bedrooms/Den", "3 Bedrooms", "3 Bedrooms/Den", "4 Bedrooms"]
found = False
unit = ""
while found == False:
    unit = input(f'''Choose one of the following (type it exactly):
        {unit_list[0]}
        {unit_list[1]}
        {unit_list[2]}
        {unit_list[3]}
        {unit_list[4]}
        {unit_list[5]}
        {unit_list[6]}
        {unit_list[7]}   ''')
    if unit in unit_list:
        found = True
        print(Report("Fairfax", int(income), unit))