import aws_cdk as cdk
from constructs import Construct
from aws_cicd_cdk.pipeline_lambda_stack import MyLambdaStack


class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, ** kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = MyLambdaStack(self, "LambdaStack")
