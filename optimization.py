import optuna
from sklearn.metrics import recall_score, roc_auc_score
from catboost import Pool, CatBoostClassifier
from config import selected_feats
optuna.logging.set_verbosity(optuna.logging.WARNING)


## Подбор оптимального трешхолда по целевой метрике

def objective(trial, test_df, target, i):
    param_grid = {
        f'param_{i}': trial.suggest_uniform(f'param_{i}', test_df[f'sc_{target}'].min(), test_df[f'sc_{target}'].max()),
    }
    recall_0 = recall_score(test_df[target], test_df[f'sc_{target}']>param_grid[f'param_{i}'])
    recall_1 = recall_score((test_df[target]==0), test_df[f'sc_{target}']<param_grid[f'param_{i}'])
    return recall_1/2+recall_0/2


# Поиск наилучшего порога модели с помощью optuna
def get_best_params(test_df, target, num_trials, i, direction='maximize'):
    study_cb = optuna.create_study(direction=direction)
    study_cb.optimize(lambda trial: objective(
        trial, test_df, target, i), n_trials=num_trials, timeout=60*60)
    return study_cb.best_params, study_cb.best_value


# Подбор оптимальных парметров модели
def objective_model(trial, tr_df, val_df, target):
    param_grid = {
        'depth': trial.suggest_int('max_depth', 1, 3),
        'n_estimators':  trial.suggest_int("n_estimators", 10, 50),
        'l2_leaf_reg': trial.suggest_uniform("reg_lambda", 0, 50),
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.003, 0.04),
        'border_count': trial.suggest_int("border_count", 1, 255),
        'random_strength': trial.suggest_loguniform('random_strength', 1e-9, 10),
        'bagging_temperature': trial.suggest_uniform("bagging_temperature", 0, 1),
        'random_state': 123,
         'eval_metric': 'AUC', 
        'early_stopping_rounds': 50,
        "verbose": False
    }
    cb = CatBoostClassifier(**param_grid)
    train_pool = Pool(tr_df[selected_feats[target]], tr_df[target])
    val_pool = Pool(val_df[selected_feats[target]], val_df[target])
    cb.fit(train_pool, eval_set = val_pool)
    return roc_auc_score(val_df[target], cb.predict_proba(val_pool)[:,1])


# Поиск наилучших параметров модели с помощью optuna
def get_best_model_params(tr_df, val_df, target, num_trials, direction='maximize'):
    study_cb = optuna.create_study(direction=direction)
    study_cb.optimize(lambda trial: objective_model(
        trial, tr_df, val_df, target), n_trials=num_trials, timeout=60*60)
    return study_cb.best_params, study_cb.best_value