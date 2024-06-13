import matplotlib.pyplot as plt

# Data
parallel_connections = [1, 4, 8]

amazon_plts = [487, 699, 926]
cnn_plts = [216, 237, 700]
wikipedia_plts = [20, 291, 345]
github_plts = [17, 342, 376]
nyt_plts = [268, 715, 924]
bing_plts = [200, 250, 378]

plt.figure(figsize=(10, 6))

# Plot for each website
plt.plot(parallel_connections, amazon_plts, marker='o', label='Amazon (HTTP/3)')
plt.plot(parallel_connections, cnn_plts, marker='o', label='CNN (HTTP/2)')
plt.plot(parallel_connections, wikipedia_plts, marker='o', label='Wikipedia (HTTP/2)')
plt.plot(parallel_connections, github_plts, marker='o', label='GitHub (HTTP/2)')
plt.plot(parallel_connections, nyt_plts, marker='o', label='New York Times (HTTP/2)')
plt.plot(parallel_connections, bing_plts, marker='o', label='Bing (HTTP/1.1)')

plt.xlabel('Number of Parallel Connections')
plt.ylabel('Page Load Time (ms)')
plt.title('Page Load Times vs. Number of Parallel Connections')
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig('plt_vs_connections.png')
plt.show()
