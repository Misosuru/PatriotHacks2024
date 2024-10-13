import csv

# https://docs.python.org/3/library/csv.html

"""
LIST OF DICTIONARIES
 - buyer_map_dictionary
 - renter_vacancy_rate_dictionary
 - renter_district_vacancy_rate_dictionary
 - renter_age_vacancy_rate_dictionary
 - renter_supervisor_vacancy_rate_dictionary
 - renter_unit_vacancy_rate_dictionary
 - renter_structure_vacancy_rate_dictionary
 - renter_monthly_rent_dictionary
 - renter_age_monthly_rent_dictionary
 - renter_district_monthly_rent_dictionary
 - renter_supervisor_monthly_rent_dictionary
 - renter_unit_monthly_rent_dictionary
 - renter_structure_monthly_rent_dictionary
"""


"""
 !!! buyer_map_dictionary !!!
   key: TRACT
   values: [YEAR, TOTAL HOUSING UNITS, OCCUPIED HOUSING UNITS, LOW MARKET VALUE <500K, MID MARKET VALUE 500K to <1MIL, HIGH MARKET VALUE >1MIL]
 
   To access value of a tract: buyer_map_dictionary.get("<TRACT>")
       Ex: print(buyer_map_dictionary.get("415100"))
           OUTPUT: ['2023', '1651', '1629', '110', '726', '366']
"""
# this is like...a dictReader and is an object
buyer_map_dictReader = csv.DictReader(open("Map.csv"))
buyer_map_dictionary = {}
for row in buyer_map_dictReader:
    values = list(row.values())
    buyer_map_dictionary[row["TRACT"]] = values[1:len(values)]

# for key, value in buyer_map_dictionary.items():
#     print(f"{key}: {value}")

"""
 !!! renter_vacancy_rate_dictionary !!!
   key: YEAR
   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_vacancy_rate_dictionary.get("<YEAR>")
       Ex: print(renter_vacancy_rate_dictionary.get("2009"))
           OUTPUT: ['65571', '8.2']
"""
renter_vacancy_rate_dictReader = csv.DictReader(open("Total_Units_and_Vacancy_Rate.csv"))
renter_vacancy_rate_dictionary = {}
for row in renter_vacancy_rate_dictReader:
    values = list(row.values())
    renter_vacancy_rate_dictionary[row["Year"]] = values[1:len(values)]

# for key, value in renter_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_vacancy_rate_dictionary.get("2009"))

"""
 !!! renter_district_vacancy_rate_dictionary !!!
   keys (make sure it is exactly as shown): 
        Annandale
        Baileys
        Bull Run
        Fairfax
        Jefferson
        Lincolnia
        Lower Potomac
        McLean
        Mount Vernon
        Pohick
        Rose Hill
        Springfield
        Upper Potomac
        Vienna

   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_district_vacancy_rate_dictionary.get("<District>")
       Ex: print(renter_district_vacancy_rate_dictionary.get("Annadale"))
           OUTPUT: ['4009', '9.5']
"""
renter_district_vacancy_rate_dictReader = csv.DictReader(open("Planning_District_Vacancy_Rate.csv"))
renter_district_vacancy_rate_dictionary = {}
for row in renter_district_vacancy_rate_dictReader:
    values = list(row.values())
    renter_district_vacancy_rate_dictionary[row["District"]] = values[1:len(values)]

# for key, value in renter_district_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_district_vacancy_rate_dictionary.get("Annandale"))

"""
 !!! renter_age_vacancy_rate_dictionary !!!
   keys (make sure it is exactly as shown): 
       Less than 6
       6 to 10
       11 to 15
       16 to 20
       Over 20

   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_age_vacancy_rate_dictionary.get("<KEY>")
       Ex: print(renter_age_vacancy_rate_dictionary.get("Less than 6"))
           OUTPUT: ['10527', '17.2']
"""
renter_age_vacancy_rate_dictReader = csv.DictReader(open("Vacancy_Rate_by_Age.csv"))
renter_age_vacancy_rate_dictionary = {}
for row in renter_age_vacancy_rate_dictReader:
    values = list(row.values())
    renter_age_vacancy_rate_dictionary[row["Age"]] = values[1:len(values)]

# for key, value in renter_age_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_age_vacancy_rate_dictionary.get("Less than 6"))

"""
 !!! renter_supervisor_vacancy_rate_dictionary !!!
   keys (make sure it is exactly as shown): 
        Braddock
        Dranesville
        Franconia
        Hunter Mill
        Mason
        Mount Vernon
        Providence
        Springfield
        Sully

   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_supervisor_vacancy_rate_dictionary.get("<Supervisor>")
       Ex: print(renter_supervisor_vacancy_rate_dictionary.get("Braddock"))
           OUTPUT: ['5303', '3.3']
"""
renter_supervisor_vacancy_rate_dictReader = csv.DictReader(open("Supervisor_Vacancy_Rate.csv"))
renter_supervisor_vacancy_rate_dictionary = {}
for row in renter_supervisor_vacancy_rate_dictReader:
    values = list(row.values())
    renter_supervisor_vacancy_rate_dictionary[row["Supervisor"]] = values[1:len(values)]

