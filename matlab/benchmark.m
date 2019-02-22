hs = [2970.0, 4933.0, 5960.0, 8428.0, 6609.0, 8074.0, 7972.0, 9416.0, 10002.0, 10031.0] / 1000;
tf = [3707.0, 13301.0, 19124.0, 17167.0, 13624.0, 13443.5, 15094.0, 17473.5, 19074.0, 20614.0] / 1000;
bar([hs; tf]');
xlabel('Number of connections');
ylabel('Latencies (ms)')
set(gca,'FontSize',20)
legend('handshake latency', 'transport latency');
print('figures/direct-latency','-depsc');

cpu_cli = [1 2];
cpu_ser = [1 2];
bar([cpu_cli; cpu_ser]');
xlabel('Number of connections');
ylabel('CPU usage (%)')
set(gca,'FontSize',20)
% ylim([27 31])
legend('client', 'server');
print('figures/direct-cpu','-depsc');



mem_cli = [29484, 29616, 29748, 29748, 29888, 30016, 30020, 30156, 30156, 30292] / 1024;
mem_ser = [29472, 29608, 29608, 29736, 29860, 29864, 30004, 30004, 30136, 30240] / 1024;
bar([mem_cli; mem_ser]');
xlabel('Number of connections');
ylabel('Memory (MB)')
set(gca,'FontSize',20)
ylim([27 31])
legend('client', 'server');
print('figures/direct-memory','-depsc');