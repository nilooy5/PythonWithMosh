def age_risk():
    try:
        age = int(input('Age: '))
        income = 2000
        risk = income/age
        print(risk)
    except ZeroDivisionError:
        print('age cannot be 0.')
    except ValueError:
        print('value error')