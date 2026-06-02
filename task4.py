import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")

# Load dataset
df = pd.read_csv("US_Accidents_March23.csv")

# Use a sample for faster processing
df = df.sample(100000, random_state=42)

print("Dataset Shape:")
print(df.shape)

# --------------------------
# Data Cleaning
# --------------------------

# Remove rows with missing weather data
df = df.dropna(subset=['Weather_Condition'])

# Convert Start_Time safely
df['Start_Time'] = pd.to_datetime(
    df['Start_Time'],
    format='mixed',
    errors='coerce'
)

# Remove invalid dates
df = df.dropna(subset=['Start_Time'])

# Extract hour from timestamp
df['Hour'] = df['Start_Time'].dt.hour

# --------------------------
# 1. Accidents by Hour
# --------------------------

plt.figure(figsize=(10,5))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.savefig("1_accidents_by_hour.png")
plt.close()

# --------------------------
# 2. Weather Conditions
# --------------------------

top_weather = df['Weather_Condition'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_weather.plot(kind='bar')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Accident Count')
plt.tight_layout()
plt.savefig("2_weather_conditions.png")
plt.close()

# --------------------------
# 3. Severity Distribution
# --------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Severity', data=df)
plt.title('Accident Severity Distribution')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("3_severity_distribution.png")
plt.close()

# --------------------------
# 4. Day vs Night
# --------------------------

plt.figure(figsize=(6,4))
sns.countplot(x='Sunrise_Sunset', data=df)
plt.title('Day vs Night Accidents')
plt.xlabel('Time of Day')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("4_day_night.png")
plt.close()

print("\nAll charts generated successfully!")
print("Files created:")
print("1_accidents_by_hour.png")
print("2_weather_conditions.png")
print("3_severity_distribution.png")
print("4_day_night.png")