from zhipuai import ZhipuAI
from typing import Any, Union


from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

class CogViewTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:

    client = ZhipuAI(api_key=self.runtime.credentials['api_key'])
  
    response = client.images.generations(
        model="cogview-3",
        prompt=tool_parameters['prompt'],
    )

    return(response)