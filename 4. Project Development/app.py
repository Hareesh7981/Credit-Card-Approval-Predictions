income = float(request.form["income"])
employment_days = float(request.form["employment_days"])

data = pd.DataFrame({
    "AMT_INCOME_TOTAL": [income],
    "YEARS_EMPLOYED": [employment_days]
})
