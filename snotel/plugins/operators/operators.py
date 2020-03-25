

import logging
from datetime import datetime

from airflow.operators.sensors import BaseSensorOperator
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from IPython import embed;
log = logging.getLogger(__name__)



class StageRedshiftOperator(BaseOperator):
    def execute(self, context):
        pass
