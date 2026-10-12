# /// script
# requires-python = ">=3.14"
# dependencies = ["pydantic>=2.13.4"]
# ///
"""Reject invalid configuration before starting expensive training."""

from pydantic import BaseModel, Field, ValidationError


class TrainingConfig(BaseModel, strict=True, extra="forbid", frozen=True):
    test_size: float = Field(default=0.2, gt=0, lt=1)
    n_estimators: int = Field(default=100, gt=0)


config = TrainingConfig.model_validate({"test_size": 0.25, "n_estimators": 10})
assert config.n_estimators == 10

for invalid in (
    {"test_size": 1.0},
    {"n_estimators": "10"},
    {"n_estimators": 0},
    {"n_estimator": 10},
):
    try:
        TrainingConfig.model_validate(invalid)
    except ValidationError:
        continue
    raise AssertionError(f"Invalid configuration was accepted: {invalid}")

print("Valid configuration accepted; four invalid configurations rejected.")
