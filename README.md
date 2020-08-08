![Build/Tests](https://github.com/dgokcin/gjg-backend-challenge/workflows/Build/Tests/badge.svg)
![Python](https://img.shields.io/badge/Python-v^3.7.1-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v^1.0.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Redis](https://img.shields.io/badge/Redis-v3.0.1-red.svg?longCache=true&style=flat-square&logo=redis&logoColor=white&colorA=4c566a&colorB=bf616a)


# gjg-backend-challenge
A REST API endpoint, that manages a game which uses a leaderboard with players submitting new scores from around the world.

### Requirements
- docker
- docker-compose

### Used Containers
```
flask: Contains the Flask application and uWSGI application server.
nginx: Contains the Nginx web server.
redis: Stores information about users & handles leaderboard interactions.
```
- The containers can be found under my [docker-hub account.](https://hub.docker.com/u/denizgokcin)

### Documentation
- The documentation can be found [here.](https://github.com/dgokcin/gjg-backend-challenge/blob/master/doc/gjg-backend-challenge.pdf)

### Building
`docker-compose up -d`

### Deployment
- The API is deployed to my Docker Swarm running on my Digital Ocean Droplets. The application is distributed on 3 nodes. The main page can be reached from [this](http://178.62.26.184) link.

`docker stack deploy -c docker-compose-swarm.yml gjg`

### Testing the endpoints
- The leaderboard is already filled with 50k random users.
- You can create more random data by using the following snippet in (https://www.json-generator.com).
```
[
  '{{repeat(50000)}}',
  {
    user_id: '{{guid()}}',
    rank: '{{integer(1, 10000000)}}',
    country: '{{random("tr", "fr", "us", "uk", "it")}}',
    display_name: '{{firstName()}}' ,
    points: '{{integer(1, 1000000000)}}'
    
  }
]
```
- You can post your [sample-data.json](https://github.com/dgokcin/gjg-backend-challenge/blob/master/sample-data.json) to http://178.62.26.184/user/create. 
- You can also add individual users using the same endpoint.
- You can get the leaderboard from http://178.62.26.184/leaderboard
- You can update a users score by posting to http://178.62.26.184/score/submit following the syntax in [this-document](https://github.com/dgokcin/gjg-backend-challenge/blob/master/doc/gjg-backend-coding-challenge.pdf)

### Notes:
- GitHub Actions are used for automatically running pytests and deploying to DockerHub.

### Future Work:
- Although there are multiple worker nodes, the response time could be improved if more powerful droplets are used.
- Getting the leaderboard for all the players takes short time but updating in with display name, country takes a long time since it depends on the number of players in the leaderboard. Could be improved but I do not think it is necessary since you only need to see detailed information about the first few players on a leaderboard.
