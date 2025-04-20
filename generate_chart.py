import pandas as pd
import plotly.express as px
import os

# Load the CSV
df = pd.read_csv("daily_stats.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Ensure 'assets/' directory exists
os.makedirs("assets", exist_ok=True)

# ==== 📊 Interactive Bar Chart ====
fig_bar = px.bar(
    df,
    x="Date",
    y="Problems_Solved",
    text="Problems_Solved",
    title="📈 Daily Problem Solving Stats",
    labels={"Problems_Solved": "Problems Solved"},
    color="Problems_Solved",
    color_continuous_scale="Greens"
)
fig_bar.update_traces(textposition="outside")
fig_bar.update_layout(xaxis_tickangle=-45)

# Save as HTML (for full interactivity)
fig_bar.write_html("assets/daily_stats_chart.html")
print("✅ Interactive bar chart saved as daily_stats_chart.html")

# ==== 🗓️ Simulated Calendar Heatmap ====

# Create a "day of year" column to mimic calendar layout
df["DayOfYear"] = df["Date"].dt.dayofyear
df["Week"] = df["Date"].dt.isocalendar().week
df["Weekday"] = df["Date"].dt.weekday

fig_heatmap = px.density_heatmap(
    df,
    x="Week",
    y="Weekday",
    z="Problems_Solved",
    hover_name="Date",
    color_continuous_scale="YlGn",
    title="🗓️ Calendar Heatmap of Problems Solved"
)
fig_heatmap.update_layout(
    yaxis=dict(
        tickmode="array",
        tickvals=[0, 1, 2, 3, 4, 5, 6],
        ticktext=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    )
)

# Save as HTML
fig_heatmap.write_html("assets/calendar_heatmap.html")
print("✅ Interactive calendar heatmap saved as calendar_heatmap.html")
