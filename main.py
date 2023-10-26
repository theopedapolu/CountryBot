# Theophilus Pedapolu
# Chatbot Assignment
# April 3, 2019
# Honor Code: I have neither given nor received help on this exam

# read in the data about each country
inFile = open("Countries.txt",'r')
fileLines = inFile.readlines()
countries = []

# place the data in a 2D list
for line in fileLines:
  linArr = line.split("\t")
  countries.append(linArr)


# function to find the country that matches with the user preferences the best by using Manhattan Distance
def minError(userData):
  global countries
  distance = 1e20
  index = 0
  # Loops through all countries and finds the one with the minimal distance
  for k in range(len(countries)):
    country = countries[k]
    sum = 0
    for i in range(len(userData)):
      sum += abs(float(userData[i]) - float(country[i+1]))
    if (sum < distance):
      distance = sum
      index = k 
  return countries[index] # returns a list containing information about this country




def main():  

  # Introduction 
  print("Welcome! I am Country Bot 100.\n")
  print("So, you want to move to a new country, I see. Don't worry, I'll help you find which country is the best for you. You just have to answer a few questions.\n")

  # Questions that the user answers to gauge their preferences
  temp = input("What outside temperature do you like best (in  °C): \n")
  print("\n\nFor the next set of statements, answer on a scale from 1-10, with 1 meaning you completely disagee with the statement and 10 meaing that you completely agree with the statement.\n")
  
  lifeExp = input("I would like to go to a country with very high life expectency: \n")

  popDensity = input("I would like to go to country with a densely-packed population:\n")

  develop = input("I would like to go to a country that is completely developed and urbanized: \n")

  healthCare = input("I would like to go to a country with the best healthcare system, including high government expeditures on healthcare and coverage. (Note that a 10 usually means a universal healthcare system and higher taxes): \n")

  incomeTax = input("The country I go to should have high income taxes to support public and governmental services:\n")

  education = input("The country I go to should have a strong education system, both in secondary schooling and universities:\n")

  crimeIndex = input("I can tolerate having a high crime rate in the country I go to: \n ")

  COL = input("The cost of living in the country I go to, including property rates, rent, supermarket prices, and other consumer markets, can be high: \n")

  # Place user preferences in a list
  userInputs = [healthCare, temp, lifeExp, COL, popDensity, develop, education, incomeTax, crimeIndex]
  
  # Find the country that matches best with the user preferences
  countryData = minError(userInputs)
  
  # Prints the results, including the country's name and information
  print("\n\nYou should go to " + countryData[0] + "! It is the best fit for you. Here is some data about " + countryData[0] + ". All the data (except for temperature) is on a scale from 1-10 \n")

  print("Health Care Index: " + countryData[1])

  print("Average Annual Temperature: " +  countryData[2])

  print("Life Expectency: "  + countryData[3])
  
  print("Cost of Living: "  + countryData[4])

  print("Population Density: "  + countryData[5])

  print("Human Development Index: "  + countryData[6])

  print("Education Index: "  + countryData[7])

  print("Income Tax Rate: "  + countryData[8])

  print("Crime Index: "  + countryData[9])

  print("\nPlease consult the user documentation if you have any questions about any of these metrics.\n")

  print("Thank you for using Country Bot 100! Have fun in " + countryData[0])



main()