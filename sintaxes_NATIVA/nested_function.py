

def country(the_country):
    def features():
        from random import choice
        return choice([' é frio', ' é tropical', ' é lotado', ' não neva', ' é festivo', ' é úmido', ' não faz calor'])
    return the_country + features()


print(country(the_country='Alemanha'))
print(country(the_country='Brasil'))
print(country(the_country='Bélgica'))
