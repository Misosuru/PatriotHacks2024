class Report:
    REC_BUDGET = .30
    YEAR = 2023
    
    def __init__(self, county, income, unit, structure = "Mid-Rise"):
        self.income = income
        self.county = county
        self.unit = unit
        self.structure = structure
    
    def createBudget(self, income):
        inflation = pow(0.021,4) #need to change to a function that gets from parser
        low_bound = income * self.REC_BUDGET
        high_bound = income * (self.REC_BUDGET + inflation)
        bounds = str(low_bound) + " and " + str(high_bound)
        return bounds
    
    def averageRent(self, rent_dict):
        sum = 0;
        #check if what was gotten back isnt null, then do
        for x in rent_dict:
            sum += int(rent_dict[x])
        avg = sum/len(rent_dict)
        return avg;
        #add up all values in for loop
        #divide by length
    
    
    
    def __str__(self):
        report = f'''With an annual income of {self.income}, your budget should be between [blah].
            Based on that budget, you should look at these districts:
                option 1:
                option 2:
                option 3:
        The average rent for a {self.unit} would be [unitrent].
            You will have a higher chance of finding vacancies in:
                option 1:
                option 2:
                option 3: 
        The average rent for a {self.structure} would be [structure rent].
             You will have a higher chance of finding vacancies in:
                option 1:
                option 2:
                option 3: 
        Complexes [this old] have a [higher/lower] vacancy rate than those [older/younger] than it,
            but rent is [math of rent], at a monthly rate of [amount]. You should look at 
            complexes [this old] that have an average rent of [blank], with a [blank]% vacancy rate.'''
        return report