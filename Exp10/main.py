"""Loan Approval Prediction using Logistic Regression."""
from dataset import load_dataset, FEATURE_NAMES
from model import train_model, predict_approval
from plot import save_graph
from utils import get_number, get_category


def main():
    print("=" * 56)
    print("   LOAN APPROVAL PREDICTION USING MACHINE LEARNING")
    print("=" * 56)

    # Step 1: load the sample dataset
    X, y = load_dataset()
    print(f"\n[1] Dataset loaded: {X.shape[0]} applicants, "
          f"{X.shape[1]} input features")
    print("    Features :", ", ".join(FEATURE_NAMES))

    # Step 2: train and evaluate the model
    print("\n[2] Training Logistic Regression model ...")
    model, X_train, X_test, y_test, y_pred, acc, cm = train_model(X, y)
    print("    Model training completed.")
    print(f"    Training samples : {len(X_train)}")
    print(f"    Testing samples  : {len(X_test)}")

    # Step 3: show evaluation metrics
    print("\n[3] Model evaluation on the test set")
    print(f"    Accuracy : {acc * 100:.2f} %")
    print("    Confusion matrix (rows = actual, columns = predicted)")
    print("                 Rejected  Approved")
    print(f"      Rejected   {cm[0][0]:5d}     {cm[0][1]:5d}")
    print(f"      Approved   {cm[1][0]:5d}     {cm[1][1]:5d}")

    # Step 4: save the graph of confusion matrix and dataset
    save_graph(X, y, cm, acc, "loan_results.png")
    print("\n[4] Graph saved as loan_results.png")

    # Step 5: predict for new applicants entered in the terminal
    while True:
        print("\n[5] Enter the applicant details")
        income = get_number(
            "    Monthly income (Rs. thousands, 10 - 200): ", 10, 200)
        score = get_number(
            "    Credit score (300 - 900)                : ", 300, 900)
        loan = get_number(
            "    Loan amount (Rs. lakhs, 1 - 100)        : ", 1, 100)

        prob = predict_approval(model, income, score, loan)
        decision = "Approved" if prob >= 0.5 else "Rejected"
        print("\n    ---------- PREDICTION RESULT ----------")
        print(f"    Approval probability : {prob * 100:.2f} %")
        print(f"    Loan decision        : {decision}")
        print(f"    Risk category        : {get_category(prob)}")
        print("    ---------------------------------------")

        again = input("\nPredict for another applicant? (y/n): ")
        again = again.strip().lower()
        if again != "y":
            break

    print("\nThank you. Program finished.")


if __name__ == "__main__":
    main()
