# Converseo
<p align="center">
  <img src="readme/dashboard_readme.png" alt="Converseo"/>
</p>

> <h2>Converseo is an web app allowing the users to communicate with each other and look for new acquaintances.Backend was made in Django Rest Framework (asgi,channels included) as an API for Frontend which contains Vite/Vue app, managing websocket connections and API Calls (axios).
</h2> <br>

Live demo <br>
• [Converseo](http://3.127.135.129) <br>

Dummy user credentials <br>
<b>Username</b>: 'test1' <br>
<b>Password</b>: 'test1'

<b>Username</b>: 'test4' <br>
<b>Password</b>: 'test4'

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Improvements to be done](#improvements-to-be-done)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Converseo is an web app allowing the users to communicate with each other and look for new acquaintances. <br>
It allows you to search for people to talk with you.
Firstly you have to register a profile inside Converseo and set your avatar to better expose yourself to the potential Talkers.
Then you are ready to go, click at the icon which allows you to search for them.

Clicking at it, adds the profile to the queue of searching users and if there are someone who also is looking for new chatter, they get a match.
Each of them has to vote if they want to talk, they have two options - decline or accept.
If both of them accept, they are redirected to the conversation room, where they can talk.

In case someone gets bored or does not want to talk anymore, there is a close conversation button.

## Technologies Used
- <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20" align='center'/> Python 3.10.4 &nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="20" height="20" align='center'/> Django 4.1.5 &nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="DRF" alt="DRF" width="20" height="20" align='center'/> Django Rest Framework 3.14.0 (w/ channels, simplejwt)&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Daphne" alt="Daphne" width="20" height="20" align='center'/> Daphne Django ASGI&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original-wordmark.svg" title="HTML5" alt="HTML5" width="20" height="20" align='center'/> HTML5&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/sass/sass-original.svg" title="SASS" alt="SASS" width="20" height="20" align='center'/> SASS&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/tailwindcss/tailwindcss-original-wordmark.svg" title="Tailwind" alt="Tailwind" width="20" height="20" align='center'/> Tailwind&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="20" height="20" align='center'/> JavaScript ES6+ (websockets included)&nbsp;
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Vitejs-logo.svg/1039px-Vitejs-logo.svg.png" title="Vite" alt="Vite" width="20" height="20" align='center'/> Vite&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/vuejs/vuejs-original.svg" title="Vue" alt="Vue" width="20" height="20" align='center'/> Vue&nbsp;
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Axios_logo_%282020%29.svg/1200px-Axios_logo_%282020%29.svg.png" title="Axios" alt="Axios" width="20" height="20" align='center'/> Axios&nbsp;

### :hammer_and_wrench: Tools & Deployment:
- <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="Pycharm" width="20" height="20" align='center'/> PyCharm&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-plain-wordmark.svg" title="MySql" alt="MySql" width="20" height="20" align='center'/> MySQL&nbsp;
- <img src="https://symbols.getvecta.com/stencil_9/32_aws-elastic-beanstalk.3cbb564d52.svg" title="AWS" alt="AWS" width="20" height="20" align='center'/> AWS EC2/S3 (static files storage, VPS server)&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/nginx/nginx-original.svg" title="Nginx" alt="Nginx" width="20" height="20" align='center'/> Nginx&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="20" height="20" align='center'/> Docker&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="Redis" width="20" height="20" align='center'/> Redis&nbsp;



## Features
List the ready features here:
- Creating an account
- Logging in
- Adding/editing avatar image
- Searching for talkers
- Deciding if you want to talk to a random person
- Conversation room for matched talkers and sending messages
- Closing the conversation


## Screenshots
![name](readme/login_readme.png)
![name](readme/signup_readme.png)
![name](readme/dashboard_readme.png)
![name](readme/dashboard_readme1.png)
![name](readme/decider_readme.png)
![name](readme/conversation_readme.png)
![name](readme/dashboard_readme2.png)
![name](readme/dashboard_readme3.png)

<!-- If you have screenshots you'd like to share, include them here. -->
... and many more!

## Setup
1. Create New Folder <br>

2. Type <br>
> 'git clone https://github.com/drutkoowski/Converseo.git' into the console/git cli <br>
Then <br>
> 'cd Converseo' <br>

3. Create Virtual Environment by typing <br>
>'python3 -m venv venv' (in some cases you might use python instead of python3) <br>

4. Install all required dependencies located in requirements.txt using <br>
> 'pip install -r requirements.txt' <br>

5. Create '.env' file (variables required are located in env-sample)<br>

6. Run migrations by typing <br>
> 'python manage.py makemigrations' and then 'python manage.py migrate' <br>

7. Install packages
> 'cd frontend' and then 'npm install'

8. Run frontend server
> 'npm run dev'

9. Finally run backend server <br>
> 'python manage.py runserver' <br>

Frontend server: http://localhost:5173
Backend server: http://localhost:8000

Or using Docker:
1. Pull the project from Github
> 'git clone https://github.com/drutkoowski/Converseo.git'
2. Navigate to project folder
> 'cd Converseo'
3. Create Docker Image
> 'docker compose -f local.yml up -d'


## Project Status
Project is: :fire: COMPLETED :fire:

## Improvements to be done
- Adjusting layout
- Adding some better UX

## Contact
Created by Damian Rutkowski - feel free to contact me!
<div id="badges">
  <a href="https://www.facebook.com/drutkoowski/">
    <img src="https://img.shields.io/badge/Facebook-blue?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook Badge"/>
  </a>
  
   <a href="mailto:d.rutkowski2000@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail Badge"/>
  </a>
  
  <a href="https://www.linkedin.com/in/damian-rutkowski-810428237/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  
</div>

