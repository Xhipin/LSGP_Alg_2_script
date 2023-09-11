# Locally Stationary Graph Processes Local Approximation
This script was employed to produce the graph partitioning outcomes as presented in [[1]](#1). It uses the NOAA weather dataset [[2]](#2) as its primary data source. In this representation, the NOAA graph is structured with 246 weather stations, which serve as the graph nodes, and encompasses 8,760 distinct realizations. The edge weights between nodes are determined using a Gaussian function, combined with a 7-NN (7-nearest neighbor) construction method.


## Obtaining Results
To produce the results, execute the script via "main.m", which subsequently triggers the Python script named "main.py". This procedure was carried out on a computer running the Windows operating system, equipped with WSL (Windows Subsystem for Linux). The inclusion of WSL is due to the specific parallelization techniques, which necessitate Linux to effectively execute the Ricci flow community detection as detailed in [[3]](#3).

While the provided script demonstrates graph partitioning based on covariance using a specific dataset(NOAA), it can also be applied to other datasets using the same partitioning method. If you introduce appropriate data to the "data/input" directory, formatted similarly to "data/input/noaaGraph.mat"—a .mat file that contains the process covariance (Cx), the process itself named "noaaTemperature", the weight matrix (W), diagonal degree matrix (D), and Laplacian matrix (LG)—the script will generate results consistent with Algorithm 2 from [[1]](#1). Please note: the 'coord_data' is used exclusively for visualization purposes in MATLAB.

Other parameters related to Ricci flow, surgery with modularity etc., can be found in "main.m", if it is necessary to change the parameters. Before proceeding let us introduce equations for partitioning the graph that we change their hyperparameters via the script in MATLAB:

1. Gaussian Function:
$$d(x)= \text{exp}\left(\frac{-x^2}{\sigma}\right)$$

2. Probability Distribution Centered on Some Node [[3]](#3):
<img src="/images/prob_dist.png" alt="" style=""/>

3. Modularity:
For modularity partitioning algorithm used in surgery, please refer to the link in [[4]](#4).

> sigma: Variance parameter for the Gaussian. This parameter should be adjusted such that at least the bell shape is observed when edge covariances are transformed for better separation. $\sigma$ in 1. Gaussian Function.

>alpha: Parameter denoting how much the probability measure on each node centered on that certain node. Less alpha value creates more emphasis on neighboring nodes. $\alpha$ in 2. Probability Distribution Centered on Some Node.

> exp_power: Distance power for exponentiation. $p$ in 2. Probability Distribution Centered on Some Node.

> num_iter: Number of iterations on the flow process updating transformed covariance weights. Details can be found in [[3]](#3).

> resolution: resolution in networkx.greedy_modularity_communities(). (Description acquired from [[4]](#4)) If resolution is less than 1, modularity favors larger communities. Greater than 1 favors smaller communities.

> best_n: best_n in networkx.greedy_modularity_communities(). In all the experiments, it is chosen as number of partitions desired. (Description acquired from [[4]](#4)) A maximum number of communities above which the merging process will not stop. This forces community merging to continue after modularity starts to decrease until best_n communities remain. If None, don’t force it to continue beyond a maximum.

NOTE: In order not to restrict the greedy_modularity_communities() too much, we did not set cutoff input. Its default value is 1.

> cutoff: (Description acquired from [[4]](#4)) A minimum number of communities below which the merging process stops. The process stops at this number of communities even if modularity is not maximized. The goal is to let the user stop the process early. The process stops before the cutoff if it finds a maximum of modularity.

## Results
If successful, the script should produce the plots below.

<table>
<tr>
<th> Original NOAA Graph </th>
<th> Original NOAA Graph with Distance Info </th>
</tr>
<tr>
<td>

*Plot showing original graph before partitioning.

<img src="/images/orig_noaa_graph.png" alt="" style="height:300px;"/>
</td>
<td>

*Plot showing original NOAA graph, whose edge colors correspond to transformed covariance values.

<img src="/images/orig_noaa_graph_distance.png" alt="" style="height:300px;"/>

</td>
</tr>
<tr>
<th> Original NOAA Graph with Covarince Info </th>
<th> Bad </th>
</tr>

</table>


<!-- * Original Graph: Plot showing original graph before partitioning.
<img src="/images/orig_noaa_graph.png" alt="" style=""/> -->

## References
<a id="1">[1]</a> 
A. Canbolat and E. Vural, “Locally stationary graph processes,”
arXiv preprint arXiv:2309.01657, 2023.

<a id="2">[2]</a> 
A. Arguez, I. Durre, S. Applequist, R. S. Vose, M. F. Squires, X. Yin,
R. R. Heim, and T. W. Owen, “NOAA’s 1981-2010 U.S. climate
normals: An overview,” Bulletin of the American Meteorological Society,
vol. 93, no. 11, pp. 1687 – 1697, 2012

<a id="3">[3]</a> 
C. C. Ni, Y. Y. Lin, F. Luo, and J. Gao, “Community detection on
networks with Ricci flow,” Scientific Reports, 2019.

<a id="4">[4]</a>
[NetworkX greedy_modularity_communities](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html)
