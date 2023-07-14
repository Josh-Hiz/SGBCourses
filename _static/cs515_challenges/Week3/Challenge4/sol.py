def predict(cases, predicted_growths):
    for growth in predicted_growths:
        for i in range(len(cases)):
            cases[i] = cases[i] + growth
        print(cases)