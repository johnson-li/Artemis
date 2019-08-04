dns = [14.3975+4.4748  14.3975+30.8457 13.477 34.77];

% bar([14.3975+4.4748  14.3975+30.8457], 0.5)
% % legend('DNS', 'Artemis', 'location', 'northwest')
% set(gca,'FontSize',24)
% ylabel('Connection setup latency (ms)')
% % set(gca,'XtickLabel',{'\begin{tabular}{c} DNS \\ cache hit \end{tabular}'; '\begin{tabular}{c} DNS \\ cache miss \end{tabular}'; '\begin{tabular}{c} Artemis \\ optimal \end{tabular}'; '\begin{tabular}{c} Artemis \\ non-optimal \end{tabular}'}, 'TickLabelInterpreter', 'latex')
% set(gca, 'XtickLabel', {'cache hit'; 'cache miss'})
% pbaspect([2 2 1])
% ylim([0 50])
% % set(gca,'XTickLabelRotation',45)
% print('figures/setup-latency-dns','-depsc')
% 
% bar([13.477 34.77], 0.5)
% % legend('DNS', 'Artemis', 'location', 'northwest')
% set(gca,'FontSize',24)
% ylabel('Connection setup latency (ms)')
% % set(gca,'XtickLabel',{'\begin{tabular}{c} DNS \\ cache hit \end{tabular}'; '\begin{tabular}{c} DNS \\ cache miss \end{tabular}'; '\begin{tabular}{c} Artemis \\ optimal \end{tabular}'; '\begin{tabular}{c} Artemis \\ non-optimal \end{tabular}'}, 'TickLabelInterpreter', 'latex')
% set(gca, 'XtickLabel', {'optimal'; 'non-optimal'})
% pbaspect([2 2 1])
% % set(gca,'XTickLabelRotation',45)
% ylim([0 50])
% print('figures/setup-latency-artemis','-depsc')

% bar([23.36 17.25; 23.36 17.25])
bar([4.4748*0.83+30.8457*0.17+14.3975 34.77*0.177+13.4777*0.823 16.86; 14.40 14.40 16.86; 4.4748*0.83+30.8457*0.17+14.3975+14.40 34.77*0.177+13.4777*0.823+14.40 16.86+16.86;])
legend('DNS', 'Artemis', 'Anycast', 'location', 'northwest')
set(gca,'FontSize',24)
ylabel('Latency (ms)')
set(gca, 'XtickLabel', {'\begin{tabular}{c} Connection \\ setup latency \end{tabular}'; 'RTT'; '\begin{tabular}{c} Query \\ latency \end{tabular}'}, 'TickLabelInterpreter', 'latex')
pbaspect([2 1 1])
% set(gca,'XTickLabelRotation',45)
ylim([0 43])
print('figures/setup-latency-cmp','-depsc')