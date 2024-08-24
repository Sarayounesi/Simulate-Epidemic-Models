import networkx as nx
import matplotlib.pyplot as plt
import EoN

N = 10**5 # number of nodes
G = nx.barabasi_albert_graph(N, 5) # create a BA network
tmax = 20 # maximum time
iterations = 5 # number of simulations
tau = 0.1 # transmission rate
gamma = 1.0 # recovery rate
omega = 0.01 # loss of immunity rate
rho = 0.005 # initial fraction of infected nodes

for counter in range(iterations): # run simulations
   t, S, I, R = EoN.fast_SIR(G, tau, gamma, omega=omega, rho=rho, tmax=tmax)
if counter == 0:
   plt.plot(t, I, color='k', alpha=0.3, label='Simulation')
else:
   plt.plot(t, I, color='k', alpha=0.3)

plt.xlabel('$t$')
plt.ylabel('Number infected')
plt.legend()
plt.show()
