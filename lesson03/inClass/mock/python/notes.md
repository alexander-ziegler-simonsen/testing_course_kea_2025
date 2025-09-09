# fixed the vs code import problem

everytime I have a import inside a py file, vs code gives me a error.

I have to write these commands:

```bash

# start the project
uv init

# activate the venv 
uv venv

# sync it
uv sync
```

Also you need to write a new file 
.vscode/settings.json

where this needs to be inside 
```json
{
    "python.defaultInterpreterPath": ".venv/bin/python" 
}
```
