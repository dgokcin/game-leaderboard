gjg-backend-challenge
=====================

A REST API endpoint, that manages a game which uses a leaderboard with
players submitting new scores from around the world.

Requirements
~~~~~~~~~~~~

-  docker
-  docker-compose

Used Containers
~~~~~~~~~~~~~~~

::

    flask: Contains the Flask application and uWSGI application server.
    nginx: Contains the Nginx web server.
    redis: Stores information about users & handles leaderboard interactions.

-  The containers can be found under my `docker-hub
   account <https://hub.docker.com/u/denizgokcin>`__

Building
~~~~~~~~

``docker-compose up -d``

Deployment
~~~~~~~~~~

-  The API is deployed to my Docker Swarm running on my Digital Ocean
   Droplets. The application is distributed on 3 nodes. The main page
   can be reached from `this <http://178.62.26.184>`__ link.

``docker stack deploy -c docker-compose-swarm.yml gjg``

Testing the endpoints
~~~~~~~~~~~~~~~~~~~~~

-  To test the endpoints, you need to add users to the leaderboard. You
   can achieve this by posting
   `sample-data.json <https://github.com/dgokcin/gjg-backend-challenge/blob/master/sample-data.json>`__
   to http://178.62.26.184/user/create. You can also add individual
   users using the same endpoint.
-  You can get the leaderboard from http://178.62.26.184/leaderboard
-  You can update a users score by posting to
   http://178.62.26.184/score/submit following the syntax in `this
   document <https://github.com/dgokcin/gjg-backend-challenge/blob/master/doc/gjg-backend-coding-challenge.pdf>`__

Notes:
~~~~~~

-  GitHub Actions are used for automatically running pytests and
   deploying to DockerHub. ### Future Work:
-  Although there are multiple worker nodes, the response time could be
   improved if more powerful droplets are used.

