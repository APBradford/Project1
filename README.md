# DevOps Core Fundamental Project

This project is to create a Create, Read, Update and Delete (CRUD) application created in python. The application will be hosted on an Amazon EC2 instance and the database layer server will also be hosted in AWS using the RDS service. The front end of the application will be written using the Flask python framework.

My application is for a triathlon training tracking app. The user will be able to enter/veiw training data for running, swimming and cycling indiviudally. The application will then automatically create a fourth table, which takes data for each indivual activity and show the training totals for that week.

The MVP for the application will be having the pages, tables and CRUD features for Cycling and Training week.



# ERD Diagram

Below is the ERD digaram for the MySQL database. It shows the one to many relationship between the Cycling, Running, Swimming tables with the training week tables. The yellow highlighted tables are the MVP.

<img width="855" alt="ERD" src="https://user-images.githubusercontent.com/88770635/132582017-f2294821-4a48-4ccc-aa80-9eb1133d1742.PNG">

# Risk Assessment & Matrix

Below is the risk assessment/matrix for the project. Comments have been made as to a review of the risks at the end of the project.

<img width="492" alt="RiskAssessment3" src="https://user-images.githubusercontent.com/88770635/132868796-5de3fa49-e63f-45c2-817e-9089ac0b2632.PNG">

<img width="334" alt="Risk Matrix" src="https://user-images.githubusercontent.com/88770635/132209681-0727cfcb-d9a5-4b16-930a-a8a0bf69c1cc.PNG">

# Project Kanban Board

The project kanban board at the very beginning of the project (post sprint-planning) was as followed:

<img width="705" alt="Trello" src="https://user-images.githubusercontent.com/88770635/132214863-200ccabb-e6ec-4c9f-bcff-6bf67138354d.PNG">

As the project is only a few days long, the project sprints were 2 days long. User stories were written for each backlog item and MoSCoW priotisation was done. An example is as follows:

<img width="405" alt="User Story" src="https://user-images.githubusercontent.com/88770635/132214503-a44cd6e5-e7f0-42ff-9533-e279a7af7464.PNG">

At the end of the project, most of the user stories were able to be completed, with the exception of those which were prioritised as 'Could haves' which were extra features which were not part of the MVP.

<img width="700" alt="Trello2" src="https://user-images.githubusercontent.com/88770635/132869354-f3f31a55-de40-4861-9c59-5b9d3dedc8b0.PNG">

# Final MVP Stratha App

The final working MVP of the app is shown below.

<img width="400" alt="TW" src="https://user-images.githubusercontent.com/88770635/132870569-ae8df834-4a86-4bff-904d-e1c7caeed303.PNG">

The first page, the home/training week page, shows information taken from the training week database model. The data displayed is the sum of all the cycling activities entered into the second page form, sorted by training week and then sums up the distance of all the cycles done within that week. This table is automatically generated from the data entered into the cycling page.

<img width="712" alt="Cycling" src="https://user-images.githubusercontent.com/88770635/132871030-dcdfa431-116f-48d0-8eba-2a66e93fe90b.PNG">

The cycling page allows you to enter information about a cycle using a form built with wtforms. This then gets stored in the database under the cycling model. This data is then displayed in the table.

You can then edit an entry by clicking the 'Edit Entry' Button at the side of it. This will then take you to the edit page.

<img width="699" alt="edit" src="https://user-images.githubusercontent.com/88770635/132871326-650a93f8-9735-4c7a-847a-4d7b86c993fb.PNG">

Here you can then edit/delete the highlighted entry. The change in info will then be pushed and update the training week table as well.

# Testing 

Unit testing and intergration testing was completed using pytest and selenium. The coverage report was:

============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/ubuntu/Project1/Stratha-app
plugins: cov-2.12.1
collected 7 items

tests/test_app.py .......                                                [100%]

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
application/__init__.py       9      0   100%
application/forms.py         68     14    79%   36, 38-42, 61, 94, 96-100, 119
application/models.py        14      0   100%
application/routes.py        54      0   100%
-------------------------------------------------------
TOTAL                       145     14    90%


============================== 7 passed in 13.37s ==============================

Overall the tests covered 90% of the application. The missing lines were due to the custom wtform validators I had created where there were multiple raise validationErrors's for a test. Despite writing tests which returned these errors, pytest would still not claim they were covered, despite them being shown within the app itself.

# Jenkins

A jenkins CI server was also set up for this project. This would build the application and automatically install all required libraries and dependancies for the application. It was also configured with a webhook to the GitHub repo and so a new build would be automatically created upon a new push to the repo.

# Final GitHub network graph

The final github network graph for this project looked as follows. This shows that the project followed the Feature Branch Model.


