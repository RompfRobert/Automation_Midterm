# Get Top Artists - Documentation
The aim of this app is to get the top billboard artists this week and the previous 3 weeks, or in short, the most popular artists in the last 4 weeks, this week included. Although, first and foremost, for this application to work as intended, some setup is required by the user.
***
## Google Cloud Setup
For the application to work correctly, first and foremost you will need to set up a [Google Cloud account](https://console.cloud.google.com) and follow the steps laid out.
### Create a project
The next step is to create a [Google Cloud project](https://developers.google.com/workspace/guides/create-project), as that is what allows users to create, manage and enable the use of Google Cloud Services using Google APIs.
>To create a Google Cloud project:
> 1. Open the Google Cloud Console.
> 1. At the top-left corner, click on the Navigation Menu -> IAM & Admin -> Create a Project.
> 1. In the Project Name field, enter a name for your project. (Warning: This cannot be changed so choose carefully).
> 1. Leave the location field default as is.
> 1. Click Create.

After creating a project, the console will navigate to the Dashboard page and the project will be created in a few minutes.

If the project wasn't automatically selected then click on 'select project' on the notification popup, or manually select the project from the drop down selection.
### Enable Google Drive API
Before you can use any of the Google Services, you must first enable the [Google Workspace API](https://developers.google.com/workspace/guides/enable-apis) of the service you wish to use. If you wish to use more than one Google Service, you can enable one or more APIs for a specific project.
>To enable an API in your Google Cloud project:
> 1. Open the Google Cloud Console.
> 1. At the top-left, click on the Navigation Menu > APIs & Services > Library.
> 1. In the search field, enter 'Drive' and press Enter.
> 1. In the list of search results, click the on the Drive API to enable.
> 1. Click Enable. 

If you want to enable more APIs then repeat steps 2–5.
### Set up Authentication 
To access the enabled APIs, Google Projects require you to create credentials with which you can access said APIs. To get an authorization token you must configure a 'OAuth consent screen'; this is the screen where people can choose to allow the application to access their Google Account.

Every request your application sends to the Drive API must include an authorization token. The token also identifies your application to Google.
#### Configure OAuth consent & register your app
> To configure an OAuth Consent Screen:
> 1. Open the Google Cloud Console.
> 1. At the top-left, click on Menu > APIs & Services > [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent).
> 1. Select 'External' user type, then click on Create.
> 1. In the app registration form, fill out the App name field and provide your email in the User support email field and the developer contact information field, then click on Save and Continue.
> 1. In the Scopes section, click on Add or Remove Scopes and search for 'Drive' and select the one with the scope '.../auth/drive', then click Update, then click on Save and Continue.
> 1. Under 'Test Users', leave everything blank and click on Save and Continue.
> 1. Lastly, review the app registration summary and click on Back to Dashboard.
#### OAuth client ID credentials
> To configure an OAuth Consent Screen:
> 1. Open the Google Cloud Console.
> 1. At the top-left, click Menu > APIs & Services > [Credentials](https://console.cloud.google.com/apis/credentials).
> 1. Click Create Credentials > OAuth client ID
> 1. Click Application type > Web application.
> 1. Under Authorized redirect URIs, click '+ADD URI' and paste the following link <u>http<nolink>://localhost:8080/</u> and click Create. (You can also give the client a name.)
> 1. The OAuth client created screen appears, showing your new Client ID and Client secret. __DO NOT SHOW THESE TO ANYONE!__ 
> 1. Download the JSON file and rename it to ***'credentials.json'*** and move/copy it into the folder where the script resides.
***
## Web-Scraping Script Setup
Before running the script it is important to check whether 'credentials.json' is located inside the same folder as the python script is in. Fortunately, there is no need to pip install anything as the virtual environment (.venv) is provided as well.
### Linux Server Crontab

