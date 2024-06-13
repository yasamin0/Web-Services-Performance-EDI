import matplotlib.pyplot as plt

# Data
websites = [
    'Amazon No Cache', 'Amazon Cache-Control', 'Amazon ETag',
    'CNN No Cache', 'CNN Cache-Control', 'CNN ETag',
    'Wikipedia No Cache', 'Wikipedia Cache-Control', 'Wikipedia ETag',
    'GitHub No Cache', 'GitHub Cache-Control', 'GitHub ETag',
    'New York Times No Cache', 'New York Times Cache-Control', 'New York Times ETag',
    'PayPal No Cache', 'PayPal Cache-Control', 'PayPal ETag'
]
plt_values = [
    1115, 556, 745, 1496, 776, 912,
    1102, 502, 655, 1303, 705, 855,
    1406, 742, 880, 1265, 599, 787
]

# Plotting
plt.figure(figsize=(14, 8))
plt.bar(websites, plt_values, color=['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue'])

plt.xlabel('Websites and Caching Policies')
plt.ylabel('Page Load Time (ms)')
plt.title('Page Load Times (PLT) vs. Caching Policies')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('plt_vs_caching.png')

# Show the plot
plt.show()
