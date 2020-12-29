# Technation API

## Heroku Deployment
1. create heroku remote: `heroku create <heroku api app name>`
2. set heroku remote: `heroku git:remote -a <heroku api app name>`
3. push `/api` subdirectory to heroku: `git subtree push --prefix api heroku main`
4. make sure one instance is running: `heroku ps:scale web=1`
5. 