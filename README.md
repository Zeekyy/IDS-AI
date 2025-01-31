# Network Traffic Analysis with Machine Learning

This project is a network traffic analysis application that uses machine learning to detect malicious connections. The application allows users to train a machine learning model with a CSV file of network traffic data and then analyze new CSV files to identify potentially malicious connections.

## Overview

The project consists of the following main components:
- **Data Preprocessing**: Functions to load and preprocess network traffic data.
- **Model Training**: Functions to train a RandomForestClassifier model on the preprocessed data.
- **Model Evaluation**: Functions to evaluate the trained model and generate classification reports.
- **Web Interface**: A Flask-based web interface that allows users to upload CSV files for training and analysis.

## Features

- **Train Model**: Upload a CSV file to train the machine learning model.
- **Analyze File**: Upload a CSV file to analyze network traffic and identify malicious connections based on the trained model.
- **Visualization**: Generate and visualize decision trees from the trained model.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- scikit-learn
- pandas
- joblib
- graphviz
- pydotplus

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ids-machine-learning.git
    cd IDS Machine Learning
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install GraphViz:
    - **macOS**: `brew install graphviz`
    - **Ubuntu/Debian**: `sudo apt-get install graphviz`
    - **Windows**: Download and install from [GraphViz Download](https://graphviz.gitlab.io/download/)

### Usage

1. **Generate Training Data**:
    ```sh
    python csvgen.py
    ```

2. **Run the Flask Application**:
    ```sh
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

4. **Train the Model**:
    - Go to the "Train Model" page.
    - Upload a CSV file with network traffic data.
    - The model will be trained and saved as [trained_model.pkl](http://_vscodecontentref_/0).

5. **Analyze a File**:
    - Go to the "Analyze File" page.
    - Upload a CSV file to analyze.
    - The application will identify and display potentially malicious connections.

6. **Visualize Decision Tree**:
    - Run the following script to visualize a decision tree from the trained model:
        ```sh
        python checkpkl.py
        ```
    - The visualization will be saved as [tree.png](http://_vscodecontentref_/1).

## About the Project

This project was created as a learning exercise to explore machine learning and network traffic analysis. Approximately 50% of the code was generated with the assistance of an AI (GitHub Copilot) to help with coding tasks and answer questions. As a beginner in machine learning, this project provided valuable insights and hands-on experience.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [pandas](https://pandas.pydata.org/)
- [GraphViz](https://graphviz.gitlab.io/)
- [GitHub Copilot](https://github.com/features/copilot)
