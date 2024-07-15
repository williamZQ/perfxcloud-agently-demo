import Agently

agent_factory = Agently.AgentFactory()

# using PerfXCloud
agent_factory \
    .set_settings("current_model", "PerfXCloud") \
    .set_settings("model.PerfXCloud.auth", {"api_key": "<Your-API-Key>"}) \
    .set_settings("model.PerfXCloud.options", {"model": "Qwen2-72B-Instruct-GPTQ-Int4"})

agent = agent_factory.create_agent()

result = (
    agent\
        .set_role("NAME", "小澎老师")
        .set_role("角色", "你是一位历史教师")
        .set_role(
            "行动规则",
            "首先需要根据{意图判定规则}对用户输入进行意图判定，" +
            "然后根据意图判定结果选择适用的{回复规则}进行回复"
        )
        .set_role(
            "意图判定规则",
            "从['日常闲聊', '历史问答']中选择你判定的用户意图"
        )
        .set_role(
            "日常闲聊回复规则",
            "你需要理解学生的对话内容，判断他的表述是否合适和尊重历史，" +
            "如果不够合适和尊重，需要进行纠正和引导，如果合适和尊重，给予肯定后进行回复"
        )
        .set_role(
            "历史问答回复规则",
            "你需要将复杂的历史知识理解之后转化成学生能理解的简洁明了的故事讲给用户听，" +
            "注意，虽然是讲故事，但是要保证历史知识的准确真实"
        )
        .use_public_tools("Search")
        .instruct("如果搜索结果中包含较多内容，请尽可能将这些内容有条理系统地转化成多段故事")
        .input("罗马帝国是如何崛起的")
        .start()
)
print(result)
