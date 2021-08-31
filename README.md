# CSL7510_Assessment_1_Part2

This repository contains code files for the 2nd part of assessment 1.

## Application : Random Employee Generator

The application retreives 10 random employees from a csv file.

The web-app is based on flask framework.

Steps to run the application:

  1. Make sure your syaytem has docker installed. If not, please downlaod from https://www.docker.com/products/docker-desktop
  2. Go inside *flask* folder and run --> 
  ```console 
     docker image build [your app name] .
   ```
   This will create a container with your app which contains all the dependencies.
  3. to run the application, execute --> 
  ```console 
  docker run -p 5000:5000 -d [your app name]
  ```
  4. To see the application, go to 
  ```console
  http://127.0.0.1:5000/
  ```
