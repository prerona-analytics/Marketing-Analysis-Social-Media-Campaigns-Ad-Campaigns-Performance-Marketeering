"""
Social Media Engagement Analysis
Analyses cross platform content performance to identify which content themes,
formats and platforms drive the strongest engagement and follower growth.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv("social_media_posts.csv")
df["post_date"] = pd.to_datetime(df["post_date"])
df["month"] = df["post_date"].dt.to_period("M").astype(str)

print("="*70)
print("SOCIAL MEDIA ENGAGEMENT ANALYSIS")
print("="*70)

# Platform level summary
platform_summary = df.groupby("platform").agg(
    total_posts=("post_id", "count"),
    avg_reach=("reach", "mean"),
    avg_engagement_rate=("engagement_rate", "mean"),
    total_follows=("follows_gained", "sum")
).round(3).sort_values("avg_engagement_rate", ascending=False)

print("\nPlatform Performance Summary")
print(platform_summary)

# Theme level performance
theme_summary = df.groupby("theme").agg(
    avg_reach=("reach", "mean"),
    avg_engagement_rate=("engagement_rate", "mean"),
    total_follows=("follows_gained", "sum"),
    post_count=("post_id", "count")
).round(3).sort_values("avg_engagement_rate", ascending=False)

print("\nContent Theme Performance (ranked by engagement rate)")
print(theme_summary)

# Monthly trend
monthly_trend = df.groupby("month").agg(
    avg_engagement_rate=("engagement_rate", "mean"),
    total_reach=("reach", "sum"),
    total_follows=("follows_gained", "sum")
).round(3)

print("\nMonthly Trend")
print(monthly_trend)

# Top 10 performing posts
top_posts = df.nlargest(10, "engagement_rate")[["post_id", "platform", "theme", "content_type", "engagement_rate", "reach"]]
print("\nTop 10 Posts by Engagement Rate")
print(top_posts.to_string(index=False))

# Visualisations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.barplot(data=theme_summary.reset_index(), x="avg_engagement_rate", y="theme", ax=axes[0, 0], palette="Blues_d")
axes[0, 0].set_title("Average Engagement Rate by Content Theme", fontsize=12, fontweight="bold")
axes[0, 0].set_xlabel("Engagement Rate")

sns.boxplot(data=df, x="platform", y="engagement_rate", ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Engagement Rate Distribution by Platform", fontsize=12, fontweight="bold")
axes[0, 1].set_ylabel("Engagement Rate")

monthly_plot = df.groupby(["month", "platform"])["engagement_rate"].mean().reset_index()
for plat in df["platform"].unique():
    data = monthly_plot[monthly_plot["platform"] == plat]
    axes[1, 0].plot(data["month"], data["engagement_rate"], marker="o", label=plat)
axes[1, 0].set_title("Engagement Rate Trend Over Time", fontsize=12, fontweight="bold")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Engagement Rate")
axes[1, 0].legend()
axes[1, 0].tick_params(axis="x", rotation=45)

follows_by_theme = df.groupby("theme")["follows_gained"].sum().sort_values(ascending=False)
sns.barplot(x=follows_by_theme.values, y=follows_by_theme.index, ax=axes[1, 1], palette="Greens_d")
axes[1, 1].set_title("Total Follower Growth by Content Theme", fontsize=12, fontweight="bold")
axes[1, 1].set_xlabel("Follows Gained")

plt.tight_layout()
plt.savefig("engagement_analysis_dashboard.png", dpi=150, bbox_inches="tight")
print("\nDashboard saved as engagement_analysis_dashboard.png")

# Key findings export
findings = f"""
KEY FINDINGS

1. Best performing platform by engagement rate: {platform_summary.index[0]} ({platform_summary.iloc[0]['avg_engagement_rate']:.1%})
2. Best performing content theme: {theme_summary.index[0]} ({theme_summary.iloc[0]['avg_engagement_rate']:.1%} engagement rate)
3. Theme driving most follower growth: {follows_by_theme.index[0]} ({follows_by_theme.iloc[0]} new follows)
4. Total posts analysed: {len(df)}
5. Average engagement rate across all content: {df['engagement_rate'].mean():.2%}
6. Total follower growth: {df['follows_gained'].sum()}
7. Platform with highest reach: {df.groupby('platform')['reach'].sum().idxmax()}

RECOMMENDATIONS

1. Prioritise {theme_summary.index[0]} and {theme_summary.index[1]} content themes
2. Focus on {platform_summary.index[0]} for engagement quality
3. Use {platform_summary.index[1]} for reach and audience expansion
4. Avoid over-reliance on promotional content; pair with paid amplification
5. Monitor monthly trends for early signs of audience fatigue
"""
print(findings)

with open("key_findings.txt", "w") as f:
    f.write(findings)
print("Findings saved to key_findings.txt")
