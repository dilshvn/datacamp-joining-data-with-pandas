# Merge movies and financials with a left join
movies_financials = movies.merge(financials, how='left', on='id')