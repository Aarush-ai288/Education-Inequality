
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Income-Based Education Inequality in Grade 8 Math")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("education_inequality_math_grade8.csv")

df = load_data()

# Filters
st.sidebar.header("Filter Data")
years = sorted(df['year'].dropna().unique())
states = sorted(df['stateabb'].dropna().unique())

selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
selected_gap = st.sidebar.selectbox(
    "Select Gap Metric",
    ['gap_ecd', 'gap_black_white', 'gap_female_male'],
    index=0
)

# Filtered Data
filtered_df = df[df['year'] == selected_year].sort_values(by=selected_gap, ascending=False)

# Show Table
st.subheader(f"{selected_gap.replace('_', ' ').title()} by State - {selected_year}")
st.dataframe(filtered_df[['stateabb', selected_gap]].reset_index(drop=True))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(filtered_df['stateabb'], filtered_df[selected_gap])
ax.set_title(f"{selected_gap.replace('_', ' ').title()} by State in {selected_year}")
ax.set_ylabel("Gap (Grade Level Units)")
st.pyplot(fig)

# Insights
st.markdown("### ℹ️ About This Project")
st.markdown("""
This dashboard visualizes the achievement gaps in 8th grade math scores based on socioeconomic and demographic variables.
Key metrics include:
- **gap_ecd**: Economic disadvantage (low vs. high income)
- **gap_black_white**: Racial gap between Black and White students
- **gap_female_male**: Gender-based gap

Data Source: Stanford Education Data Archive (SEDA)
""")
