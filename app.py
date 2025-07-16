import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predict import append_user_data
from speech_to_text import capture_speech
from weekly_report_generator import generate_weekly_report
from datetime import datetime

st.set_page_config(page_title="Suicidal Ideation Tracker", layout="wide")

st.title("🧠 Suicidal Ideation Monitoring Dashboard")
st.markdown("Enter your **daily thoughts** via text or speech to track emotional health.")

# --- Text Input ---
text = st.text_area("💬 Type your thoughts here:", height=150)
if st.button("Analyze Typed Text"):
    if text.strip() != "":
        label, score = append_user_data(text, log_speech=False)
        st.success(f"Prediction: **{label}**")
        st.info(f"Suicidal Probability: **{score:.3f}**")
    else:
        st.warning("Please enter some text.")

# --- Speech Input ---
st.markdown("---")
st.subheader("🎤 Speak Your Thoughts")

if st.button("Record Speech"):
    with st.spinner("Listening..."):
        spoken_text = capture_speech()
    if spoken_text:
        st.write(f"**Transcript:** {spoken_text}")
        label, score = append_user_data(spoken_text, log_speech=True)
        st.success(f"Prediction: **{label}**")
        st.info(f"Suicidal Probability: **{score:.3f}**")
    else:
        st.error("Could not understand your speech.")

# --- Load & Display Data ---
try:
    df = pd.read_csv("user_data.csv")
    df['date'] = pd.to_datetime(df['date'])

    st.subheader("📅 Daily Input Log")
    st.dataframe(df.sort_values("date", ascending=False).reset_index(drop=True))

    # --- Trend Graph ---
    st.subheader("📈 Stress Trend")
    daily_avg = df.groupby('date')['score'].mean().reset_index()

    fig, ax = plt.subplots()
    ax.plot(daily_avg['date'], daily_avg['score'], marker='o', linestyle='-', label='Daily Avg')
    ax.axhline(0.5, color='r', linestyle='--', label='Risk Threshold')
    ax.set_ylabel("Avg Suicide Probability")
    ax.set_xlabel("Date")
    ax.set_title("7-Day Stress Trend")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # --- Rolling 7-Day Report ---
    st.subheader("🧾 7-Day Rolling Stress Summary")
    report = []
    for i in range(len(daily_avg)):
        today = daily_avg.iloc[i]
        window = daily_avg.iloc[max(0, i-6):i+1]
        rolling_avg = window['score'].mean()
        verdict = "At Risk" if rolling_avg > 0.5 else "Fine"
        report.append({
            "date": today['date'].strftime("%Y-%m-%d"),
            "day_score": round(today['score'], 3),
            "7_day_avg": round(rolling_avg, 3),
            "verdict": verdict
        })
    report_df = pd.DataFrame(report)
    st.dataframe(report_df.sort_values("date", ascending=False).reset_index(drop=True))

except FileNotFoundError:
    st.warning("No input yet. Add some text or speech.")

# --- View Speech Logs ---
with st.expander("📄 View Raw Speech Log"):
    try:
        with open("user_speech_log.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.info("No speech logs yet.")

# --- Weekly Report ---
st.markdown("---")
st.subheader("🧾 Generate Weekly Summary Report")
if st.button("Generate Weekly Report"):
    generate_weekly_report()
    st.success("Weekly report generated as `weekly_report.txt`!")

with st.expander("📋 View Weekly Report"):
    try:
        with open("weekly_report.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.info("No weekly report generated yet.")
