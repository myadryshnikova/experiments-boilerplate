# experiments-boilerplate

# Table of contents
- [experiments-boilerplate](#experiments-boilerplate)
  - [Description](#description)
  - [Performing experiments](#performing-experiments)
    - [Prerequisites](#prerequisites)
    - [Dev Containers](#dev-containers)
    - [Adding dependencies to the environment](#adding-dependencies-to-the-environment)
    - [Changing experiment parameters](#changing-experiment-parameters)
    - [Do run of experiment](#do-run-of-experiment)

## Description
Experimental repository boilerplate for machine learning experiments.

Contains the following services:
* Mlflow [https://mlflow.org/]

## Performing experiments
### Prerequisites
1. `Docker` [https://www.docker.com/]
2. `VSCode` [https://code.visualstudio.com/]
3. `MLflow-server` is running. Quick launch of the server is available in the repository: https://github.com/myadryshnikova/mlflow-docker-compose
4. An `.env` file is created in the project root and filled in. An example of an env file is `.env.example`. The variables it contains:
    * TRACKING_URI - mlflow-server tracking URI;
    * MLFLOW_TRACKING_USERNAME - username of developer, that registered in mlflow-server;
    * MLFLOW_TRACKING_PASSWORD - password of developer in mlflow-server.


### Dev Containers
Local development in this repository is assumed to be in Dev Container.

To run dev-container:
1. Clone this repository
    ```bash
    git clone https://github.com/myadryshnikova/experiments-boilerplate.git
    ```
2. Start the Docker service
3. Open the repository in VSCode
4. Run the Dev Containers: `Open Folder in Container...` command from the Command Palette (F1).

A notification will then appear that the Dev Container has started building. As soon as the build is finished, you can do experiments, the environment for the project is set up.

### Adding dependencies to the environment
This project uses `poetry` [https://python-poetry.org/] as a package manager.
The python packages used can be seen in the `pyproject.toml` file. 

To add a dependency:
    ```bash
        poetry add <package-name>
    ```

You can also directly update `pyproject.toml` by following the example of how other packages are written in it. After that, you need to synchronize it with the `poetry.lock` file using:
    ```bash
        poetry lock
    ```

If the dependency is not applied to the project after successful installation, you can rebuild the Dev Container.

### Changing experiment parameters
Parameters for the experiment are set in the `experiment_config.yaml` file in the root of the project.
Changed parameters will be applied to the code created for the experiment in the repository.

Since this template uses MLflow, there are concepts of `run` and `experiment`. 
Roughly speaking, experiment is a common theme for all runs. Run is a single iteration of an experiment with changed parameters. 

`experiment_config.yaml` is built on the same principle.

### Do run of experiment
To start and fix the run of experiment in MLFlow-server:
    ```bash
        make exp
    ```
Once the command is executed, the results of the experiment will be available on the MLFlow server.