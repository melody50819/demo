# GainMiles-demo

## Environment SetUp

- miniconda3
- python (^3.10)
- pdm package

```bash
conda activate <env_name>

pip3 install pdm

pdm install
```

## Project Setup

Create `.env` file in the root directory and paste env variable:

```bash
MYSQL_DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3306/product"
```

### Vscode debug mode

`launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Flask",
      "type": "debugpy",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "main.py",
        "FLASK_DEBUG": "1"
      },
      "cwd": "${workspaceFolder}/src",
      "args": ["run", "--no-debugger", "--reload"],
      "jinja": true,
      "autoStartBrowser": false
    }
  ]
}
```

### Docker Compose

```bash
docker compose up -d  # run project

docker compose down # down project
```

## OpenAPI document

```
http://127.0.0.1:5000/docs
```
