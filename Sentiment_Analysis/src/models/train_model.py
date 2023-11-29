### Training with XGBoost. Hyperparameter tuning

def objective(trial): # The objective to maximize in the optuna study
    n_estimators = trial.suggest_int("n_estimators", 1, 50)
    learning_rate = trial.suggest_float("learning_rate", 0.01, 0.1, log=True)
    max_depth = trial.suggest_int("max_depth", 1, 5)
    _XGB_model = XGBClassifier(objective = 'binary:logistic', eval_metric = 'error', learning_rate = learning_rate,
                               max_depth = max_depth, n_estimators = n_estimators, random_state = 0)
    _XGB_model.fit(X_train, y_train)
    return _XGB_model.score(X_test, y_test)

sampler = TPESampler(seed=0)
study = optuna.create_study(direction="maximize", sampler=sampler)
study.optimize(objective, n_trials=50)

print("\nNumber of finished trials: ", len(study.trials))
print("Best trial:")
trial = study.best_trial
print("  Value: ", trial.value)
print("  Params: ")
for key, value in trial.params.items():
    print("    {}: {}".format(key, value))

learning_rate = trial.params['learning_rate']
max_depth = trial.params['max_depth']
n_estimators = trial.params['n_estimators']

## End of hyperparameter tuning

### Training

# XGBoost XGB_model with tuned parameters
XGB_model = XGBClassifier(objective = 'binary:logistic', eval_metric = 'error', learning_rate = learning_rate,
                          max_depth = max_depth, n_estimators = n_estimators, random_state = 0)

# The tuning should have returned: XGB_model = XGBClassifier(objective = 'binary:logistic', eval_metric = 'error',
# learning_rate = 0.0584, max_depth = 3, n_estimators = 21)

XGB_model.fit(X_train, y_train)
y_hat = XGB_model.predict(X_test)
print('\nThe XGB_model score on the test set is: ', XGB_model.score(X_test, y_test))
print(classification_report(y_test, y_hat))

print('\nImportance of each feature using this XGB_model:\n')
selector = RFECV(XGB_model, step=1, cv=5, min_features_to_select = 1)

selector = selector.fit(X_train, y_train)
for j in range(X.shape[1]):
    print(f'The variable X{j+1} was selected: ', selector.support_[j])
for j in range(X.shape[1]):
    print(f'Rank of variable X{j+1}: ', selector.ranking_[j])

X_train_reduced = X_train[['X1', 'X3']]
XGB_model.fit(X_train_reduced, y_train)
y_hat = XGB_model.predict(X_test[['X1', 'X3']])
print('\nThe XGB_model score on the test set using only X1 and X3 features is: ', XGB_model.score(X_test[['X1', 'X3']], y_test))
print(classification_report(y_test, y_hat))

X_train_reduced = X_train[['X1']]
XGB_model.fit(X_train_reduced, y_train)
y_hat = XGB_model.predict(X_test[['X1']])
print('The XGB_model score on the test set using only X1 feature is: ', XGB_model.score(X_test[['X1']], y_test))
print(classification_report(y_test, y_hat))
