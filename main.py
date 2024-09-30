from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationtrainingPipeline
from textSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
logger.propagate = True

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} strated <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} strated <<<<<<<<<")
    data_validation = DataValidationtrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} strated <<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} strated <<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

