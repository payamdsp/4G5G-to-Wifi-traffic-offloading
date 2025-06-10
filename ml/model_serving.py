import mlflow.pyfunc

class OffloadModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        import joblib
        self.rf = joblib.load("random_forest.pkl")
        self.iso = joblib.load("isolation_forest.pkl")

    def predict(self, context, model_input):
        iso_scores = self.iso.decision_function(model_input)
        rf_pred = self.rf.predict(model_input)
        return {"rf": rf_pred.tolist(), "iso": iso_scores.tolist()}

if __name__ == "__main__":
    mlflow.pyfunc.save_model(
        path="offload_model",
        python_model=OffloadModel(),
        conda_env=None
    )