# Social Media Engagement Analysis: Cross Platform Content Performance

## Project Overview

This project analyses six months of social media posting activity for a direct to consumer apparel brand across Instagram, TikTok and YouTube Shorts. The objective was to identify which content themes, formats and platforms drive the strongest engagement and follower growth.

## Business Question

With limited content production capacity, which themes and platforms should the brand prioritise to maximise engagement and follower growth, rather than spreading effort evenly across everything.

## Dataset

The analysis covers 420 posts across three platforms with the following metrics tracked:

| Metric | Description |
|--------|-------------|
| Platform | Instagram, TikTok or YouTube Shorts |
| Content Type | Format of the post (Reel, Carousel, Static Post, Story, Short Video) |
| Theme | Content theme (Product Launch, Behind the Scenes, User Generated Content, Styling Tips, Promotional Offer, Trend Based) |
| Reach | Number of unique accounts reached |
| Likes | Number of likes received |
| Comments | Number of comments |
| Shares | Number of shares |
| Saves | Number of saves |
| Follows Gained | New followers attributed to the post |
| Engagement Rate | (Likes plus Comments plus Shares plus Saves) divided by Reach |

Note: This dataset is synthetically generated to reflect realistic engagement patterns observed in consumer social media accounts. It is intended as a portfolio demonstration of analysis methodology rather than real client data.

## Methodology

1. Aggregated performance by platform to compare reach and engagement rate at a channel level
2. Aggregated performance by content theme to identify which creative direction performs best regardless of platform
3. Tracked monthly trend to check for seasonality or fatigue in any theme
4. Identified the top performing individual posts to extract qualitative patterns
5. Built a four panel dashboard summarising all findings visually

## Key Findings

- **User Generated Content and Trend Based posts consistently outperformed scripted or promotional content on engagement rate**
- TikTok delivered the highest average reach per post but Instagram delivered a comparable engagement rate with a more loyal, slower growing audience
- Promotional Offer content, while necessary for conversion, had the lowest organic engagement rate of any theme, suggesting it should be paired with paid amplification rather than relied on for organic reach
- Engagement rate held steady across the six month period with a slight increase in May, suggesting no content fatigue within the period analysed

## Tools and Technologies

- Python 3.8 plus
- Pandas for data manipulation
- NumPy for numerical operations
- Matplotlib and Seaborn for data visualisation
- Jupyter Notebook compatible

## Installation and Setup

### Requirements

```bash
pip install pandas numpy matplotlib seaborn
```

### Python Version

Python 3.7 or higher

## How to Run

### Step 1: Generate Data

```bash
python generate_data.py
```

This creates `social_media_posts.csv` containing 420 synthetic post records.

### Step 2: Run Analysis

```bash
python analysis.py
```

This produces:
- `engagement_analysis_dashboard.png` - four panel visualisation dashboard
- `key_findings.txt` - summary of findings

### Expected Output

The analysis will print to console:
- Platform performance summary
- Content theme performance ranked by engagement
- Monthly trend data
- Top 10 performing posts

## Project Structure

```
.
|-- README.md                          (This file)
|-- generate_data.py                   (Data generation script)
|-- analysis.py                        (Analysis and visualisation)
|-- social_media_posts.csv             (Generated dataset)
|-- engagement_analysis_dashboard.png  (Output dashboard)
|-- key_findings.txt                   (Findings summary)
|-- requirements.txt                   (Python dependencies)
|-- .gitignore                         (Git ignore rules)
```

## Files Explanation

### generate_data.py
Generates 420 synthetic social media posts with realistic engagement distributions based on platform, content type and theme. Saves to CSV format.

**Key parameters:**
- Number of posts: 420
- Date range: 6 months (Jan to Jun 2025)
- Platforms: Instagram, TikTok, YouTube Shorts
- Content types and themes with realistic engagement multipliers

### analysis.py
Runs complete analysis pipeline including:
- Platform level aggregation
- Theme level performance analysis
- Monthly trend calculation
- Top posts identification
- Four panel dashboard generation

### social_media_posts.csv
Generated dataset with 420 rows and 12 columns. Column format:

```
post_id, platform, post_date, content_type, theme, reach, likes, comments, shares, saves, follows_gained, engagement_rate
```

## Analysis Sections

### 1. Platform Performance
Compares reach, engagement rate and follower growth across Instagram, TikTok and YouTube Shorts.

### 2. Content Theme Performance
Evaluates six content themes (Product Launch, Behind the Scenes, User Generated Content, Styling Tips, Promotional Offer, Trend Based) on engagement and follower growth.

### 3. Monthly Trends
Tracks engagement rate and reach across the six month period to identify seasonality or audience fatigue.

### 4. Top Performing Posts
Identifies the 10 highest engagement rate posts to extract patterns and qualitative insights.

## Key Insights from Dashboard

The four panel dashboard shows:
1. **Top left:** Average engagement rate by content theme (bar chart)
2. **Top right:** Engagement rate distribution by platform (box plot)
3. **Bottom left:** Engagement rate trend over time by platform (line chart)
4. **Bottom right:** Total follower growth by content theme (bar chart)

## Recommendations

Based on the analysis:

1. Prioritise User Generated Content and Trend Based content, which show 2x to 3x higher engagement than promotional content
2. Consider platform specific strategies: TikTok for reach, Instagram for engagement quality
3. Use promotional content strategically rather than organically; pair with paid amplification
4. Monitor monthly trends to catch audience fatigue early
5. Increase posting frequency for top performing themes and times

## Reproducibility

To reproduce results with new synthetic data:

```bash
python generate_data.py  # Regenerates social_media_posts.csv
python analysis.py       # Recomputes analysis and dashboard
```

Random seed is fixed in both scripts for reproducibility. Change seed values to generate different synthetic data distributions.

## Limitations

- Dataset is synthetically generated for portfolio demonstration
- Engagement patterns are based on observed industry benchmarks but not real data
- Monthly trend period (6 months) may not capture longer term seasonality
- Platform specific features (Stories, Reels, Shorts) are abstracted into content types
- No demographic or audience segmentation included

## Future Enhancement Ideas

- Add audience demographic segmentation analysis
- Include hashtag performance analysis
- Add competitor benchmark comparison
- Build predictive model for engagement based on post characteristics
- Incorporate follower growth velocity and retention metrics
- Add posting schedule optimisation analysis

## Contact and Feedback

For questions or feedback on this analysis, please reach out.

## License

This project is provided as a portfolio demonstration. All data is synthetic.

---

**Portfolio Note:** This analysis is part of a marketing analytics portfolio demonstrating capability in data extraction, analysis, visualisation and business communication. All data is synthetically generated.
