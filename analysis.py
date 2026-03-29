# This script is a Python implementation of my research paper on SSRN.
# I am going to be using basic logic to see how Tourism affects the GDP.

def run_montenegro_report(year, tourism_percent, gdp_growth):
    """
    This function takes data from my paper and gives an automated 
    economic status update.
    """
    print(f"--- Processing Data for Year: {year} ---")
    
    # In my SSRN paper, I argued that high tourism reliance is a risk and therefore we should not depend fully on it.
    # Here, setting a 20% limit is to check this risk automatically.
    
    threshold = 20.0
    
    if tourism_percent > threshold:
        status = "CRITICAL DEPENDENCY"
        advice = "We need to diversify into Agriculture or ICT sectors."
    else:
        status = "HEALTHY BALANCE"
        advice = "The economy is stable, but we must stay cautious."

    # Checking if the economy is growing or shrinking (like in 2020 COVID era)
    if gdp_growth < 0:
        performance = "Negative Growth (Recession)"
    else:
        performance = "Positive Growth (Recovery)"

    # Outputting the results in a readable format
    print(f"Current Status: {status}")
    print(f"GDP Movement: {performance}")
    print(f"My Research Recommendation: {advice}")
    print("-" * 30)


#TESTING WITH REAL DATA FROM MY RESEARCH
# 2019: Before COVID, tourism was very high.
run_montenegro_report(2019, 25.1, 4.1)

# 2020: COVID-19 hit Montenegro hard so the GDP dropped a lot.
# I mentioned this drop specifically in my paper.
run_montenegro_report(2020, 7.5, -15.3)

# 2023: The recovery phase.
run_montenegro_report(2023, 24.5, 6.0)

 
# I want to add more data points like Debt-to-GDP ratio later as I learn more Python libraries like Pandas.
