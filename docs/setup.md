### Miniconda and Python installation
1. Add both miniconda and python to path in env variables
2. C:\Users\niharika\miniconda3\condabin
3. C:\Users\niharika\AppData\Local\Programs\Python\Python313

```shell 
conda --version
python --version
```
### Setup and Run Environment - use command prompt only

1. Create conda python venv 
```shell 
conda env list
conda create -n llm-agents python
```

2. Activate conda venv
```shell 
conda activate llm-agents
```

3. Create python virtual environment
```shell 
python -m venv venv
```

4. Activate python virtual environment
```shell 
venv\Scripts\Activate
```

5. Install Required Packages in venv
```shell
pip install -r requirements.txt --no-user
```

### .env setup
1. rename .env.example to .env

### Run Google ADK

1. Run in terminal 
```shell
adk run
```

2. Run/ Test in Google adk UI
```shell
adk web
```

### Run MCP server
```shell
python ./mcp/main_server.py
```
