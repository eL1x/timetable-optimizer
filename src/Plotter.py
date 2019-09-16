import matplotlib.pyplot as plt


class Plotter:
    def plot_cost_function(self, cost_function):
        plt.plot(cost_function)
        plt.xlabel('Number of iterations')
        plt.ylabel('Value of cost function')
        plt.title('Optimization process')
        plt.show()

