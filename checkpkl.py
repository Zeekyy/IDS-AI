import joblib
import pandas as pd
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

model = joblib.load('trained_model.pkl')

print(model)

if hasattr(model, 'estimators_'):
    print(f"Number of trees in the forest: {len(model.estimators_)}")
    feature_importances = model.feature_importances_
    print(f"Feature importances: {feature_importances}")

    data = pd.read_csv('training_data.csv')
    
    data = data.drop('label', axis=1)  
    data = pd.get_dummies(data, drop_first=True)
    feature_names = data.columns
    
    for name, importance in zip(feature_names, feature_importances):
        print(f"{name}: {importance}")

    tree = model.estimators_[0]
    dot_data = export_graphviz(tree, out_file=None, 
                               feature_names=feature_names,  
                               class_names=['Normal', 'Malicious'],  
                               filled=True, rounded=True,  
                               special_characters=True)  
    graph = pydotplus.graph_from_dot_data(dot_data)  
    graph.write_png("tree.png")
    print("Tree visualization saved as tree.png")