# a lot of work in the last moment

I didn't think about how much work there was in this one homework task.....
(note to self... don't do this again)

## setup 

you need uv installed and vs code. (and python)

run these commands
``` 
uv venv
uv sync
uv ./createLocalDb.py

```

also add the currencyApi key to the .env value 

### vs code problems

when using python uv, sometimes vs code will not pick up the right python interpreter.
click down in the right corner -> select folder -> use path-finder/finder to pick it -> go to this project and inside the "./.venv/Scripts/python.exe" you find what you need.