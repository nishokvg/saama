# Saama Tasks

## Getting details from AWS Env

  1) Set up the AWS Access keys profile
  2) run 'python getdetails.py'


## Docker file to install any flask-based application

   1) Test the flask app with out docker `python demo.py`
   2) Creating a docker image of the project and How to run it
        Build the Docker image

        ``` sudo docker build --tag flask-docker-demo-app . ```

        Run the docker image we just created.

        ``` sudo docker run --name flask-docker-demo-app -p 5001:5001 flask-docker-demo-app ```
