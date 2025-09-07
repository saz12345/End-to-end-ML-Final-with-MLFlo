from src.mlProject.utils._init_ import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainingTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        data_ingestion= DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        data_ingestion= DataValidationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME= "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        data_ingestion= DataTransformationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME= "Model Trainer Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        data_ingestion= ModelTrainingTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e


