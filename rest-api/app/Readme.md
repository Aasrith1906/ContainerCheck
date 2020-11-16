# Container Management API 
***
## Purpose:
This is an API designed by Aasrith Chennapragada which uses Flask-restful and firebase to store and fetch container status, container details 

***

### Different URLS and their functions:
- **/** : this is the index page contains functions of this api and guide 
- **/Containers**: accpets only **GET** request and returns all containers stored in firebase in json format 
- **/<containername>**: accpets **GET** and **POST**, with **GET** returns details of container in json format, with **POST** updates container details if it already exists or it creates a new container

###### sample **POST** format for **/<containername>**: **{"location":"kitchen","item":"testitem2","refill":"false","last_date":"12-11-2020"}**

- **location** is the location of the continer
- **item** is the item inside the container
- **refill** field is the field that tells if a container needs refilling
- **last_date** is the last time the container was empty 

***

### Project Information

- manages containers and tells you which containers are empty and need to be refilled, generates shopping lists as well 

***