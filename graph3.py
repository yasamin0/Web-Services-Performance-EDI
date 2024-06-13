import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
websites = ['Amazon', 'CNN', 'Wikipedia', 'GitHub', 'New York Times', 'Bing']
requests = [1000, 2000]
concurrency = [10, 20]

# RPS data for each website, with rows corresponding to different websites and columns to different concurrency levels
rps_data = np.array([
    [36.84, 38.21],  # Amazon
    [137.36, 129.55],  # CNN
    [95.69, 101.98],  # Wikipedia
    [65.41, 73.43],  # GitHub
    [170.52, 310.98],  # New York Times
    [210.24, 360.47]  # Bing
])

fig, ax = plt.subplots()

# Define bar width and positions
bar_width = 0.35
bar_positions = np.arange(len(websites))

# Plot bars for each concurrency level
for i in range(len(concurrency)):
    ax.bar(bar_positions + i * bar_width, rps_data[:, i], bar_width, label=f'Concurrency {concurrency[i]}')

# Set the labels and title
ax.set_xlabel('Websites')
ax.set_ylabel('Requests Per Second (RPS)')
ax.set_title('Apache Benchmark Results')
ax.set_xticks(bar_positions + bar_width / 2)
ax.set_xticklabels(websites, rotation=45)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
