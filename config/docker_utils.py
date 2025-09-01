async def start_docker_container(docker):
    try:
        await docker.start()
    except Exception as e:
        print(f"Error starting Docker container: {e}")
        raise

async def stop_docker_container(docker):
    try:
        await docker.stop()
    except Exception as e:
        print(f"Error stopping Docker container: {e}")
        raise
