## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Tutorial](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```
To create CI/CD pipeline in heroku git
```
1. HEROKU_EMAIL = sudamghosh@gmail.com
2. HEROKU_API = 9ba03b76-d316-47b0-ba63-4bf5330456f7
3. HEROKU_APP_NAME = ml-project

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
```
Note: image name for docker must be lowercase

To list docker images
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 
