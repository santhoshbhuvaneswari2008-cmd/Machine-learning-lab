"""Training, evaluation and prediction using Logistic Regression."""
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def train_model(X, y, test_size=0.2, random_state=42):
    """Split the data, train Logistic Regression and evaluate it."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return model, X_train, X_test, y_test, y_pred, accuracy, cm


def predict_approval(model, income, credit_score, loan_amount):
    """Return the probability (0 - 1) that the loan is approved."""
    features = [[income, credit_score, loan_amount]]
    return float(model.predict_proba(features)[0][1])
