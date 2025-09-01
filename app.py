import streamlit as st 
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio
st.title("DSA_helper- DSA problem solver")
st.write("Welcome to DSA_helper! An AI-powered platform to solve Data Structures and Algorithms problems using advanced language models.")

task = st.text_input("Enter your DSA problem statement here:")

async def run(team, docker, task):
    try:
        await start_docker_container(docker)

        async for message in team.run_stream(task= task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"stop reason: {message.stop_reason}")
                yield msg
                
        
        print("Task completed.")

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        await stop_docker_container(docker)

if st.button("Solve Problem"):
    st.write(f"Solving the problem...")
    team, docker = get_dsa_team_and_docker()
    async def collect_messages():
        async for msg in run(team, docker, task):
            if isinstance(msg, str):
                if msg.startswith('user'):
                    with st.chat_message("user", avatar="🧑‍💻"):
                        st.markdown(msg)
                elif msg.startswith('DSA_helper'):
                    with st.chat_message("DSA_helper", avatar="🤖"):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                st.markdown(f"Task completed with stop reason: {msg.stop_reason}")


    asyncio.run(collect_messages())