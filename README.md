## Project Title

### Mintz_Gallery

##Project Description

### This project is to enable me practice and implement Django functions by creating a website application where a user can add images and others can view.

## Getting Started

- Create a repository on Github.
- Create a new directory in the terminal and initialize it
- Open your choice editor and start creating your code.
- When you are done with the project,deploy it to Heroku.
- Host your Heroku link as your live link on your created Github repository.

## Prerequisites

- Python3
- Django
- virtual environment

### User story
- User can log in the admin dashboard
- User can upload images
- Other users can view images based on location taken
- Search images by their category
- See image description when they hover on image


## Installing


## Deployment
- log in to heroku
```
heroku login
```
- create heroku app
```
heroku create app
```
- Upload requirements
```
pip freeze
```
- create a postgres addon to your heroku app
```
heroku addons:create heroku-postgresql:hobby-dev
```
- push to heroku

```
git push heroku master
```
- run migrations
```
heroku run python manage.py migrate
```
## Contact Information
- For any inqueries feel free to write to me through :
  - ![link] (betty.weru@student.moringaschool.com)

## Licence
- MIT License
- Copyright (c) 2022 Betty Weru
