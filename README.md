# Locally Stationary Graph Processes Local Approximation
This script was employed to produce the graph partitioning outcomes as presented in [[1]](#1). It uses the NOAA weather dataset [[2]](#2) as its primary data source. In this representation, the NOAA graph is structured with 246 weather stations, which serve as the graph nodes, and encompasses 8,760 distinct realizations. The edge weights between nodes are determined using a Gaussian function, combined with a 7-NN (7-nearest neighbor) construction method.


## Obtaining Results
To produce the results, execute the script via "main.m", which subsequently triggers the Python script named "main.py". This procedure was carried out on a computer running the Windows operating system, equipped with WSL (Windows Subsystem for Linux). The inclusion of WSL is due to the specific parallelization techniques, which necessitate Linux to effectively execute the Ricci flow community detection as detailed in [[3]](#3).

While the provided script demonstrates graph partitioning based on covariance using a specific dataset(NOAA), it can also be applied to other datasets using the same partitioning method. If you introduce appropriate data to the "data/input" directory, formatted similarly to "data/input/noaaGraph.mat"—a .mat file that contains the process covariance (Cx), the process itself named "noaaTemperature", the weight matrix (W), diagonal degree matrix (D), and Laplacian matrix (LG)—the script will generate results consistent with Algorithm 2 from [[1]](#1). Please note: the 'coord_data' is used exclusively for visualization purposes in MATLAB.

## Parameter Details for Ricci Flow & Modularity
Before diving into the main results, it's essential to understand the parameters that drive the Ricci flow, surgery with modularity, and other related algorithms. All parameters can be adjusted within the "main.m" script. Here are the main equations used for partitioning, along with an explanation of their hyperparameters:

1. Gaussian Function:
$$d(x)= \text{exp}\left(\frac{-x^2}{\sigma}\right)$$

> sigma: Variance parameter for the Gaussian. Adjust this parameter until the transformation of edge covariances results in a clear bell-shaped curve. Denoted as $\sigma$.

2. Probability Distribution Centered on Some Node [[3]](#3):
<img src="/images/prob_dist.png" alt="" style=""/>


>alpha: Determines the emphasis on the probability measure of each node, centered on that specific node. A smaller alpha places more emphasis on neighboring nodes. Denoted as $\alpha$.

> exp_power: Refers to the distance power used for exponentiation. Denoted as $p$.

3. Modularity:
For modularity partitioning algorithm used in surgery, please refer to the link in [[4]](#4).

> resolution: resolution in networkx.greedy_modularity_communities(). (Description acquired from [[4]](#4)) If resolution is less than 1, modularity favors larger communities. Greater than 1 favors smaller communities.

> best_n: best_n in networkx.greedy_modularity_communities(). In all the experiments, it is chosen as number of partitions desired. K = 7 in this case. (Description acquired from [[4]](#4)) A maximum number of communities above which the merging process will not stop. This forces community merging to continue after modularity starts to decrease until best_n communities remain. If None, don’t force it to continue beyond a maximum.

> cutoff: (Description acquired from [[4]](#4)) A minimum number of communities below which the merging process stops. The process stops at this number of communities even if modularity is not maximized. The goal is to let the user stop the process early. The process stops before the cutoff if it finds a maximum of modularity.

Note: To ensure the greedy_modularity_communities() function isn't overly restrictive, the cutoff input is left at its default value of 1.

> num_iter: Number of iterations on the flow process updating transformed covariance weights. Details can be found in [[3]](#3).

## Results
If successful, the script should produce the plots below.

<table width="100%">
<tr>
<th> Original NOAA Graph </th>
<th> Original NOAA Graph with Distance Info </th>
</tr>
<tr>
<td width="50%">


<img src="/images/orig_noaa_graph.png" alt="" style=""/>
<i>Plot displaying the initial graph prior to partitioning.</i>

</td>
<td width="50%">

<img src="/images/orig_noaa_graph_distance.png" alt="" style=""/>
<i>Plot displaying the initial graph, whose edge colors correspond to transformed covariance values. Notice how the values are clearly separated as a result of transformation.</i>

</td>
</tr>
<tr>
<th> Original NOAA Graph with Covarince Info </th>
<th> Original NOAA Graph after Ricci Flow </th>
</tr>
<tr>
<td width="50%">

<img src="/images/orig_noaa_graph_covariance.png" alt="" style=""/>
 <i>This plot showcases the original NOAA graph with edges colored according to covariance values.</i>

</td>
<td width="50%">

<img src="/images/orig_noaa_graph_ricci_distance.png" alt="" style=""/>
  <i>A visualization of the NOAA graph post-Ricci Flow application. Edge colors correspond to transformed covariance values, making partitions evident.</i>
</td>
</tr>

<tr>
<th> Original NOAA Graph Covariance Info after Ricci Flow </th>
<th> Resulting Partition </th>
</tr>
<tr>
<td width="50%">

<img src="/images/orig_noaa_graph_ricci_covariance.png" alt="" style=""/>

<i>Displays the NOAA graph with edges colored based on negative log-transformed covariance values post-Ricci Flow. Edges with diminished covariance values are more likely to be cut.</i>

</td>
<td width="50%">

<img src="/images/partitions.png" alt="" style=""/>
  
  <i>Illustrates the partitions as output by the algorithm. This division aligns with the US's climatic regions solely based on temperature data. Despite the West's diverse climate, the algorithm offers a plausible partitioning.</i>  
  
  See: [[5]](#5).


</td>
</tr>


</table>


This README.md has been created with the help of [ChatGPT](https://chat.openai.com).

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

<a id="5">[5]</a>
H. E. Beck, N. E. Zimmermann, T. R. McVicar, N. Vergopolan,
A. Berg, and E. F. Wood, “Present and future Koppen-Geiger climate ¨
classification maps at 1-km resolution,” Scientific data, vol. 5, no. 1, pp.
1–12, 2018.