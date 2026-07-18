"""
Social Media Engagement Data Generator
Generates synthetic social media posts across Instagram, TikTok and YouTube Shorts
for a direct to consumer apparel brand over a 6 month period.
"""
import pandas as pd
import numpy as np

np.random.seed(42)

platforms = ["Instagram", "TikTok", "YouTube Shorts"]
content_types = ["Reel", "Carousel", "Static Post", "Story"]
themes = ["Product Launch", "Behind the Scenes", "User Generated Content", "Styling Tips", "Promotional Offer", "Trend Based"]

start_date = pd.Timestamp("2025-01-01")
n_posts = 420

rows = []
for i in range(n_posts):
    platform = np.random.choice(platforms, p=[0.45, 0.35, 0.20])
    content_type = np.random.choice(content_types, p=[0.4, 0.25, 0.2, 0.15]) if platform == "Instagram" else "Short Video"
    theme = np.random.choice(themes)
    post_date = start_date + pd.Timedelta(days=int(np.random.uniform(0, 180)))

    base_reach = {"Instagram": 8000, "TikTok": 15000, "YouTube Shorts": 6000}[platform]
    theme_multiplier = {
        "Product Launch": 1.4, "Behind the Scenes": 0.9, "User Generated Content": 1.6,
        "Styling Tips": 1.1, "Promotional Offer": 0.8, "Trend Based": 1.7
    }[theme]

    reach = int(np.random.gamma(2, base_reach / 2) * theme_multiplier)
    engagement_rate = np.clip(np.random.normal(0.045, 0.018) * theme_multiplier / 1.2, 0.005, 0.18)
    likes = int(reach * engagement_rate * np.random.uniform(0.7, 0.85))
    comments = int(reach * engagement_rate * np.random.uniform(0.03, 0.08))
    shares = int(reach * engagement_rate * np.random.uniform(0.05, 0.15))
    saves = int(reach * engagement_rate * np.random.uniform(0.08, 0.2))

    follows_gained = int(reach * np.random.uniform(0.0005, 0.004) * theme_multiplier)

    rows.append({
        "post_id": f"P{i+1:04d}",
        "platform": platform,
        "post_date": post_date.strftime("%Y-%m-%d"),
        "content_type": content_type,
        "theme": theme,
        "reach": reach,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "saves": saves,
        "follows_gained": follows_gained,
        "engagement_rate": round(engagement_rate, 4)
    })

df = pd.DataFrame(rows)
df.to_csv("social_media_posts.csv", index=False)
print(f"Generated {len(df)} social media posts")
print(f"Date range: {df['post_date'].min()} to {df['post_date'].max()}")
print(f"Platform distribution: {df['platform'].value_counts().to_dict()}")
