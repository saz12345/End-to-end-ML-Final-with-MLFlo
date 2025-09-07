from pathlib import Path
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from urllib.parse import urlparse
from src.mlProject.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        # Load test data and trained model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Set MLflow registry/tracking URI
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Make predictions
            predicted_qualities = model.predict(test_x)

            # Evaluate metrics
            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log parameters and metrics
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Infer model signature
            signature = infer_signature(test_x, predicted_qualities)

            # Log the model
            if tracking_url_type_store != "file":
                # Remote tracking: register model
                model_info = mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    registered_model_name="Elasticnetmodel",
                    signature=signature
                )
            else:
                # Local tracking: just log the model
                model_info = mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    signature=signature
                )

            # Print the URI where model is saved
            print("Model logged at:", model_info.model_uri)
