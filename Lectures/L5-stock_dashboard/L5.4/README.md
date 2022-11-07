# Lecture 5.4 - Dashboard

Created dashboard with main functionality in place: 

- choose stock 
- filter time 
- filter OHLC options - open, high, low, close

Note that we use local csv-files for this example and not API calls. 

## Intermediate storage

In this update we use the client-side storage, i.e. the user's browser for storing JSON data after filtering. After filtering this intermediate storage is then used for multiple callbacks such as updating the graph and updating highest and lowest values. We use the **dcc.Store** component for doing this.

## Styling dash app

For styling this app we mostly used dash bootstrap components, but also some minor css-styling. TODO: fix minor responsiveness with mobile version.

## Deployment

Deploy on Heroku: 

1. Create account on [Heroku](https://www.heroku.com)
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) 
3. Add this line 
```py
server = app.server
```
under app = dash.Dash(\_\_name\_\_, ...).

4. If this project is not in a separate repo, with separate pipenv, make sure to create a new repo in Github and clone it. 

5. In this folder you should put all the files in this project and make sure to install all neccessary packages in this projects **pipenv**. 

6. Install gunicorn: 

```py
pipenv install gunicorn
```

7. Create a file named Procfile and write this line in it: 

```
web: gunicorn app_name_without.py:server
```


8. Run these commands to add, commit and push to Github:

```
git add .
git commit -m "<your message>"
git push
```

9. Add Heroku remote by going in to Heroku deploy and scroll down to "Existing Git repository".

```
heroku git:remote -a <heroku_project_name>
heroku ps:scale web=1
```

10. Push to Heroku:

```
git push heroku main
```

11. Enjoy your deployed dashboard app: 
[https://stocky-dashboard.herokuapp.com/](https://stocky-dashboard.herokuapp.com/)