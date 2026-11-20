from xgboost import XGBClassifier


def train_gbm(X_train, y_train, X_val=None, y_val=None):
    pos = max(int(y_train.sum()), 1)
    model = XGBClassifier(
        n_estimators=400, learning_rate=0.05, max_depth=4, subsample=0.8,
        colsample_bytree=0.8, eval_metric="aucpr",
        scale_pos_weight=(len(y_train) - pos) / pos, random_state=42,
    )
    eval_set = [(X_val, y_val)] if X_val is not None else None
    model.fit(X_train, y_train, eval_set=eval_set, verbose=False)
    return model
