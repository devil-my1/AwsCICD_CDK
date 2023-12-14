import aws_cdk as cdk
from aws_cdk import (
    Stack
)
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
    ManualApprovalStep,
)
from constructs import Construct

from pipeline_app_stage import PipelineAppStage


class AwsCicdCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Set up pilpline
        pipeline = CodePipeline(self, "Pipeline",
                                pipeline_name="MyPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub(
                                                    "devil-my1/AwsCICD_CDK", "main"),
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )

        # Source stage
        testing_stage = pipeline.add_stage(PipelineAppStage(self,"test",env=cdk.Environment(account="241916871697",
                                    region="ap-northeast-1")))
        
        testing_stage.add_post(ManualApprovalStep("Manual approval before production"))
        
        production_stage = pipeline.add_stage(PipelineAppStage(self,"prod",env=cdk.Environment(account="241916871697",
                                    region="ap-northeast-1")))