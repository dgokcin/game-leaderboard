# gjg-backend-challenge
A REST API endpoint, that manages a game which uses a leaderboard with players submitting new scores from around the world.

### Requirements
- Docker
- docker-compose

__The application is compromised of 3 containers:__
```
flask: Contains the Flask application and uWSGI application server.
nginx: Contains the Nginx web server.
redis: Stores information about users & leaderboard.
```

### Building
`docker-compose up -d`

### Deployment
- The API is deployed to Docker Swarm running on my Digital Ocean Droplets. It can be reached from [this](http://178.62.26.184) link.

`docker stack deploy -c docker-compose-swarm.yml gjg`
