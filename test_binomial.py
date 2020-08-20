from binomial_tree import Binomial_Tree
import math

##############################    MAIN    ############################################

treeDepth = 5                           #For instance, a tree with three nodes would have a treeDepth of 2, one with 6 nodes would have a depth of 3, 10 nodes would have 4, and so on
time_step = 1/12                        #This is the unit of time that corresponds with one level in the tree. For instance a time_step of 1/12 is equivalent to one month
volatility = 0.2                        #annualized volatility
interest = 0.1                          #annualized risk free interest rate
starting_price = 100                    #price of stock at t=0
strike = 100                            #strike price of option
OptionType = "Call"                     #Put or call option
p_prime = .5 + interest*math.sqrt(time_step)/(2*volatility)
not_p_prime = 1 - p_prime
drift = math.sqrt(volatility)
u = (1 + drift * time_step) + volatility * math.sqrt(time_step)
v = (1 + drift * time_step) - volatility * math.sqrt(time_step)
u = 1 + volatility * math.sqrt(time_step)
v = 1 - volatility * math.sqrt(time_step)


x = Binomial_Tree()
x.create_tree(starting_price,treeDepth,u,v)
y = x.option_price(x.get_root(), p_prime, not_p_prime, interest, time_step, strike, OptionType)
x.print_tree_prices()
x.print_tree_option_vals()
print(y)
print("P_Prime: " + str(p_prime) + " Not P_Prime: " + str(not_p_prime)+ " U: " + str(u) + " V: " + str(v))
