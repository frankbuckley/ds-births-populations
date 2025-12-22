import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy
from typing import Any


def plot_roc_curve(
    fpr,
    tpr,
    model_idx: int,
    save: bool = False,
    output_dir: str = ".",
    file_name: str = "roc_curve",
):
    plt.figure(figsize=(4, 4))
    plt.plot(fpr, tpr, label="ROC curve")
    plt.plot([0, 1.0], [0, 1], "--", color="#999999", label="Random classifier")
    plt.xlim([-0.03, 1.03])
    plt.ylim([0, 1.03])
    plt.xlabel("False Positive Rate (FPR)")
    plt.ylabel("True Positive Rate (TPR)")
    plt.title(f"Model {model_idx}: Receiver Operating Characteristic (ROC) Curve")
    plt.legend(loc="lower right")
    if save:
        plt.savefig(
            f"{output_dir}/{file_name}.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.savefig(
            f"{output_dir}/{file_name}.svg",
            bbox_inches="tight",
        )
    plt.show()


def plot_precision_recall_curve(
    fpr,
    tpr,
    model_idx: int,
    save: bool = False,
    output_dir: str = ".",
    file_name: str = "precision_recall_curve",
):
    plt.figure(figsize=(4, 4))
    plt.plot(fpr, tpr, label=f"Precision-Recall curve")
    plt.xlim([-0.03, 1.03])
    plt.ylim([0, 1.03])
    plt.xlabel("Recall [TP / (TP + FN)]")
    plt.ylabel("Precision [TP / (TP + FP)]")
    plt.title(f"Model {model_idx}: Precision-Recall Curve")
    plt.legend(loc="lower right")
    if save:
        plt.savefig(
            f"{output_dir}/{file_name}.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.savefig(
            f"{output_dir}/{file_name}.svg",
            bbox_inches="tight",
        )
    plt.show()


def plot_permutation_importances(
    result,
    X_eval,
    model_idx: int,
    save: bool = False,
    output_dir: str = ".",
    file_name: str = "permutation_importances",
):
    sorted_importances_idx = result.importances_mean.argsort()

    importances = pd.DataFrame(
        result.importances[sorted_importances_idx].T,
        columns=X_eval.columns[sorted_importances_idx],
    )
    x_size = max(4, min(6, 0.25 * importances.shape[1]))
    ax = importances.plot.box(vert=False, whis=10, figsize=(6, x_size))
    ax.set_title(f"Model {model_idx}: Permutation importances")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in accuracy score")
    ax.set_ylabel("Predictor variable")

    if save:
        plt.savefig(
            f"{output_dir}/{file_name}.png",
            dpi=300,
            bbox_inches="tight",
        )
        plt.savefig(
            f"{output_dir}/{file_name}.svg",
            bbox_inches="tight",
        )
    plt.show()


def plot_dendrogram(
    condensed,
    labels,
    model_idx: int,
    save: bool = False,
    output_dir: str = ".",
    file_name: str = "dendrogram",
):
    plt.figure(figsize=(5, 4))

    dist_linkage = hierarchy.linkage(condensed, method="average")
    dendro = hierarchy.dendrogram(
        dist_linkage,
        labels=labels,
        orientation="right",
        ax=plt.axes(),
    )

    plt.vlines(0.5, 0, 500, linestyle="--", color="#b2b4549f", linewidth=2)
    plt.xlabel("Linkage distance (increase in within-cluster variance)")
    plt.ylabel("Predictors")
    plt.title(f"Model {model_idx}: Hierarchical clustering of predictors")
    plt.show()
    
    return dist_linkage, dendro


def plot_correlation_heatmap(
    corr,
    dendro,
    label_threshold: float = 0.30,
    model_idx: int | Any = None,
    save: bool = False,
    output_dir: str = ".",
    file_name: str = "correlation_heatmap",
):
    C = corr[dendro["leaves"], :][:, dendro["leaves"]]
    labels = dendro["ivl"]
    dendro_idx = np.arange(len(labels))

    ysize = max(6, min(15, 0.4 * C.shape[0]))
    xsize = ysize

    with plt.rc_context(
        {"ytick.labelsize": 12, "xtick.labelsize": 12, "axes.titlesize": 12}
    ):
        fig, ax = plt.subplots(figsize=(xsize, ysize))
        im = ax.imshow(C, cmap="viridis")

        ax.set_title(f"Model {model_idx}: Correlation heatmap of predictors")
        ax.set_xticks(dendro_idx)
        ax.set_yticks(dendro_idx)
        ax.set_xticklabels(labels, rotation="vertical")
        ax.set_yticklabels(labels)

        n = C.shape[0]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue  # skip diagonal
                if abs(C[i, j]) < label_threshold:
                    continue

                ax.text(
                    j,
                    i,
                    f"{C[i, j]:.2f}",
                    ha="center",
                    va="center",
                    fontsize=8,
                    color="white" if abs(C[i, j]) < 0.6 else "black",
                )

        plt.colorbar(im, ax=ax, fraction=0.03, pad=0.025)

        if save:
            plt.savefig(f"{output_dir}/{file_name}.png", dpi=300, bbox_inches="tight")
            plt.savefig(f"{output_dir}/{file_name}.svg", bbox_inches="tight")

        plt.show()
