import pandas as cleaner


data = {
    'Names':['Anna','Trisha','Nicole','Christine','Dianne','Lucy'],
    'Money':[200,800,920,400,None,600]
}

unsanitized_data = cleaner.DataFrame(data)

print(unsanitized_data)
print("----------------")

# fill out missing data
# use Money Mean
unsanitized_data.fillna(unsanitized_data['Money'].mean(),inplace=True)

print(unsanitized_data)


# Perform basic data analysis
print('--- Analysis ---')
print(unsanitized_data.describe())

# grouping 
money_allowance_groups = unsanitized_data.groupby(
    cleaner.cut(
        unsanitized_data['Money']
        ),observed=True
    ).count()

print(money_allowance_groups)

