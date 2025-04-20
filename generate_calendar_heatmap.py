import pandas as pd
import calplot
import matplotlib.pyplot as plt

# Load your CSV
df = pd.read_csv('daily_stats.csv', parse_dates=['Date'])
df = df.set_index('Date')['Problems_Solved']

# Plot the calendar heatmap
calplot.calplot(df, cmap='YlGn', colorbar=True, suptitle='🗓️ Coding Problem Calendar Heatmap')

# Save the heatmap
plt.savefig('calendar_heatmap.png', bbox_inches='tight')
