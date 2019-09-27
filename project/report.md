# Cloudmesh Cloud AI Service: The Online Recommendation System

## Objective

> *The project you will be developing a number of services exposing AI capabilities on the cloud. You will be developig a REST service that invokes an AI functionality in a general term. It is not sufficient to just port an application, but you must decide which functions are part of the application and port these as collaborating REST services.* *Your service must be demonstrated on kubernetes and OpenStack showcasing applicability in container and virtual machines. A deployment, testing, and benchmark activity need t be demonstrated.*

The project will expose recommendation service API to user driven by a recommendation system involving the uses of sci-kit learn. 

The recommendation system can recommend the best item that the customers are most likely to buy.  The business customers shall provide pertinent information, and then the recommendation system will predict based on the previous records after data are uploaded to the recommendation system cloud. 

For example, a car rental company wants to find out which car the customer want to rent most. It should provide the related information such the profile of a car that rented by the customer and the customer's age which may also imply his interests. Then the recommendation engine will take those information to train a model using sci-kit learn as the tool and predict the preference of the customer.

The system shall secure the data of different users by the authentication. For example, the user has to log in their account and password before operating on the items.

## Technical Feasibility

### The Recommendation Engine

* Sci-kit learn

### Databae 

* Mongodb

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



