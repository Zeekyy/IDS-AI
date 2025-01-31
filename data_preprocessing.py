import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    if 'Index' in data.columns:
        data = data.drop('Index', axis=1)
    data = data.ffill()  
    data = pd.get_dummies(data, drop_first=True)
    
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test, data