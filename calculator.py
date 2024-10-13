import parser

class Report:
    RECC_BUDGET = .30
    YEAR = 2023
    
    def __init__(self, county, income, unit):
        if (0 < income):
            self.income = income
            self.county = county
            self.unit = unit
        else: 
            raise ValueError
    
    def create_budget(self):
        inflation = pow(0.021,4) #need to change to a function that gets from parser
        low_bound = self.income * self.RECC_BUDGET
        high_bound = self.income * (self.RECC_BUDGET + inflation)
        return low_bound, high_bound
    
    def average_rent(self, rent_dict):
        sum = 0
        #check if what was gotten back isnt null, then do
        for x in rent_dict:
            sum += int(rent_dict[x])
        avg = sum/len(rent_dict)
        return avg
       
    def find_pd_budget(self, low_bound, high_bound, pd_rent):
        valid_low = []
        valid_high = []
        for x in pd_rent:
            if (pd_rent[x] < low_bound):
                valid_low.append(pd_rent[x])
            elif (pd_rent[x] < high_bound):
                valid_high.append(pd_rent[x])
        valid_low.sort()
        valid_high.sort()
        
    
    def __str__(self):
        unit_rent = average_rent(r_unit_rent())
        struct_rent = average_rent(r_struct_rent())
        low_bound, high_bound = create_budget()
        report = f'''With an annual income of {self.income}, your budget should be between {low_bound} and {high_bound}.
            Based on that budget, you should look at these districts:
                option 1:
                option 2:
                option 3:
        The average rent for a {self.unit} would be ${unit_rent:.2f}.
            You will have a higher chance of finding vacancies in:
                option 1:
                option 2:
                option 3: 
        The structure that best matches your budget is [blank]. 
            These have a [higher/lower] vacancy rate than those [taller/shorter] 
            than it. Rent is [annual rent], at a monthly rate of [amount]. 
        The complex age that best matches your budget is [blank]. 
            These have a [higher/lower] vacancy rate than those [older/younger] 
            than it. Rent is [annual rent], at a monthly rate of [amount]. '''
        return report