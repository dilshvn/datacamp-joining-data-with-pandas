# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country','date'], 
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)