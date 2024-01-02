import matplotlib.pyplot as plt
import numpy as np

def simulate(n):
    A = [[1.0000, 0.0679, -0.1535], [0.0679, 1.0000, 0.5908], [-0.1535, 0.5908, 1.0000]]  # original correlation matrix

    vol_stocks = 0.1754
    vol_bonds = 0.0320
    vol_inflation = 0.0296

    mean_stocks = 0.1198
    mean_bonds = 0.0604
    mean_inflation = 0.04

    U = np.linalg.cholesky(A)  # creating cholesky decomposition of A
    R = np.random.normal(0, 1, size=(n, 3))  # normal random numbers
    Rc = R @ U  # Array of correlated random sequences

    # turning into percentages
    for i in range(len(Rc)):
        Rc[i][0] = Rc[i][0] * vol_stocks + mean_stocks
        Rc[i][1] = Rc[i][1] * vol_bonds + mean_bonds
        Rc[i][2] = Rc[i][2] * vol_inflation + mean_inflation

    return Rc

def line_plot(outcomes):
    plt.xlim(17, 85)
    plt.ylim(0, 3000000)
    for i in range(len(outcomes)):
        plt.plot(x, outcomes[i])
    plt.ylabel('Portfolio Amount')
    plt.show()

sex = input("Please enter your sex (M/F): ")
if sex == "M":
    death_age = 75
elif sex == "F":
    death_age = 80
seed = int(input("Please enter initial seed amount as an integer: "))
deposit = int(input("Please enter your annual deposit amount as an integer: "))
start_age = int(input("Please enter your current age: "))
x = np.arange(start_age, death_age)
stock_percentage = float(input("What percentage of your portfolio is stocks? (as a decimal): "))
bond_percentage = 1 - stock_percentage
annual_income = int(input("What is your annual income?: "))

outcomes = [] #big array of the sums of every simulation
ages = []

for j in range(1000):
    sum = seed
    sim = [] #array of the sums of one simulation
    sim_ages = []
    for i in range(start_age, death_age):
        sum += deposit
        Rc = simulate(1)
        returns = Rc[0][0] * stock_percentage * sum + Rc[0][1] * bond_percentage * sum
        returns = returns / (1 + Rc[0][2])
        sum += returns
        if (sum * 0.04 >= .7 * annual_income):
            sim_ages.append(i)
            sum *= 0.96
        sim.append(sum)
    outcomes.append(sim)
    ages.append(sim_ages)

retirement_ages = []
for i in range(len(ages)):
    for j in range(len(ages[i]) - 1, 0, -1):
        if (ages[i][j] != ages[i][j-1] + 1):
            retirement_ages.append(ages[i][j])
            break
        if (j == 1):
            retirement_ages.append(ages[i][j-1])
retirement_ages.sort()

for i in range(50):
    retirement_ages.pop()
print("With 95% certainty, you are able to retire at age: " + str(retirement_ages[len(retirement_ages)-1]))
line_plot(outcomes)


