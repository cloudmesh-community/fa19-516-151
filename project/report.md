# Cloudmesh Cloud AI Service

## Abstract

The project you will be developing a number of services exposing AI capabilities on the cloud. You will be developig a REST service that invokes an AI functionality in a general term. It is not sufficient to just port an application, but you must decide which functions are part of the application and port these as collaborating REST services.

Your service must be demonstrated on kubernetes and OpenStack showcasing applicability in container and virtual machines. A deployment, testing, and benchmark activity need t be demonstrated.

## Objective

This project will provide AI capabilities  on the cloud. The functionalities will be deployed at two different cloud platform in order to compare their performance. The cloud will expose REST API for users. Users are able to upload data to the cloud, calling functions and receive response messages. Now the cloud only provides a number of services, and the project will evolve at the later development. The scenario where user use AI service offered by the cloud should be defined in diverse situations.

## Technical Feasibility

### REST

* OpenAPI
  * The REST API will be defined by using OpenAPI specification
* Swagger editor
  * The swagger editor is used to write API documentation based on the OpenAPI standard
* Flask
  * The web application framework that handles incoming requests
* Connexion
  * Connexion is an application on the top of Flask that will map the REST API documentation to python functions on Flask

### Testing

* Pytest will be the testing framework of this project 

## Benchmark

## Team Member 