# for key, value in renter_supervisor_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_supervisor_vacancy_rate_dictionary.get("Braddock"))

"""
 !!! renter_unit_vacancy_rate_dictionary !!!
   keys (make sure it is exactly as shown): 
        Studio/Efficiency
        1 Bedroom
        1 Bedroom/Den
        2 Bedrooms
        2 Bedrooms/Den
        3 Bedrooms
        3 Bedrooms/Den
        4 Bedrooms

   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_unit_vacancy_rate_dictionary.get("<Unit Type>")
       Ex: print(renter_unit_vacancy_rate_dictionary.get("1 Bedroom"))
           OUTPUT: ['33254', '6.4']
"""
renter_unit_vacancy_rate_dictReader = csv.DictReader(open("Unit_Type_Vacancy_Rate.csv"))
renter_unit_vacancy_rate_dictionary = {}
for row in renter_unit_vacancy_rate_dictReader:
    values = list(row.values())
    renter_unit_vacancy_rate_dictionary[row["Type"]] = values[1:len(values)]

# for key, value in renter_unit_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_unit_vacancy_rate_dictionary.get("1 Bedroom"))

"""
 !!! renter_structure_vacancy_rate_dictionary !!!
   keys (make sure it is exactly as shown): 
        Low-Rise
        Mid-Rise
        High-Rise
        Townhouse

   values: [UNITS, VACANCY RATE]
 
   To access value of a year: renter_structure_vacancy_rate_dictionary.get("<Structure Type>")
       Ex: print(renter_structure_vacancy_rate_dictionary.get("Low-Rise"))
           OUTPUT: ['59085', '5.2']
"""
renter_structure_vacancy_rate_dictReader = csv.DictReader(open("Structure_Type_Vacancy_Rate.csv"))
renter_structure_vacancy_rate_dictionary = {}
for row in renter_structure_vacancy_rate_dictReader:
    values = list(row.values())
    renter_structure_vacancy_rate_dictionary[row["Type"]] = values[1:len(values)]

# for key, value in renter_structure_vacancy_rate_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_structure_vacancy_rate_dictionary.get("Low-Rise"))

"""
 !!! renter_monthly_rent_dictionary !!!
   key: YEAR
   values: [UNITS, AVG MONTHLY RENT, PERCENT CHANGE]
 
   To access value of a year: renter_monthly_rent_dictionary.get("<YEAR>")
       Ex: print(renter_monthly_rent_dictionary.get("2009"))
           OUTPUT: ['1375', '2.5']
"""
renter_monthly_rent_dictReader = csv.DictReader(open("Avg_Monthly_Rent_by_Year.csv"))
renter_monthly_rent_dictionary = {}
for row in renter_monthly_rent_dictReader:
    values = list(row.values())
    renter_monthly_rent_dictionary[row["Year"]] = values[1:len(values)]

# for key, value in renter_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_monthly_rent_dictionary.get("2009"))

"""
 !!! renter_age_monthly_rent_dictionary !!!
    keys (make sure it is exactly as shown): 
        Less than One
        1 to 5
        6 to 10
        11 to 15
        16 to 20
        Over 20
   values: [UNITS, 2022 AVG MONTHLY RENT, 2023 AVG MONTHLY RENT, PERCENT CHANGE]
 
   To access value of a year: renter_age_monthly_rent_dictionary.get("<YEAR>")
       Ex: print(renter_age_monthly_rent_dictionary.get("Less than One"))
           OUTPUT: ['2186', '2407', '10.1']
"""
renter_age_monthly_rent_dictReader = csv.DictReader(open("Avg_Monthly_Rent_by_Age.csv"))
renter_age_monthly_rent_dictionary = {}
for row in renter_age_monthly_rent_dictReader:
    values = list(row.values())
    renter_age_monthly_rent_dictionary[row["Age"]] = values[1:len(values)]

# for key, value in renter_age_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_age_monthly_rent_dictionary.get("Less than One"))

