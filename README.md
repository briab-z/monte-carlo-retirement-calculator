# Monte Carlo Retirement Calculator
This is a retirement calculator built in python under the guidance of my mentor Mr. Ron Choi.

I took historical data from the S&P, 10-year Treasury Yield, and the Consumer Price Index and generated a correlation matrix. Then, I used the numpy library to create a Cholesky decomposition of this matrix. Finally, I again used numpy to generate random decimals and create an array of correlated random sequences.

The calculator asks basic questions such as sex, seed deposit, annual deposit, and portfolio composition. Then, it generates a monte carlo simulation using 1000 random sequences based on the data. It assumes that the user will live off their annual returns until their death, which must be at least 70% of their annual salary. The calculator then makes an estimate with 95% certainty to guess the correct retirement age.

Finally, the calculator uses matplotlib to visualize the data.

Further steps in this project would be using less generalizations, gathering more data, and accounting for black swan events.
