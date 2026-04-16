import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n Data Loaded Successfully\n")
        return df
    except Exception as e:
        print(" Error loading file:", e)
        return None

# Explore Data
def explore_data(df):
    print("🔹 First 10 Rows:\n", df.head(10))
    print("\n🔹 Last 5 Rows:\n", df.tail(5))

    print("\n🔹 Shape:", df.shape)
    print("🔹 Columns:", list(df.columns))
    print("\n🔹 Data Types:\n", df.dtypes)

# Data Cleaning
def clean_data(df):
    # Convert Marks to numeric
    df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

    print("\n🔹 Missing Values Before:\n", df.isnull().sum())

    # Fill missing values with mean
    mean_val = df["Marks"].mean()
    df["Marks"] = df["Marks"].fillna(mean_val)

    print("\n🔹 Missing Values After:\n", df.isnull().sum())

    return df

# Basic Analysis
def basic_analysis(df):
    max_att = df["Attendance"].max()
    avg_hours = df["StudyHours"].mean()

    print("\n Basic Analysis")
    print("➡ Highest Attendance:", max_att)
    print("➡ Average Study Hours:", round(avg_hours, 2))

# Correlation Analysis
def correlation_analysis(df):
    numeric_df = df.select_dtypes(include=['number'])

    corr = numeric_df.corr()

    print("\n📈 Correlation Matrix:\n", corr)

    print("\n➡ Marks vs StudyHours:", corr.loc["Marks", "StudyHours"])
    print("➡ Marks vs Attendance:", corr.loc["Marks", "Attendance"])
    
# IQR Outlier Detection
def iqr_analysis(df):
    Q1 = df["Marks"].quantile(0.25)
    Q3 = df["Marks"].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    print("\n IQR Analysis")
    print(f"Q1={Q1}, Q3={Q3}, IQR={IQR}")
    print(f"Lower={lower}, Upper={upper}")

    outliers = df[(df["Marks"] < lower) | (df["Marks"] > upper)]

    print("\n⚠ Outliers Found:\n", outliers if not outliers.empty else "No Outliers")

    # Clean data
    clean_df = df[(df["Marks"] >= lower) & (df["Marks"] <= upper)]

    print("\n Clean Data Stats")
    print("Min Marks:", clean_df["Marks"].min())
    print("Max Marks:", clean_df["Marks"].max())

    return clean_df

# Visualization
def visualize(df):
    # Study Hours vs Marks
    plt.figure()
    plt.scatter(df["StudyHours"], df["Marks"])
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.title("Study Hours vs Marks")
    plt.show()

    # Attendance vs Marks
    plt.figure()
    plt.scatter(df["Attendance"], df["Marks"])
    plt.xlabel("Attendance")
    plt.ylabel("Marks")
    plt.title("Attendance vs Marks")
    plt.show()

# Save Clean Data
def save_data(df):
    df.to_csv("cleaned_student_data.csv", index=False)
    print("\n💾 Cleaned data saved successfully!")

# Main Function (Entry Point)
def main():
    file_path = "student_dataset_v2.csv"

    df = load_data(file_path)
    explore_data(df)

    df = clean_data(df)
    basic_analysis(df)

    correlation_analysis(df)

    df_clean = iqr_analysis(df)

    visualize(df_clean)

    save_data(df_clean)


# Run Program
if __name__ == "__main__":
    main()