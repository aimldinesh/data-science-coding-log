import pandas as pd
import matplotlib.pyplot as plt
import calplot
import os

# Load the CSV
df = pd.read_csv("daily_stats.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# ==== Part 1: Bar Chart ====
plt.figure(figsize=(12, 6))
plt.bar(df["Date"].dt.strftime("%Y-%m-%d"), df["Problems_Solved"], color="#4CAF50")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Date")
plt.ylabel("Problems Solved")
plt.title("📈 Daily Problem Solving Stats")
plt.tight_layout()

# Ensure 'assets/' directory exists
os.makedirs("assets", exist_ok=True)

# Save bar chart
plt.savefig("assets/daily_stats_chart.png")
plt.close()
print("✅ Bar chart saved as daily_stats_chart.png")

# ==== Part 2: Calendar Heatmap ====
df_heatmap = df.set_index("Date")["Problems_Solved"]
calplot.calplot(df_heatmap, cmap="YlGn", colorbar=True, suptitle="🗓️ Calendar Heatmap of Problems Solved")

# Save calendar heatmap
plt.savefig("assets/calendar_heatmap.png", bbox_inches="tight")
plt.close()
print("✅ Calendar heatmap saved as calendar_heatmap.png")
