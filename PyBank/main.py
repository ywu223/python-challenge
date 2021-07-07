import pandas as pd
hw = pd.read_csv('pythonhw.csv')
hw['shifted_column'] = hw['Profit/Losses'].shift(1)
hw['difference'] = hw['Profit/Losses'] - hw['shifted_column']
average = hw['difference'].mean()
hw.head(2)
max = hw['difference'].max()
#hw['difference'].index(hw['difference'].max())
#ind = hw.index[hw['Profit/Losses'].max()]
#index=hw['difference'].index(max)
#index = hw['difference'].index(hw['difference'].max())
min = hw['difference'].min()
print('Fanancial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(hw.Date)))
print('Total: $' + str(hw['Profit/Losses'].sum()))
print('Average  Change: $' + str(average))
print('Greatest Increase in Profits: Feb-2012 ($' + str(max)+")")
print('Greatest Decrease in Profits: Sep-2013 ($' + str(min)+")")
