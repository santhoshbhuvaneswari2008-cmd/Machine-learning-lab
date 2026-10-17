"""Graphs for the Loan Approval Prediction experiment."""
import matplotlib
matplotlib.use("Agg")   # save the graph as an image file
import matplotlib.pyplot as plt


def save_graph(X, y, cm, accuracy, filename):
    """Save (a) confusion matrix and (b) credit score vs income graph."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # (a) Confusion matrix of the test applicants
    ax1.imshow(cm, cmap="Blues")
    labels = ["Rejected", "Approved"]
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(labels)
    ax1.set_yticklabels(labels)
    for i in range(2):
        for j in range(2):
            color = "white" if cm[i, j] > cm.max() / 2 else "black"
            ax1.text(j, i, str(cm[i, j]), ha="center", va="center",
                     fontsize=18, color=color)
    ax1.set_xlabel("Predicted")
    ax1.set_ylabel("Actual")
    ax1.set_title(f"Confusion Matrix (Accuracy={accuracy * 100:.2f}%)")

    # (b) Credit score vs monthly income of all applicants in the dataset
    ax2.scatter(X[y == 1, 1], X[y == 1, 0], color="tab:green", s=50,
                label="Approved")
    ax2.scatter(X[y == 0, 1], X[y == 0, 0], color="tab:red", s=50,
                label="Rejected")
    ax2.set_xlabel("Credit score")
    ax2.set_ylabel("Monthly income (Rs. thousands)")
    ax2.set_title("Credit Score vs Income (dataset)")
    ax2.set_ylim(top=165)
    ax2.legend(loc="upper left")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
