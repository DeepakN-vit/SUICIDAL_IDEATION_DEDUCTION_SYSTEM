import pandas as pd
from datetime import datetime, timedelta

def generate_weekly_report(data_file="user_data.csv", output_file="weekly_report.txt"):
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print("No data available to generate report.")
        return

    df['date'] = pd.to_datetime(df['date'])
    today = datetime.today()
    week_ago = today - timedelta(days=6)

    # Filter last 7 days
    weekly_data = df[(df['date'] >= week_ago)]

    if weekly_data.empty:
        print("No data in the last 7 days.")
        return

    # Aggregate
    daily_avg = weekly_data.groupby('date')['score'].mean().reset_index()

    report_lines = ["🧾 Weekly Mental Health Report", "=============================\n"]
    for _, row in daily_avg.iterrows():
        day = row['date'].strftime("%A, %Y-%m-%d")
        score = round(row['score'], 3)
        verdict = "At Risk" if score > 0.5 else "Fine"
        report_lines.append(f"{day}: Avg Score = {score} → {verdict}")

    weekly_avg = daily_avg['score'].mean()
    final_status = "At Risk" if weekly_avg > 0.5 else "Stable"
    report_lines.append("\n📊 Final 7-Day Average: {:.3f} → {}".format(weekly_avg, final_status))

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"✅ Weekly report saved to {output_file}")
