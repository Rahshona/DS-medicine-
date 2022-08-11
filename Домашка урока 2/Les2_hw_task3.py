n = int(input('Enter any number of month:'))
my_seas_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
my_season_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
if n in my_seas_dict:
    print(f'{n} - from {my_season_list[n - 1]}')
    print(f'{n} - {my_seas_dict[n]}')
else:
    print('Err')