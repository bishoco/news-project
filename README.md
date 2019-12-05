## Motley Fool Developer Interview Project - Corey Bishop

Overview
This is a my Motley Fool Developer interview project It is a simple news website that diplays articles from a json data file. When you click on an article headline, the full article is displayed along with stock quotes related to the articled.

Since I'm new to python and django, I kept things pretty simple. Let me know if you have any questions.

I created User Stories and Acceptance Criteria for this project. That can be seen here: https://github.com/bishoco/foolish-project/wiki/User-Stories

I also created a task board which helped keep track of what I was doing (and my sanity). It can be seen here: https://github.com/bishoco/foolish-project/projects/1

**Features**

Main page 
* Displays a main article
*The main article is the first article with the slug=10-promise. (This is driven via the db table ContentConfig where key = main-article-slug which can be changed in the admin)
* Three articles below.

Detailed Article page
*Displays full article text
*Displays stock quotes on the right side bar based on the instruments element in the article data
*User can enter comments at the bottom of the page

Search function
*Simple search function that displays search results

**Technical Specs**
* Django 2.2.7
* Python 3.8.0
* sqlite database
* bootstrap 4.4.1
* jquery 3.4.1
* popper.js 1.16.0

**Project Layout**
* articles - This is the app folder and where the core source code is
* data - This is where the API json files are stored
* foolnews - This is project folder
* wireframe - the original wireframes for the project
