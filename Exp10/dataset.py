"""Sample dataset for Loan Approval Prediction."""
import numpy as np

FEATURE_NAMES = ["Monthly income", "Credit score", "Loan amount"]

# Each row: (monthly_income, credit_score, loan_amount, approved)
# approved: 1 = loan approved, 0 = loan rejected
APPLICANT_DATA = [
    (93, 540, 9, 0), (127, 805, 37, 1), (112, 645, 23, 1),
    (43, 795, 9, 1), (53, 700, 36, 0), (124, 745, 26, 1),
    (16, 460, 24, 0), (118, 660, 16, 0), (115, 645, 18, 1),
    (73, 805, 11, 1), (53, 580, 3, 1), (50, 685, 35, 0),
    (47, 445, 20, 0), (71, 590, 23, 0), (78, 560, 14, 0),
    (84, 485, 31, 0), (139, 780, 3, 1), (114, 585, 16, 1),
    (93, 850, 3, 1), (139, 680, 7, 1), (42, 685, 39, 0),
    (35, 700, 27, 1), (92, 720, 18, 1), (20, 485, 22, 0),
    (19, 615, 35, 0), (79, 525, 15, 0), (73, 595, 24, 0),
    (130, 465, 28, 0), (94, 845, 16, 1), (79, 515, 22, 0),
    (77, 715, 31, 1), (46, 550, 37, 0), (16, 805, 8, 1),
    (39, 710, 37, 0), (102, 480, 2, 0), (40, 790, 31, 1),
    (61, 835, 33, 1), (15, 820, 7, 1), (119, 670, 18, 1),
    (34, 485, 33, 0),
]


def load_dataset():
    """Return the feature matrix X and target vector y (NumPy arrays)."""
    data = np.array(APPLICANT_DATA, dtype=float)
    X = data[:, :3]                # income, credit score, loan amount
    y = data[:, 3].astype(int)     # 1 = approved, 0 = rejected
    return X, y
