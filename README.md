# Project: Airline Revenue Management using Markov Decision Process

This is a project for the UBC course Decision Analysis under Uncertainty. The goal of this project is to help a theoretical airline company to decide number of tickets it should sell in order to maximize profits. Concepts of markov decision making process is applied in this project.

### Introduction:
Consider the airline company is operating a flight with 100 seats available, and it's 15 days until flight depature. Days until Flight Departure, Price, Demand mean are given in the Excel file (Solution Output.xlsx). In addition, actual demand is either the mean, one less, or one more, each with 1/3 probability.

### Mathematics Formulations:
A general form of bellman equation for each state s, at each period t is as follows:
<p align = 'center'>
<img src = 'https://github.com/vivianddyu/markovdecisionprocess/blob/main/data/bellman_1.PNG?raw=true'>
</p>
For the project problem, let s denotes number of seats remaining, d denotes actual demand for the day, and a denotes number of seats sold (ie: action taken) on that day. Below is the bellman equation for t = 15 days to go, with a request of 12 tickets at the $150 price for that day:

<p align = 'center'>
<img src = 'https://github.com/vivianddyu/markovdecisionprocess/blob/main/data/bellman_2.PNG?raw=true'>
</p>

### Results:
The main.py file generates 1 Excel file, where **optimal action** and its related **optimal action value** are respectively stored in different sheets.