"""
 !!! renter_district_monthly_rent_dictionary !!!
   keys (make sure it is exactly as shown): 
        Annandale
        Baileys
        Bull Run
        Fairfax
        Jefferson
        Lincolnia
        Lower Potomac
        McLean
        Mount Vernon
        Pohick
        Rose Hill
        Springfield
        Upper Potomac
        Vienna

   values: [UNITS, AVG MONTHLY RENT]
 
   To access value of a year: renter_district_monthly_rent_dictionary.get("<District>")
       Ex: print(renter_district_monthly_rent_dictionary.get("Annadale"))
           OUTPUT: ['4009', '1897']
"""
renter_district_monthly_rent_dictReader = csv.DictReader(open("Planning_District_Monthly_Rent.csv"))
renter_district_monthly_rent_dictionary = {}
for row in renter_district_monthly_rent_dictReader:
    values = list(row.values())
    renter_district_monthly_rent_dictionary[row["District"]] = values[1:len(values)]

# for key, value in renter_district_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_district_monthly_rent_dictionary.get("Annandale"))

"""
 !!! renter_supervisor_monthly_rent_dictionary !!!
   keys (make sure it is exactly as shown): 
        Braddock
        Dranesville
        Franconia
        Hunter Mill
        Mason
        Mount Vernon
        Providence
        Springfield
        Sully

   values: [UNITS, AVG MONTHLY RENT]
 
   To access value of a year: renter_supervisor_monthly_rent_dictionary.get("<Supervisor>")
       Ex: print(renter_supervisor_monthly_rent_dictionary.get("Braddock"))
           OUTPUT: ['5303', '2000']
"""
renter_supervisor_monthly_rent_dictReader = csv.DictReader(open("Supervisor_Monthly_Rent.csv"))
renter_supervisor_monthly_rent_dictionary = {}
for row in renter_supervisor_monthly_rent_dictReader:
    values = list(row.values())
    renter_supervisor_monthly_rent_dictionary[row["Supervisor"]] = values[1:len(values)]

# for key, value in renter_supervisor_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_supervisor_monthly_rent_dictionary.get("Braddock"))

"""
 !!! renter_unit_monthly_rent_dictionary !!!
   keys (make sure it is exactly as shown): 
        Studio/Efficiency
        1 Bedroom
        1 Bedroom/Den
        2 Bedrooms
        2 Bedrooms/Den
        3 Bedrooms
        3 Bedrooms/Den
        4 Bedrooms

   values: [UNITS, 2022 AVG MONTHLY RENT, 2023 AVG MONTHLY RENT, PERCENT CHANGE]
 
   To access value of a year: renter_unit_monthly_rent_dictionary.get("<Unit Type>")
       Ex: print(renter_unit_monthly_rent_dictionary.get("1 Bedroom"))
           OUTPUT: ['1755', '1825', '4']
"""
renter_unit_monthly_rent_dictReader = csv.DictReader(open("Unit_Type_Monthly_Rent.csv"))
renter_unit_monthly_rent_dictionary = {}
for row in renter_unit_monthly_rent_dictReader:
    values = list(row.values())
    renter_unit_monthly_rent_dictionary[row["Type"]] = values[1:len(values)]

# for key, value in renter_unit_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_unit_monthly_rent_dictionary.get("1 Bedroom"))

"""
 !!! renter_structure_monthly_rent_dictionary !!!
   keys (make sure it is exactly as shown): 
        Low-Rise
        Mid-Rise
        High-Rise
        Townhouse

   values: [UNITS, 2022 AVG MONTHLY RENT, 2023 AVG MONTHLY RENT, PERCENT CHANGE]
 
   To access value of a year: renter_structure_monthly_rent_dictionary.get("<Structure Type>")
       Ex: print(renter_structure_monthly_rent_dictionary.get("Low-Rise"))
           OUTPUT: ['1857', '1907', '2.7']
"""
renter_structure_monthly_rent_dictReader = csv.DictReader(open("Structure_Type_Monthly_Rent.csv"))
renter_structure_monthly_rent_dictionary = {}
for row in renter_structure_monthly_rent_dictReader:
    values = list(row.values())
    renter_structure_monthly_rent_dictionary[row["Structure"]] = values[1:len(values)]

# for key, value in renter_structure_monthly_rent_dictionary.items():
#     print(f"{key}: {value}")

# print(renter_structure_monthly_rent_dictionary.get("Low-Rise"))

"""
 !!! annual_inflation_dictionary !!!
   key: YEAR
   values: [PERCENT CHANGE]
 
   To access value of a year: annual_inflation_dictionary.get("<YEAR>")
       Ex: print(annual_inflation_dictionary.get("2010"))
           OUTPUT: ['1.6']
"""
annual_inflation_dictReader = csv.DictReader(open("Annual_Inflation_Rate.csv"))
annual_inflation_dictionary = {}
for row in annual_inflation_dictReader:
    values = list(row.values())
    annual_inflation_dictionary[row["Year"]] = values[1]

# for key, value in annual_inflation_dictionary.items():
#     print(f"{key}: {value}")

# print(annual_inflation_dictionary.get("2010"))