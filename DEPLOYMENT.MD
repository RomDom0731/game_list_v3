Domain Name: gamelistapp.com
Registrar: SquareSpace

Hosting Provider: Render

Tech Stack: Python (Flask) for the backend. HTML/CSS/JS for the frontend.

Database is PostgreSQL hosted on Render

The site is deployed via render using the build command pip install -r requirements.txt
Updates are CI/CD, and so any update the to GitHub repository automatically creates a new build of the backend

Secret variables, such as DATABASE_URL are stored in the environment on render