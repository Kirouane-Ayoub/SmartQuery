import requests

inputs = {"input": {"input": "Hi"}}
response = requests.post("http://localhost:8000/invoke", json=inputs)

print(response.json())

# from langserve import RemoteRunnable

# remote_runnable = RemoteRunnable("http://localhost:8000/")
# question = ""
# await remote_runnable.ainvoke({"input": question})


# # stream
# question = ""
# async for chunk in remote_runnable.astream({"input":question }):
#     print('--')
#     print(chunk)
