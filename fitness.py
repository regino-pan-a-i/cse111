print()
from datetime import datetime

def main ():
    gender = input('Enter your gender (M or F): ')
    birthdate = input('Enter your birthdate (yyyy-mm-dd): ')
    height = float(input('Enter your height: '))
    weight = float(input('Enter your weight: '))
    age = compute_age(birthdate) 
    kg = kg_from_lb(weight)
    cm = cm_from_in(height)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)

    print(f'Age (years): {age}')
    print(f'Weight (kg): {kg:0.1f}')
    print(f'Height (cm): {cm:0.1f}')
    print(f'Body mass index: {bmi:0.1f}')
    print(f'Basal metabolic rate (kcal/day): {bmr:0.0f}')
    print()
    pass

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(weight):
    kg = weight * 0.45359237
    return kg

def cm_from_in(height):
    cm = height * 2.54
    return cm

def body_mass_index(kg, cm):
    bmi = (10000 * kg) / (cm ** 2) 
    return bmi    

def basal_metabolic_rate(gender, kg, cm, age):
    if gender.upper() == 'F':
        bmr = 447.593 + 9.247 * kg + 3.098 + cm - 4.330 * age    
    else:
        bmr = 88.362 + 13.397 * kg + 4.799 * cm - 5.677 * age
        
    return bmr

main()