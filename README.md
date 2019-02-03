# Kirby 🐶

> Kirby allows you at one click create a foundation for your autotests project, that represented by simple API and LOAD tests. All you need is just a json model of your API.

## Getting Started

### Must be installed
- python 
- requests
- pytest
- allure
- locust

### Tests generation 

First you need is put your model into API/Models folder and run Gen.bat  
#### Json model format
```
{
	"base_url" : "https://reqres.in",
	"methods" : [
		{
			"type" : "get",
			"description" : "Description",
			"url" : "/api/users/2/",          
			"data" : null,                   # post request data
			"load" : 1                       # load frequency
		},
    ...
     ]
}
```
You'll get 
 - 'Executors' folder that contain your API-tree
 - 'Testcase' folder that contain one case for every API methods (you can edit them or add your own)
 - Load script for chosen methods
 
 ### Tests running
 
 For tests running you can use the 'Runners' folders
 
 API / Runners contain
 ```
 - RunTests.bat           # performs tests and collect reports to 'Reports'
 - GenerateAllure.bat     # using 'Reports' folder generate allure html reports
 - ShowHtmlReport.bat     # shows reports
 ```
 LOAD / Runners contain
 ```
 - Load.bat               # starting locust on http://localhost:8089
 ```
 
 ## Authors
* **Yegiazarian Victor**
