# Locally Stationary Graph Processes Local Approximation
This script was employed to produce the graph partitioning outcomes as presented in [[1]](#1). It uses the NOAA weather dataset[[2]](#2) as its primary data source. In this representation, the NOAA graph is structured with 246 weather stations, which serve as the graph nodes, and encompasses 8,760 distinct realizations. The edge weights between nodes are determined using a Gaussian function, combined with a 7-NN (7-nearest neighbor) construction method.



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