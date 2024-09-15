# Travel Planning

class Travel:
    def __init__(self,country,type, winter_months,summer_months):
        self.country = country
        self.type = type
        self.winter_months =  winter_months
        self.summer_months =  summer_months
        
        
    def travel_info(self,month): 
        month = month.capitalize()
        if month in self.winter_months:
            print('It is a Winter Trip !!!!')
                        
        elif month in self.summer_months:
            print('It is a Summer Trip !!!!')
        else:
            print('Invalid Input')
                




month = input('Enter the month you want: ').capitalize()
country = input('Country Name: ')
Tour_type = input('Enter trip type (luxury or business): ')
winter_months =  ['October', 'November', 'December', 'January', 'February', 'March']
summer_months =  ['April', 'May', 'June', 'July', 'August', 'September']

tour = Travel(country,Tour_type,winter_months,summer_months)
tour.travel_info(month)


