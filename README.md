# Locally Stationary Graph Processes Local Approximation
This script was employed to produce the graph partitioning outcomes as presented in [[1]](#1). It uses the NOAA weather dataset [[2]](#2) as its primary data source. In this representation, the NOAA graph is structured with 246 weather stations, which serve as the graph nodes, and encompasses 8,760 distinct realizations. The edge weights between nodes are determined using a Gaussian function, combined with a 7-NN (7-nearest neighbor) construction method.


## Obtaining Results
To produce the results, execute the script via "main.m", which subsequently triggers the Python script named "main.py". This procedure was carried out on a computer running the Windows operating system, equipped with WSL (Windows Subsystem for Linux). The inclusion of WSL is due to the specific parallelization techniques, which necessitate Linux to effectively execute the Ricci flow community detection as detailed in [[3]](#3).

While the provided script demonstrates graph partitioning based on covariance using a specific dataset(NOAA), it can also be applied to other datasets using the same partitioning method. If you introduce appropriate data to the "data/input" directory, formatted similarly to "data/input/noaaGraph.mat"—a .mat file that contains the process covariance (Cx), the process itself named "noaaTemperature", the weight matrix (W), diagonal degree matrix (D), and Laplacian matrix (LG)—the script will generate results consistent with Algorithm 2 from [[1]](#1). Please note: the 'coord_data' is used exclusively for visualization purposes in MATLAB.

Other parameters related to Ricci flow, surgery with modularity etc., can be found in "main.m", if it is necessary to change the parameters. Before proceeding let us introduce which equations the parameters correspond to three subequations or submodules:

* Gaussian Function:
$$d(x)= \text{exp}(\frac{-x^2}{\sigma})$$

* Probability Distribution Centered on Some Node [[3]](#3):
<img src="/images/prob_dist.png" alt="" style="height: 100px; width:100px;"/>



> sigma: Variance parameter for the Gaussian. This parameter should be adjusted such that at least the bell shape is observed when edge covariances are transformed for better separation. 
> alpha: Parameter denoting how the measure on each node centered on that certain node.
> exp_power: Distance power for exponentiation.

## Results
If successful, the script should produce the plots below. Notice how 

## References
<a id="1">[1]</a> 
A. Canbolat and E. Vural,  
“Locally stationary graph processes,”
arXiv preprint arXiv:2309.01657, 2023.

<a id="2">[2]</a> 
A. Arguez, I. Durre, S. Applequist, R. S. Vose, M. F. Squires, X. Yin,
R. R. Heim, and T. W. Owen, “NOAA’s 1981-2010 U.S. climate
normals: An overview,” Bulletin of the American Meteorological Society,
vol. 93, no. 11, pp. 1687 – 1697, 2012

<a id="3">[3]</a> 
C. C. Ni, Y. Y. Lin, F. Luo, and J. Gao, “Community detection on
networks with Ricci flow,” Scientific Reports, 2019.