# OmarAbdulhaq-BikeSharingDemand

This project includes a model to predict the problem of Bike Sharing Demand, the project specifically solves this problem using Polynomial regression, the dataset that included different kinds of features was tuned and reduced in order to fit the model and to get more accurate results, APIs were later on added into the project in order to test the data using POSTMAN application.

The folder includes different files,
- **__init__** for initializing flask functionalities.
- **model** is the model result of the polynomial regression in the jupyter notebook.
- **BikeSharingModel** the jupyter notebook model, which includes EDA creation and the ways data was handled, in addition to the AI model that predicts fits the result of the model.
- **prediction** for a function that does the pickling and prediction once again for the API.
- **modelAPIroutes** for both of the APIs, although the single prediction includes the selected parameters during the EDA processing phase.
- **docker and requirements.txt** for the dockerization operation.
- **main** running the application through a server on port 5000, in addition to importing all the required files.
- **.gitignore** for uploading the entire files without the cache ones.

The features used in the model were reduced into: workingdays, weather, temp, humidity, windspeed, days, seconds
The reasons beyond reducing the features into this number was mentioned in the ipynb file (jupyter notebook)
