import EoN
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
N = 300000
print('generating graph G with {} nodes'.format(N))
G = nx.fast_gnp_random_graph(N, 5./(N-1))
#In the below:
#'SS' means an individual susceptible to both diseases
#'SI' means susceptible to disease 1 and infected with disease 2
#'RS' means recovered from disease 1 and susceptible to disease 2.
#etc.
H = nx.DiGraph() #DiGraph showing spontaneous transitions
#(no interactions between indivdiuals required)
14
H.add_node('SS') #we actually don't need to include the 'SS' node in H.
H.add_edge('SI', 'SR', rate = 1) #An individual who is susceptible to disease
#1 and infected with disease 2 will recover
#from disease 2 with rate 1.
H.add_edge('IS', 'RS', rate = 1)
H.add_edge('II', 'IR', rate = 0.5)
H.add_edge('II', 'RI', rate = 0.5)
H.add_edge('IR', 'RR', rate = 0.5)
H.add_edge('RI', 'RR', rate = 0.5)
#In the below the edge (('SI', 'SS'), ('SI', 'SI')) means an
#'SI' individual connected to an 'SS' individual can lead to a transition in
#which the 'SS' individual becomes 'SI'. The rate of this transition is 0.18.
#
#Note that \texttt{IR} and \texttt{RI} individuals are more infectious than other
#individuals.
#
J = nx.DiGraph() #DiGraph showing induced transitions (require interaction).
J.add_edge(('SI', 'SS'), ('SI', 'SI'), rate = 0.18)
J.add_edge(('SI', 'IS'), ('SI', 'II'), rate = 0.18)
J.add_edge(('SI', 'RS'), ('SI', 'RI'), rate = 0.18)
J.add_edge(('II', 'SS'), ('II', 'SI'), rate = 0.18)
J.add_edge(('II', 'IS'), ('II', 'II'), rate = 0.18)
J.add_edge(('II', 'RS'), ('II', 'RI'), rate = 0.18)
J.add_edge(('RI', 'SS'), ('RI', 'SI'), rate = 1)
J.add_edge(('RI', 'IS'), ('RI', 'II'), rate = 1)
J.add_edge(('RI', 'RS'), ('RI', 'RI'), rate = 1)
J.add_edge(('IS', 'SS'), ('IS', 'IS'), rate = 0.18)
J.add_edge(('IS', 'SI'), ('IS', 'II'), rate = 0.18)
J.add_edge(('IS', 'SR'), ('IS', 'IR'), rate = 0.18)
J.add_edge(('II', 'SS'), ('II', 'IS'), rate = 0.18)
J.add_edge(('II', 'SI'), ('II', 'II'), rate = 0.18)
J.add_edge(('II', 'SR'), ('II', 'IR'), rate = 0.18)
J.add_edge(('IR', 'SS'), ('IR', 'IS'), rate = 1)
J.add_edge(('IR', 'SI'), ('IR', 'II'), rate = 1)
J.add_edge(('IR', 'SR'), ('IR', 'IR'), rate = 1)

return_statuses = ('SS', 'SI', 'SR', 'IS', 'II', 'IR', 'RS', 'RI', 'RR')
initial_size = 250
IC = defaultdict(lambda: 'SS')
15
for individual in range(initial_size): #start with some people having both
   IC[individual] = 'II'
for individual in range(initial_size, 5*initial_size): #and more with only
#the 2nd disease
    IC[individual] = 'SI'
print('doing Gillespie simulation')
t, SS, SI, SR, IS, II, IR, RS, RI, RR = EoN.Gillespie_simple_contagion(G, H,
J, IC, return_statuses,
tmax = float('Inf'))
plt.semilogy(t, IS+II+IR, '-.', label = 'Infected with disease 1')
plt.semilogy(t, SI+II+RI, '-.', label = 'Infected with disease 2')
plt.xlabel('$t$')
plt.ylabel('Number infected')
plt.legend()
plt.show()