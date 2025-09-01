from autogen_agentchat.agents import AssistantAgent 
from config.settings import get_model_client 
model_client = get_model_client()

def get_problem_solver_agent():
    problem_solver_agent = AssistantAgent(
        name="DSA_helper",
        description= "An agent that solves DSA problems",
        model_client = model_client,
        system_message="""
        you are a problem solver agent that is an expert in solving DSA problems. You will be working with code executor agent to execute code.
        you will be given a task to solve a DSA problem.
        You should:-
        Write code to solve the task. your code shall be only in Python.
        At the beginning of your response you have to specify your plan to solve the task.
        Then you should give the code in a code block(python).
        you should write code in a one code block at a time and then
        pass it to code executor agent to execute it.
        Make sure that we have 3 test cases for the code that you write.
        once the code is executed and if the same have been done successfully, you have the results.
        then you should explain the code execution result.

        In the end  once the code is executred successfully you have to say "STOP" to stop the conversation.

    """

    )
    return problem_solver_agent

