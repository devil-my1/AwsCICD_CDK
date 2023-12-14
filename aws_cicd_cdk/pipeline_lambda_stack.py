import os
import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, Code, Runtime


class MyLambdaStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, stageName: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Function(self, "PiplineLambdaFunc",
                 runtime=Runtime.PYTHON_3_12,
                 handler="lambda_handler.handler",
                 code=Code.from_asset(os.path.join(os.getcwd(), "lambda")),
                 environment={"stageName": stageName}
                 )
