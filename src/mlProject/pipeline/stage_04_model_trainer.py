from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.utils._init_ import logger
from pathlib import Path

STAGE_NAME ="Model Trainer Stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass
        
        
    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        obj= ModelTrainingTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e