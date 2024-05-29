import csv
import sys
import numpy as np
from typing import Literal, Tuple, TypedDict, List


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    def func1(value: str) -> Literal[0, 1]:
        return 1 if value == "TRUE" else 0
    visitor = {"New_Visitor": 0,"Other": 0,"Returning_Visitor": 1}
    monthes_dict = {"Jan": 0,"Feb": 1,"Mar": 2,"Apr": 3,"May": 4,"June": 5,"Jul": 6,
        "Aug": 7,"Sep": 8,"Oct": 9,"Nov": 10,"Dec": 11,}

    list1: List[EvidenceRow] = []
    list2: List[Label] = []

    with open(filename) as file:
        for i in csv.DictReader(file):
            row: RawDataRow = i  # type: ignore
            list1.append(
                (int(row["Administrative"]),float(row["Administrative_Duration"]),float(row["PageValues"]),
                int(row["Informational"]),float(row["ProductRelated_Duration"]),float(row["BounceRates"]),
                int(row["Region"]),int(row["TrafficType"]),float(row["Informational_Duration"]),
                float(row["SpecialDay"]),monthes_dict[row["Month"]],int(row["OperatingSystems"]),
                int(row["ProductRelated"]),visitor[row["VisitorType"]],func1(row["Weekend"]),
                float(row["ExitRates"]),int(row["Browser"]),))

            list2.append(func1(row["Revenue"]))

    return (list1, list2)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(np.array(evidence), labels)
    return model



def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positive_count = 0
    negative_count = 0
    predicted_positive_count = 0
    predicted_negative_count = 0
    for label, prediction in zip(labels, predictions, strict=True):
        if label == 0:
            negative_count += 1
            if label == prediction:
                predicted_negative_count += 1

        else:
            positive_count += 1
            if label == prediction:
                predicted_positive_count += 1
    attr1 = predicted_positive_count / positive_count
    attr2 = predicted_negative_count / negative_count
    return (attr1, attr2)


if __name__ == "__main__":
    main()
