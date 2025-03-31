#-----------------------------------------------------------------------------------
### Matplotlib practice:
#-----------------------------------------------------------------------------------

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#plt.plot(year, pop)
#plt.scatter(year, pop)

#---

#values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
#plt.hist(values, bins=3)

#---

year2 = [1950, 1951, 1952, 2100]
pop2 = [2.538, 2.57, 2.62, 10.85]

year2 = [1800, 1850, 1900] + year2
pop2 = [1.0, 1.262, 1.650] + pop2

plt.plot(year2, pop2)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
            ['0', '2B', '4B', '6B', '8B', '10B'])

#plt.show()



#-----------------------------------------------------------------------------------
### Dictionaries & Pandas:
#-----------------------------------------------------------------------------------

pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]
ind_alb = countries.index("albania")

#print(ind_alb)
#print(pop[ind_alb])

world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
#print(world["albania"])

world["sealand"] = 0.000027
#print(world)
#print("sealand" in world)

world["sealand"] = 0.000028
#print(world)

del(world["sealand"])
#print(world)


# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
#print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
#print(europe)


import pandas as pd
dict = {
    "Country:":["Brazil", "Russia", "India", "China", "South Africa"],
    "Capital:":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "Area:":[8.516, 17.10, 3.286, 9.597, 1.221],
    "Population:":[200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)