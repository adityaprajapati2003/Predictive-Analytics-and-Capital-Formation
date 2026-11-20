"""Isotonic calibration fitted on a later validation window."""
import joblib
from sklearn.isotonic import IsotonicRegression


class Calibrator:
    def __init__(self):
        self.iso = IsotonicRegression(out_of_bounds="clip")

    def fit(self, raw_probs, y_true):
        self.iso.fit(raw_probs, y_true)
        return self

    def predict(self, raw_probs):
        return self.iso.predict(raw_probs)

    def save(self, path):
        joblib.dump(self, path)
