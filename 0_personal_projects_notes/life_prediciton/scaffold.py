# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Data preprocessing
def preprocess_data(data):
    # Handle missing values
    data.dropna(inplace=True)

    # Feature selection and engineering
    # Add any feature selection or engineering steps here

    return data

# Model training
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Model evaluation
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mae, mse, r2

# Main function
def main():
    # Load data
    file_path = "life_expectancy_data.csv"  # Update with your file path
    data = load_data(file_path)

    # Preprocess data
    data = preprocess_data(data)

    # Split data into features and target variable
    X = data.drop("Life Expectancy", axis=1)  # Features
    y = data["Life Expectancy"]  # Target variable

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    mae, mse, r2 = evaluate_model(model, X_test, y_test)
    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)
    print("R-squared Score:", r2)

if __name__ == "__main__":
    main()
