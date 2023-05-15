XGB_model = XGBClassifier(objective = 'binary:logistic', eval_metric = 'error', learning_rate = 0.0584, max_depth = 3, n_estimators = 21, random_state = 0)

## Choose number of variables used (1, 2 or 6):
number = 1

if number == 6:
    XGB_model.fit(np.array(X), np.array(y))

elif number == 2:
    XGB_model.fit(np.array(X[['X1', 'X3']]), np.array(y))
    predictions = np.zeros((5,5))
    for i in range(1, 6):
        for j in range(1, 6):
            predictions[i-1][j-1] = XGB_model.predict([[j, i]])[0]
    sns.heatmap(predictions)
    plt.xlabel('X1 - 1')
    plt.ylabel('X3 - 1')
    plt.title('Model predictions from variables X1 and X3')
    plt.show()

elif number == 1:
    XGB_model.fit(np.array(X[['X1']]), np.array(y))
    print('The model prediction for X1 = 5 is ', XGB_model.predict([[5]])[0])
    print('The model prediction for X1 <= 4 is ', XGB_model.predict([[4]])[0])
    assert XGB_model.predict([[3]])[0] == XGB_model.predict([[2]])[0] == XGB_model.predict([[1]])[0] == 0

# The model score was identical if only X1 is chosen, or if more variable were chosen
# Therefore X1 is the only meaningful variable for this model
XGB_model.fit(np.array(X[['X1']]), np.array(y))

## set a new X_test, y_test dataset
X_test = X_test
y_test = y_test

print('\nThe XGB_model score on the test set using only X1 feature is: ', XGB_model.score(X_test[['X1']], y_test))

print('The model predicts y = 1 if and only if X1 = 5')

