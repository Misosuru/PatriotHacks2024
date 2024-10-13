from parser import *
import statistics

class Report:
    RECC_BUDGET = .30
    YEAR = 2023
    
    def __init__(self, county, income, unit):
        if (0 < income):
            self.income = int(income)
            self.county = county
            self.unit = unit
        else: 
            raise ValueError
        
    def set_inflation(self):
        inflate_dict = inflate_rate()
        inflation = 1
        for x in range(1,4):
            inflation *= 1 + int(inflate_dict[self.YEAR + 1])
        return inflation
    
    def create_budget(self):
        inflation = self.set_inflation()
        low_bound = self.income * self.RECC_BUDGET
        high_bound = self.income * (self.RECC_BUDGET + inflation)
        return low_bound, high_bound
    
    def find_options(self, low_dict, high_dict, pd_rent):
       options = "\nBased on your budget, your best options are: "
       #https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
       sorted_low = sorted(low_dict.items())
       sorted_high = sorted(high_dict.items())
       if (len(low_dict) == 0) and (len(high_dict) == 0):
           sorted_rent = sorted(pd_rent.items(), key=lambda val: (val[1], val[0]))
           return '''\nYour budget is too low to live comfortably in Fairfax County.
            The cheapest place to live is {sorted_rent[0][0]}.'''
       x = 0
       goal = 3
       if (len(low_dict) + len(high_dict) < 3):
           goal = len(low_dict) + len(high_dict)
       while x < goal:
            x += 1
            if len(low_dict) > x:
                district = sorted_low[x][1]
                rent = format(int(sorted_low[x][0]), ",")
                options += "\noption {x}:  {district} (Avg. Rent: ${rent})"
            elif len(high_dict) > x-len(low_dict):
                y = x-len(low_dict)
                district = sorted_low[y][1]
                rent = format(int(sorted_low[x][0]), ",")
                options += "\noption {x}:  {district} (Avg. Rent: ${rent})"
                rent_incrase = format(rent * self.set_inflation(), ",")
                options+='''\nPlease keep in mind that this district is very close to your budget!
                Inflation over the next 3 years will likely have your landlord increase rent to ${rent_increase}'''
       return options
            
    def find_pd_budget(self, low_bound, high_bound, pd_rent):
        pd_rent_items = pd_rent.items()
        valid_low = {}
        valid_high = {}
        for x in pd_rent:
            if (pd_rent[x][1] < low_bound):
                valid_low[pd_rent[x][1]] = x
            elif (pd_rent[x][1] < high_bound):
                valid_high[pd_rent[x][1]] = x
        pd_budget = "Based on that budget, you should look at these districts:"
        return self.find_options(valid_low, valid_high, pd_rent)
        
    def find_match(self, low_bound, high_bound, dicti):
        valid = {}
        for x in dicti:
            if (dicti[x][1] < low_bound) or (len(valid) < 2 and dicti[x][1] < high_bound):
                valid[x] = dicti[x][1]
            else:
                valid[0] = sorted(dicti)[0][0]
        valid.sort()
        me_match = valid.items()
        return me_match[0][0]
        
    def __str__(self):
        low_bound, high_bound = self.create_budget()
        pd_budget = self.find_pd_budget(low_bound, high_bound, r_pd_rent())
        vacant_units = format(r_unit_vacancy()[self.unit][0], ",")
        unit_rent = format(r_unit_rent()[self.unit][1], ",")
        struct = self.find_match(low_bound, high_bound, r_struct_rent())
        age = self.find_match(low_bound, high_bound, r_age_rent())
        struct_rent = format(r_struct_rent()[struct][1], ",")
        age_rent = format(r_age_rent[age][1],",")
        report_median = statistics.median([age_rent, struct_rent, unit_rent].sort())
        report = f'''To live in {self.county} with an annual income of ${self.income}, your budget should be 
        between ${low_bound:.2} and ${high_bound:.2}. {pd_budget}
        The average rent for a {self.unit} would be ${unit_rent:.2f}. There are {vacant_units} vacant {self.unit} units.
        The structure that best matches your budget is "{struct}". Rent is on average ${struct_rent} per month. 
        The complex age that best matches your budget is "{age}". Rent is on average ${age_rent}per month.  
        Based on the median of this data, you should find a rental unit around the price of ${report_median}'''
        return report
    
    
print(Report("Fairfax", 90000, "Studio"))