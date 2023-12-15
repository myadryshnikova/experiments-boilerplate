import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

from experiment_config_provider import PARAMS

mlflow.autolog()

def experiment_run():
    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

    rf = RandomForestRegressor(
        **PARAMS.run.model.params,
        random_state=PARAMS.run.random_state,
        )

    rf.fit(X_train, y_train)
    