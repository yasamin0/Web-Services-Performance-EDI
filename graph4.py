import matplotlib.pyplot as plt
import numpy as np

# Data
websites = ['Amazon', 'CNN', 'Wikipedia', 'GitHub', 'New York Times', 'Bing']
nghttp_rps = [180, 200, 220, 195, 205, 230]
h2load_rps = [320, 350, 340, 310, 330, 360]

x = np.arange(len(websites))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, nghttp_rps, width, label='nghttp')
rects2 = ax.bar(x + width/2, h2load_rps, width, label='h2load')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Websites')
ax.set_ylabel('RPS')
ax.set_title('nghttp and h2load Results')
ax.set_xticks(x)
ax.set_xticklabels(websites)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
