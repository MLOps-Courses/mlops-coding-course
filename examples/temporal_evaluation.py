# /// script
# requires-python = ">=3.14"
# dependencies = ["numpy>=2.1.3", "scikit-learn>=1.9.0"]
# ///
"""Tune on past observations and evaluate once on the untouched future."""

import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Synthetic time-ordered observations: no downloads or external services.
time = np.arange(120, dtype=float).reshape(-1, 1)
demand = 20 + 3 * time.ravel() + np.sin(time.ravel())
boundary = 96
inputs_train, inputs_test = time[:boundary], time[boundary:]
targets_train, targets_test = demand[:boundary], demand[boundary:]
assert inputs_train.max() < inputs_test.min()
cv = TimeSeriesSplit(n_splits=3)
for train, validation in cv.split(inputs_train):
    assert train.max() < validation.min()
    assert inputs_train[train].max() < inputs_train[validation].min()
    assert validation.max() < boundary

# Each fold fits its own scaler. The final refit sees only the training period.
search = GridSearchCV(
    make_pipeline(StandardScaler(), Ridge()),
    {"ridge__alpha": [0.01, 0.1, 1.0]},
    scoring="neg_mean_squared_error",
    cv=cv,
    n_jobs=1,
)
search.fit(inputs_train, targets_train)
np.testing.assert_allclose(search.best_estimator_["standardscaler"].mean_, inputs_train.mean(axis=0))

# Fix the selected model before looking at holdout results.
baseline = DummyRegressor(strategy="mean").fit(inputs_train, targets_train)
model_mse = mean_squared_error(targets_test, search.predict(inputs_test))
baseline_mse = mean_squared_error(targets_test, baseline.predict(inputs_test))
assert model_mse < baseline_mse
print(f"Chronology and train-only preprocessing passed; model MSE={model_mse:.3f}, baseline MSE={baseline_mse:.3f}.")
