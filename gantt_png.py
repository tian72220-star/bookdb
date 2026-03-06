import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

START_DATE = datetime(2024, 10, 12)   # 起始 2024-10-12
TASKS = [
    ("Literature Review",        14, "#AED6F1"),   # 20h
    ("Schema Design",             7, "#A9DFBF"),   # 20h
    ("Flask API + Tests",        14, "#F9E79F"),   # 40h
    ("Bootstrap UI",             14, "#FADBD8"),   # 30h
    ("Recommendation Engine",    14, "#D7BDE2"),   # 40h
    ("Cloud Deploy",              7, "#BB8FCE"),   # 25h
    ("System Testing",            7, "#F1948A"),   # 25h
    ("User Survey & Tuning",      7, "#85C1E9"),   # 20h
    ("Documentation Draft",      14, "#D5A6BD"),   # 30h
    ("Video Demo & Poster",       7, "#FFE599"),   # 15h
    ("Final Proof-read",          7, "#B7B7B7"),   # 10h
    ("Buffer & Submission",       7, "#8E8E8E"),   # 15h
]

fig, ax = plt.subplots(figsize=(16, 6))
start = START_DATE
y_pos = 0
milestones = []

for name, weeks, color in TASKS:
    end = start + timedelta(weeks=weeks)
    ax.barh(y_pos, weeks, left=mdates.date2num(start), color=color, edgecolor='black')
    ax.text(start + timedelta(weeks=weeks/2), y_pos, f"{name}", va='center', ha='center', fontsize=9, weight='bold')
    milestones.append(end)
    start = end
    y_pos += 1

for d in milestones:
    ax.axvline(mdates.date2num(d), color='red', linestyle='--', linewidth=1)
    ax.plot(d, -0.5, 'ro', markersize=6)

ax.set_yticks(range(len(TASKS)))
ax.set_yticklabels([t[0] for t in TASKS])
ax.set_xlabel("Date (starting 2024-10-12)", fontsize=12)
ax.set_title("16-Week Project Gantt (300 h) -- AI Library Management System", fontsize=14, weight='bold')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("gantt_300h.png", dpi=300)
print("✅ 甘特图已生成：gantt_300h.png")
