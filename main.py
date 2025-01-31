from data_preprocessing import load_data, preprocess_data
from model_training import train_model as train_model_func, evaluate_model
from sklearn.model_selection import cross_val_score
import joblib
import numpy as np

def analyze_file(file_path):
    data = load_data(file_path)
    X_train, X_test, y_train, y_test, original_data = preprocess_data(data)
    
    model = joblib.load('trained_model.pkl')
    
    y_pred = model.predict(X_test)
    
    original_test_data = original_data.iloc[y_test.index]
    malicious_connections = original_test_data[y_pred == 1]
    
    columns_to_display = ['protocol_type', 'num_failed_logins', 'count', 'service']
    available_columns = malicious_connections.columns
    columns_to_display = [col for col in columns_to_display if col in available_columns]
    
    results = malicious_connections[columns_to_display].reset_index()
    results = results.rename(columns={'index': 'line'})
    
    return results.to_dict(orient='records')

def train_model(file_path):
    data = load_data(file_path)
    X_train, X_test, y_train, y_test, original_data = preprocess_data(data)
    
    unique, counts = np.unique(y_train, return_counts=True)
    class_distribution = dict(zip(unique, counts))
    print("Class distribution in training data:", class_distribution)
    
    model = train_model_func(X_train, y_train)
    scores = cross_val_score(model, X_train, y_train, cv=5)
    # print("Cross-validation scores:", scores)
    # print("Mean cross-validation score:", scores.mean())
    
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)