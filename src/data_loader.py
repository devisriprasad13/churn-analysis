import pandas as pd

def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Load Telco Customer Churn dataset.
    Source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
    Returns: raw DataFrame with 7043 rows x 21 columns
    """
    df = pd.read_csv(filepath)
    print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Churn rate: {df['Churn'].value_counts(normalize=True)['Yes']:.1%}")
    return df

if __name__ == "__main__":
    df = load_raw_data("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    print(df.dtypes)
    print(df.head())

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Documented cleaning steps with business justification.
    """
    df = df.copy()

    # Fix 1: TotalCharges is stored as string — 11 rows have whitespace
    # Business reason: these are likely new customers (tenure=0), not errors
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    new_customers = df[df['TotalCharges'].isna()]
    print(f"New customers with no charges: {len(new_customers)}")

    # Decision: fill with 0 (they haven't been billed yet, not missing data)
    df['TotalCharges'] = df['TotalCharges'].fillna(0)

    # Fix 2: Binary encode Churn column for modeling
    df['Churn_Binary'] = (df['Churn'] == 'Yes').astype(int)

    # Fix 3: Drop customerID — it's an identifier, not a feature
    df = df.drop('customerID', axis=1)

    # Fix 4: SeniorCitizen is 0/1 integer but should be consistent with others
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

    # Audit log — always print what changed
    print(f"After cleaning: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Missing values remaining: {df.isnull().sum().sum()}")

    return df