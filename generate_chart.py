import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("daily_stats.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Plot
plt.figure(figsize=(12, 6))
plt.bar(df["Date"].dt.strftime("%Y-%m-%d"), df["Problems_Solved"], color="#4CAF50")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Date")
plt.ylabel("Problems Solved")
plt.title("📈 Daily Problem Solving Stats")
plt.tight_layout()

# Save chart
plt.savefig("daily_stats_chart.png")
print("✅ Chart saved as daily_stats_chart.png")
