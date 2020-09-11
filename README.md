# QA Coding Challenge
Coding and test plan challenges for QA candidates

# Instructions
- Clone this repo to your local machine
- Use it to create a new repo on GitHub under your own account (please don't use GitHub fork to accomplish this)
- Complete the challenge described below
- Cleanup commit history to have 1 commit per challenge, in order, on the master branch.
- Send us an email with a link to your repo

___
## Challenge 1. Test a static HTML page
Using any python test framework, write a test that makes sure that https://www.google.com/ is up. The goal is not to test the content of the page but rather make sure that the page is available.

* Provide instructions how to run your test. Part of this assignment is to see how you would hand off *production* code to your fellow engineers.

> *******************************************
> Instructions how to retrieve automation code:  retrieve from git by entering below command line
>                                                git clone https://github.com/rbuscato/QA100.git
> *******************************************
> Instructions how to run test:
> Pre-req: Chrome browser is installed.     (note: install of the prerequisites is outside scope of this.)
> Pre-req: python and pytest are installed.  
>  at command line enter :  'python --version' and 'pytest -- version'
>  Should receive the version : pytest 6.0.1
>
>  Navigate to the folder where you downloaded the git project. Ensure you are at same dir level as /tests.
>  run pytest from command line with following flag to produce an HTML report:
	for example (you can use any name you like)
	$pytest --html=ThisHTMLReport.html
>  This html report can now be viewed in a browser.
> ******************************************
>
* Your solution will be reviewed by the engineers you would be working with if you joined Also Energy. We are interested in seeing your real-world design, coding, and testing skills.
* If you have any questions, please, email them to the person who sent you the challenge

> **********************************************************************************
