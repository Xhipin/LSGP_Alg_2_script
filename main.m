% clc;
% clear;
% close all;
%% Initialize Variables
pyloc = 'main.py';

matstr = 'noaaGraph.mat';
input = 'input';
output = 'output';


inStr = ['data/', input, '/', matstr];


sigma = 50000;
alpha = 0.5;
exp_power = 2;
num_iter = 50;
resolution = 0.3;
best_n = 7;


savestr = ['covRicci_sigma_',num2str(sigma),'_alpha_',num2str(alpha),...
    '_exp_power_',num2str(exp_power),'_num_iter_', ...
    num2str(num_iter), '_resolution_',num2str(resolution),...
    '_best_n_',num2str(best_n),'.mat'];

outStr = ['data/', output, '/', savestr];
load(inStr);

if ~isfile(outStr)
    %% Create a WSL instance and push variables to python env
    cmd = sprintf('wsl python3 %s %s %s %f %f %f %d %f %d', pyloc, ...
        inStr, outStr, sigma, ...
        alpha, exp_power, num_iter, ...
        resolution, best_n);
    system(cmd);
else
    fprintf('Output folder exists!! Proceeding... \n');
end
%% Load Computed Data
load(outStr);


%% Plot
G = graph(W);


figure(1);
plot(G, "XData",coord_data(:,2), "YData", coord_data(:,1) ...
    ,"MarkerSize",3);
hold on;
title('Original NOAA Graph');

%% Embed Covariance to Edges
edgePairs = G.Edges{:,1};
edgeSize = size(edgePairs,1);

covExp = zeros(edgeSize,1);
dom = covExp;
for i = 1 : edgeSize
    idx = edgePairs(i,:);
    dom(i) = covNoaa(idx(1),idx(2));
    covExp(i) = exp(-covNoaa(idx(1),idx(2))^2/sigma);
end


figure(2);
plot(G, "XData",coord_data(:,2), "YData", coord_data(:,1) ...
    ,"MarkerSize",3,"LineWidth", 2, "EdgeCData", covExp);
hold on;
title('Original NOAA Graph with Covariance Info (Distance)');
colorbar

figure(3);
plot(G, "XData",coord_data(:,2), "YData", coord_data(:,1) ...
    ,"MarkerSize",3,"LineWidth", 2, "EdgeCData", dom);
hold on;
title('Original NOAA Graph with Covariance Info (Covariance)');
colorbar


%% Adjusted Ricci Weights
figure(5);
plot(G, "XData",coord_data(:,2), "YData", coord_data(:,1) ...
    ,"MarkerSize",3,"LineWidth", 2, "EdgeCData", ricciWeight);
hold on;
title('Original NOAA Graph with Ricci Distance');
colorbar
%% Clustered Graphs
figure(4);
hold on;
c = community_nodes;
for i = 1 : length(c)

    H = subgraph(G, c{i});
    plot(H, "XData",coord_data(c{i},2), "YData", coord_data(c{i},1) ...
        ,"MarkerSize",3,"LineWidth", 2, "NodeLabel", []);

end

title('NOAA Clusters');


%% Adjusted Ricci Squared Covariance
figure(6);
plot(G, "XData",coord_data(:,2), "YData", coord_data(:,1) ...
    ,"MarkerSize",3,"LineWidth", 2, "EdgeCData", covValue);
hold on;
title('Original NOAA Graph with Ricci Covariance');
colorbar