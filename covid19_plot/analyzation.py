import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bs4

confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recovered = pd.read_csv('covid19_recovered.csv')

confirmed_new = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
confirmed_new = confirmed_new.groupby(confirmed_new['Country/Region']).aggregate('sum')

deaths_new = deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths_new = deaths_new.groupby(deaths_new['Country/Region']).aggregate('sum')

recovered_new = recovered.drop(['Province/State', 'Lat', 'Long'], axis=1)
recovered_new = recovered_new.groupby(recovered_new['Country/Region']).aggregate('sum')

confirmed_new = confirmed_new.T
deaths_new = deaths_new.T
recovered_new = recovered_new.T

new_cases = confirmed_new.copy()

for day in range(1, len(confirmed_new)):
    new_cases.iloc[day] = confirmed_new.iloc[day] - confirmed_new.iloc[day-1]

growth_rate = confirmed_new.copy()

for day in range(1, len(confirmed_new)):
    growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed_new.iloc[day - 1]) * 100

active_cases = confirmed_new.copy()

for day in range(0, len(confirmed_new)):
    active_cases.iloc[day] = confirmed_new.iloc[day] - deaths_new.iloc[day] - recovered_new.iloc[day]

overall_growth_rate = confirmed_new.copy()

for day in range(1, len(confirmed_new)):
    overall_growth_rate.iloc[day] = (active_cases.iloc[day] - active_cases.iloc[day - 1]) / active_cases.iloc[day - 1] * 100


death_rate = confirmed_new.copy()

for day in range(0, len(confirmed_new)):
    death_rate.iloc[day] = (deaths_new.iloc[day] / confirmed_new.iloc[day]) * 100

hospitalization_rate_estimate = 0.05

hospitalization_needed = confirmed_new.copy()

for day in range(0, len(confirmed_new)):
    hospitalization_needed.iloc[day] = active_cases.iloc[day] * hospitalization_rate_estimate

countries = ['Italy', 'US', 'India', 'France', 'Spain', 'China', 'United Kingdom']

ax = plt.subplot()
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('Covid-19_Total Confirmed Cases in Countries', color='white')


for country in countries:
    confirmed_new[country][30:].plot(label=country)

plt.legend(loc='upper left')
plt.show()

for country in countries:
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'Covid-19_Total Confirmed Cases day/day in {country}', color='white')
    confirmed_new[country].plot.bar()
    plt.show()

for country in countries:
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'Covid-19_Total Confirmed Cases Growth rate in {country}', color='white')
    growth_rate[country].plot.bar()
    plt.show()

ax = plt.subplot()
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('Covid-19_Total Death in Countries', color='white')


for country in countries:
    deaths_new[country].plot(label=country)

plt.legend(loc='upper left')
plt.show()

for country in countries:
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'Covid-19_Total Death rate in {country}', color='white')
    death_rate[country].plot.bar()
    plt.show()

"""
simulated_growth_rate = 0.03

dates = pd.date_range(start='4/22/2020', periods=40, freq='D')
dates = pd.Series(dates)
dates = dates.dt.strftime('%m/%d/%Y')

simulated = confirmed_new.copy()
simulated = simulated.append(pd.DataFrame(index=dates))

for day in range(len(confirmed_new), len(confirmed_new)+40):
    simulated.iloc[day] = simulated.iloc[day-1] * (1 + simulated_growth_rate)

for country in countries:
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'Future Simulation for {country}', color='white')
    simulated[country].plot()
    plt.show()

"""

# estimated_death_rate = 0.025
# estimated infected = deaths / estimated death rate
