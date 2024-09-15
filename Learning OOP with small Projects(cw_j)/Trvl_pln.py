class Travel:
    def __init__(self, country, trip_type, winter_months, summer_months):
        self.country = country
        self.trip_type = trip_type
        self.winter_months = winter_months
        self.summer_months = summer_months

    def travel_info(self, month):
        month = month.capitalize()  # Capitalize the month for consistency
        if month in self.winter_months:
            print('It is a Winter Trip!')
        elif month in self.summer_months:
            print('It is a Summer Trip!')
        else:
            print('Invalid month or not in winter/summer months.')

month = input('Enter the month you want: ').capitalize()
country = input('Country Name: ')
trip_type = input('Enter trip type (luxury or business): ')
winter_months = ['October', 'November', 'December', 'January', 'February', 'March']
summer_months = ['April', 'May', 'June', 'July', 'August', 'September']

tour = Travel(country, trip_type, winter_months, summer_months)
tour.travel_info(month)
