# DevOps Task Tracker API

A beginner-friendly portfolio project demonstrating a Python REST API, automated tests, Docker containerization, and a GitHub Actions CI pipeline.

## Features
- `GET /health` — health check
- `GET /tasks` — list tasks
- `POST /tasks` — create a task
- `GET /tasks/{task_id}` — retrieve a task
- `PATCH /tasks/{task_id}` — update a task
- `DELETE /tasks/{task_id}` — delete a task
- Interactive API docs at `/docs`
- Pytest tests and a GitHub Actions test/build workflow

**Starter limitation:** tasks are stored in memory and reset when the app restarts. This keeps the first version simple; SQLite can be added as an improvement.

## Requirements
- Python 3.11 or 3.12
- Git
- Docker Desktop for local container testing
- GitHub account

## Run locally on Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -v
uvicorn app.main:app --reload
```
If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then `.\.venv\Scripts\python.exe -m pytest -v` and `python -m uvicorn app.main:app --reload`.

Open `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/health`.

## Run with Docker
Start Docker Desktop, then run:
```powershell
docker build -t devops-task-tracker:1.0 .
docker run --rm -p 8000:8000 devops-task-tracker:1.0
```
Open `http://localhost:8000/docs`; stop with Ctrl+C.

## CI workflow
`.github/workflows/ci.yml` runs on pushes and pull requests to `main`. It installs dependencies, runs tests, and then builds a Docker image. The starter workflow does not publish the image or deploy the app yet.

## Push to GitHub
Create a **new public repository** named `devops-task-tracker` on your GitHub account. Do not initialize it with a README if pushing this folder as-is. Open a terminal in this folder and run:
```powershell
git init
git add .
git commit -m "Build DevOps Task Tracker API with CI"
git branch -M main
git remote add origin https://github.com/gopika-9450/devops-task-tracker.git
git push -u origin main
```
If a remote already exists, check `git remote -v` before changing it. Never put a GitHub token or password in your code.

After pushing, open the repository's Actions tab and check that both jobs pass.

## Next improvements
1. Add SQLite persistence.
2. Add more API tests.
3. Publish the image to Docker Hub using GitHub Actions secrets.
4. Deploy to a hosting platform and document it.
5. Add screenshots of a successful workflow.

## Resume entry (only after you have tested it)
**DevOps Task Tracker — CI Pipeline with Docker and GitHub Actions**
- Developed a REST API using FastAPI and added automated tests with Pytest.
- Containerized the API with Docker and configured GitHub Actions to run tests and build an image on pushes and pull requests.
- Documented setup, container execution, and CI workflow.
Only list work you have actually implemented and verified.
