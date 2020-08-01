![Python application](https://github.com/dgokcin/gjg-backend-challenge/workflows/Python%20application/badge.svg)
![Python](https://img.shields.io/badge/Python-v^3.7.1-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v^1.0.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Redis](https://img.shields.io/badge/Redis-v6.0.6-red.svg?longCache=true&style=flat-square&logo=redis&logoColor=white&colorA=4c566a&colorB=bf616a)


# gjg-backend-challenge
A REST API endpoint, that manages a game which uses a leaderboard with players submitting new scores from around the world.

### Requirements
- docker
- docker-compose

## Tech Stack
```
flask: Contains the Flask application and uWSGI application server.
nginx: Contains the Nginx web server.
redis: Stores information about users & leaderboard.
github actions: Automatically running ptyests and deploying to DockerHub.
```
- The containers can be found under my [docker-hub account](https://hub.docker.com/u/denizgokcin)

### Building
`docker-compose up -d`

### Deployment
- The API is deployed to my Docker Swarm running on my Digital Ocean Droplets. The application is distributed on 3 nodes. The main page can be reached from [this](http://178.62.26.184) link.

`docker stack deploy -c docker-compose-swarm.yml gjg`

### Testing the endpoints
- To test the endpoints, you need to add users to the leaderboard. You can achieve this by posting [sample-data.json](https://github.com/dgokcin/gjg-backend-challenge/blob/master/sample-data.json) to http://178.62.26.184/user/create. You can also add individual users using the same endpoint.
- You can get the leaderboard from http://178.62.26.184/leaderboard
- You can update a users score by posting to http://178.62.26.184/score/submit following the syntax in [this document](https://github.com/dgokcin/gjg-backend-challenge/blob/master/doc/gjg-backend-coding-challenge.pdf)


### Future Work:
- The response time might be improved if more powerful droplets are used. 
