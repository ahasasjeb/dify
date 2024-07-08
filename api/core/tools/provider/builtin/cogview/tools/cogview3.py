from zhipuai import ZhipuAI
from typing import Any, Union


from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool
api_key=self.runtime.credentials['api_key']
client = ZhipuAI(api_key="")
  
response = client.images.generations(
    model="cogview-3",
    prompt="一只可爱的小猫咪",
)

return(response.data[0].url)