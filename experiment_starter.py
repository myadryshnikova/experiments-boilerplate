import mlflow
from experiment_config_provider import PARAMS
from experiment_run import experiment_run

mlflow.set_tracking_uri("http://host.docker.internal:8080")

experiment_description = (
    PARAMS.experiment.description
)

experiment_tags = {
    "project_name": PARAMS.project_name,
    "team": PARAMS.team,
    "mlflow.note.content": experiment_description,
}

try:
    experiment_id = mlflow.create_experiment(
        name=PARAMS.experiment.name, 
        tags=experiment_tags,
        )
except mlflow.exceptions.RestException:
    experiment_id = mlflow.get_experiment_by_name(PARAMS.experiment.name).experiment_id


mlflow.autolog()
with mlflow.start_run(
    experiment_id=experiment_id,
    description=PARAMS.run.description) as run:
    experiment_run()
