import networkx as nx
import numpy as np
import math

# matplotlib setting
import matplotlib.pyplot as plt

# load GraphRicciCuravture package
from GraphRicciCurvature.OllivierRicci import OllivierRicci
# load .mat files
import scipy.io
# push variables to python env
import sys

import surge

## Load Data
print(sys.argv)
inStr = sys.argv[1]
sigma = float(sys.argv[3])
alpha = float(sys.argv[4])
exp_power = float(sys.argv[5])
num_iter = int(sys.argv[6])

mat = scipy.io.loadmat(inStr)
W = mat['W']
D = mat['D']
LG = mat['LG']
Gnoaa = nx.from_numpy_array(W, create_using=nx.Graph)

if 'coord_data' in mat:
    coord_data = mat['coord_data']
    coord_data = np.fliplr(coord_data)
    
if 'noaaTemperature' in mat:
    noaaTemp = mat['noaaTemperature']
    covNoaa = np.cov(noaaTemp, bias = False)
elif 'Cx' in mat:
    covNoaa = mat['Cx']


## Create a distance metric from covariance
expNoaa = np.exp(-np.power(covNoaa,2)/sigma)

covAttr = dict()

for tpl in Gnoaa.edges():
    covAttr[tpl] = expNoaa[tpl]

## Set the attained parameters to weight
nx.set_edge_attributes(Gnoaa,covAttr,'weight')

## Run Ricci Flow algorithm
orf2 = OllivierRicci(Gnoaa, weight = 'weight', alpha= alpha, base=math.e, exp_power= exp_power, verbose="ERROR")
orf2.compute_ricci_flow(iterations=num_iter)
G_frc = orf2.G.copy()  # save an intermediate result


## Return to covariance domain with specified function
covValue = list()
ricciWeight = list()
weights = nx.get_edge_attributes(G_frc, "weight")
weight_max = 0
for w in weights.items():
    if w[1] > weight_max:
        weight_max = w[1]



for tpl in G_frc.edges():
    G_frc[tpl[0]][tpl[1]]['covValue'] = math.log(weight_max) - \
        math.log(G_frc[tpl[0]][tpl[1]]['weight'])
        
    covValue.append(G_frc[tpl[0]][tpl[1]]['covValue'])
    ricciWeight.append(G_frc[tpl[0]][tpl[1]]['weight'])


G_cut, c = surge.LSP_surgery(G_frc, weight = 'covValue', resolution = float(sys.argv[7]),\
 best_n = int(sys.argv[8]))

#import pdb
#pdb.set_trace()

# posdic = dict()
# i = 0
# for nde in Gnoaa.nodes():
#     posdic[nde] = coord_data[i,:]
#     i += 1

# nx.draw(G_cut, pos = posdic)
# plt.show()

## Save to MATLAB
for i in range(len(c)):
    x = c[i]
    x = [y+1 for y in x]
    c[i] = x


sdict = {'community_nodes': np.array(c, dtype = 'object')}
sdict['covNoaa'] = covNoaa
sdict['covValue'] = np.array(covValue)
sdict['ricciWeight'] = np.array(ricciWeight)

outStr = sys.argv[2]

scipy.io.savemat(outStr,sdict)

