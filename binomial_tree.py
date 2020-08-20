import math

class Binomial_Tree:

    class binomial_node:

        def __init__(self, value):
            self.value = value
            self.prev_up = None
            self.prev_down = None
            self.up = None
            self.down = None
            self.option_val = 0
            self.name = 0


    def __init__(self):
        self.root = None
        self.size = 0


    def create_tree(self, start_stock_val, treeDepth, u, v):
        #This function builds the tree by first creating the first two rows (or just the first or no rows depending on
        #the size of treeDepth). This function then uses a while loop to instantiate the other nodes and their values in
        #the tree.

        #Error Handling if given bad inputs
        if treeDepth < 1:
            raise ValueError("treeDepth must be at least 1")
        if start_stock_val <= 0:
            raise ValueError("start_stock_val must be greater than 0")
        if ((u < 0) or (v<0)):
            raise ValueError("u and v cannot be negative")

        #Instantiate the root of the tree and if the size of the tree is only 1, then exit
        nameCounter = 0 #This is for node.name
        self.root = self.binomial_node(start_stock_val)
        root = self.root
        number_of_steps = treeDepth - 1
        self.size = treeDepth
        root.name = 1
        if treeDepth == 1:
            return 0

        #The following instantiates the second level of the tree and links it with the first
        nameCounter += 1        #This is for node.name
        root.up = self.binomial_node(root.value*u)
        root.up.prev_down = root
        root.down = self.binomial_node(root.value*v)
        root.down.prev_up = root
        root.up.name = 2        #Set name for the top node in the second row
        root.down.name = 3      #Set name for the bottom node in the second row
        current_node = root.up   #This line moves the current node so that it is the top node in the second row
        count_build = 2

        #This while loop instantiates the rest of the tree with the remaining nodes and their possible stock prices
        #The loop starts with R2N1 (Row 2 Node 1), creates R3N1 and R3N2, proceeds to R2N2 and creates R3N3
        #Then the loop moves to R3N1, creates R4N1 and R4N2, proceeds to R3N2 and creates R4N3, and then proceeds
        #to R3N3 and creates R4N4. Then the cycle begins again starting with R4N1 and running to completion
        while count_build <= number_of_steps:

            count_nav_vert = 1  #count_nav_vert is a counter variable that keeps track
            while count_nav_vert <= count_build:
                if count_build == 2:
                    current_node.up = self.binomial_node(current_node.value*u)
                    current_node.up.prev_down = current_node
                    current_node.down = self.binomial_node(current_node.value * v)
                    current_node.down.prev_up = current_node
                    current_node.down.prev_down = current_node.prev_down.down
                    current_node.up.name = 4
                    current_node.down.name = 5
                    current_node = current_node.prev_down.down
                    current_node.up = current_node.prev_up.up.down
                    current_node.down = self.binomial_node(current_node.value * v)
                    current_node.down.prev_up = current_node
                    current_node.down.name = 6
                    nameCounter = 6
                    count_nav_vert = 3
                else:
                    if count_nav_vert == 1:
                        current_node.up = self.binomial_node(current_node.value*u)
                        current_node.up.prev_down = current_node
                        current_node.down = self.binomial_node(current_node.value*v)
                        current_node.down.prev_up = current_node
                        current_node.down.prev_down = current_node.prev_down.down
                        nameCounter += 1
                        current_node.up.name = nameCounter
                        current_node = current_node.prev_down.down
                    elif count_nav_vert == count_build:
                        current_node.up = current_node.prev_up.up.down
                        current_node.down = self.binomial_node(current_node.value*v)
                        current_node.down.prev_up = current_node
                        nameCounter +=1
                        current_node.up.name = nameCounter
                        nameCounter +=1
                        current_node.down.name = nameCounter
                    else:
                        current_node.up = current_node.prev_up.up.down
                        current_node.down = self.binomial_node(current_node.value*v)
                        current_node.down.prev_up = current_node
                        current_node.down.prev_down = current_node.prev_down.down
                        nameCounter += 1
                        current_node.up.name = nameCounter
                        current_node = current_node.prev_down.down
                    count_nav_vert += 1

            count_nav_diag = 1
            current_node = root
            while count_nav_diag <= count_build:
                current_node = current_node.up
                count_nav_diag += 1

            count_build += 1


    def get_root(self):
        #Return the root
        return self.root


    def print_tree_option_vals(self):
        #This function prints the name of each node and the corresponding value of the option at that node

        if (self.size > 1) and (self.root.option_val == 0):
            raise Exception("No option price data available - Binomial_Tree.option_price() needs to be called first")
        tree_size = self.size
        count = 2
        current_node = self.root
        print([[current_node.name, current_node.option_val]])
        current_node = current_node.up
        while count <= tree_size:
            entries = []
            count_nav_vert = 1
            while count_nav_vert <= count:
                entries.append([current_node.name, current_node.option_val])
                if count_nav_vert == count:
                    current_node == self.root
                else:
                    current_node = current_node.prev_down.down
                count_nav_vert += 1
            print(entries)

            count_nav_diag = 1
            current_node = self.root
            while count_nav_diag <= count:
                current_node = current_node.up
                count_nav_diag += 1
            count += 1


    def print_tree_prices(self):
        # This function prints the name of each node and the corresponding stock price at that node

        tree_size = self.size
        count = 2
        current_node = self.root
        print([[current_node.name, current_node.value]])
        current_node = current_node.up
        while count <= tree_size:
            entries = []
            count_nav_vert = 1
            while count_nav_vert <= count:
                entries.append([current_node.name, current_node.value])
                if count_nav_vert == count:
                    current_node == self.root
                else:
                    current_node = current_node.prev_down.down
                count_nav_vert += 1
            print(entries)

            count_nav_diag = 1
            current_node = self.root
            while count_nav_diag <= count:
                current_node = current_node.up
                count_nav_diag += 1
            count += 1


    def option_price(self, node, p_prime, not_p_prime, interest, time_step, strike, OptionType):
        #This function calculates the value of a European call or put option
        if self.size == 1:
            return max(self.root.value - strike, 0)
        current_node = node
        if current_node.up.up is None:
            if OptionType == "Call":
                if current_node.up.value > strike:
                    payoff_up = current_node.up.value - strike
                else:
                    payoff_up = 0
                if current_node.down.value > strike:
                    payoff_down = current_node.down.value - strike
                else:
                    payoff_down = 0
            elif OptionType == "Put":
                if current_node.up.value < strike:
                    payoff_up = strike - current_node.up.value
                else:
                    payoff_up = 0
                if current_node.down.value < strike:
                    print(str(strike) + " " + str(current_node.down.name) + " " + str(current_node.down.value))
                    payoff_down = strike - current_node.down.value
                else:
                    payoff_down = 0
            else:
                raise Exception("Valid OptionTypes are Calls and Puts")

            current_node.option_val = (math.exp(-1 * interest * time_step)) * (p_prime * payoff_up + not_p_prime * payoff_down)
            return current_node.option_val
        else:
            if ((current_node.up.option_val ==0) and (current_node.down.option_val==0)):
                current_node.option_val = (math.exp(-1 * interest * time_step)) * (p_prime * self.option_price(current_node.up, p_prime,
                not_p_prime, interest, time_step, strike, OptionType) + not_p_prime * self.option_price(current_node.down, p_prime, not_p_prime, interest, time_step, strike, OptionType))
                return current_node.option_val
            elif ((current_node.up.option_val !=0) and (current_node.down.option_val==0)):
                current_node.option_val = (math.exp(-1 * interest * time_step)) * (p_prime * current_node.up.option_val + not_p_prime * self.option_price(current_node.down, p_prime,not_p_prime, interest,time_step, strike, OptionType))
                return current_node.option_val
            elif ((current_node.up.option_val ==0) and (current_node.down.option_val!=0)):
                current_node.option_val = (math.exp(-1 * interest * time_step)) * (p_prime * self.option_price(current_node.up, p_prime,
                not_p_prime, interest, time_step, strike, OptionType) + not_p_prime * current_node.down.option_val)
                return current_node.option_val
            else:
                current_node.option_val = (math.exp(-1 * interest * time_step)) * (p_prime * current_node.up.option_val + not_p_prime * current_node.down.option_val)
                return current_node.option_val