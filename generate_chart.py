import pandas as pd
import matplotlib.pyplot as plt
import calplot
import os

# Load the CSV
df = pd.read_csv("daily_stats.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Fill missing dates with 0
df = df.set_index("Date").asfreq("D", fill_value=0).reset_index()

# ==== Part 1: Bar Chart ====
plt.figure(figsize=(14, 6))
plt.bar(df["Date"], df["Problems_Solved"], color="#4CAF50")
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

# ==== Optional: Cumulative Progress Chart ====
df["Cumulative_Solved"] = df["Problems_Solved"].cumsum()

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Cumulative_Solved"], marker="o", linestyle="-", color="#2196F3")
plt.title("📈 Cumulative Problems Solved Over Time")
plt.xlabel("Date")
plt.ylabel("Total Problems Solved")
plt.grid(True)
plt.tight_layout()

# Save cumulative chart
plt.savefig("assets/cumulative_chart.png")
plt.close()
print("✅ Cumulative chart saved as cumulative_chart.png")
