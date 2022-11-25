# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')