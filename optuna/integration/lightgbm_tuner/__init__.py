from typing import Any

from optuna._experimental import experimental
from optuna.integration.lightgbm_tuner.optimize import _check_lightgbm_availability
from optuna.integration.lightgbm_tuner.optimize import LightGBMTuner
from optuna.integration.lightgbm_tuner.optimize import LightGBMTunerCV  # NOQA
from optuna import type_checking

try:
    from optuna.integration.lightgbm_tuner.sklearn import LGBMClassifier  # NOQA
    from optuna.integration.lightgbm_tuner.sklearn import LGBMModel  # NOQA
    from optuna.integration.lightgbm_tuner.sklearn import LGBMRegressor  # NOQA

    _available = True
except ImportError as e:
    _import_error = e
    # LightGBMTuner is disabled because LightGBM is not available.
    _available = False


if type_checking.TYPE_CHECKING:
    from typing import Any  # NOQA


@experimental("0.18.0")
def train(*args: Any, **kwargs: Any) -> Any:
    """Wrapper of LightGBM Training API to tune hyperparameters.

    It tunes important hyperparameters (e.g., `min_child_samples` and `feature_fraction`) in a
    stepwise manner. Arguments and keyword arguments for `lightgbm.train()
    <https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html>`_ can be passed.
    """
    _check_lightgbm_availability()

    auto_booster = LightGBMTuner(*args, **kwargs)
    auto_booster.run()
    return auto_booster.get_best_booster()
