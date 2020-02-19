# Deploy Machine Learning model

Steps involved:

1. Create a Model
2. Exporting a Model
3. Creating a Callable API
4. Calling the API with Postman
5. Calling the API with Python
6. Calling a model through Flask
7. Launching a full ML App to web


## Heroku
1. Create Free Heroku account
2. Install Heroku CLI (brew tap heroku/brew && brew install heroku)
3. Create a new APP over Heroku portal
4. Deploying using Heroku Git

Install the Heroku CLI

Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a
 new SSH public key.

```bash
$ heroku login
```

Create a new Git repository

Initialize a git repository in a new or existing directory

```bash
$ cd my-project/
$ git init
$ heroku git:remote -a machine-learning-eu
```

Deploy your application

Commit your code to the repository and deploy it to Heroku using Git.

```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

Existing Git repository

For existing repositories, simply add the heroku remote

```bash
$ heroku git:remote -a machine-learning-eu
```

https://machine-learning-eu.herokuapp.com/