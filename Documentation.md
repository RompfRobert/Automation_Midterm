# Get Top Artists - Documentation
The aim of this app is to get the top billboard artists this week and the previous 3 weeks, or in short, the most popular artists in the last 4 weeks, this week included. Although, first and foremost, for this application to work as intended, some setup is required by the user.
## Setup

### Google Cloud
https://developers.google.com/workspace/guides/create-project

https://developers.google.com/workspace/guides/enable-apis

## Get Client Secret File
Google Drive API allows you to create apps that leverage Google Drive cloud storage. You can develop applications that integrate with Google Drive, and create robust functionality in your application using Google Drive API.

## Authentication

Every request your application sends to the Drive API must include an authorization token. The token also identifies your application to Google.

Your application must use OAuth 2.0 to authorize requests. No other authorization protocols are supported.

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib csv, scrapy, pandas
```
or
```bash
pip3 install --upgrade pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib csv, scrapy, pandas
```

## Set up Google Cloud Project
To upload the top artists, first and foremost you will need to set up a [Google Cloud account](https://console.cloud.google.com) and to create a project

![Alt Text](img/console%20cloud%20google%2C%20html.jpg "Google Console Cloud, HTML")
![Alt text](img/console%20cloud%20google%2C%20create%20project.jpg "Google Console Cloud, Create Project")

Next, navigating throught the console of the project you wish to use, under the API section, open up the [credentials](https://console.cloud.google.com/apis/credentials).

![Alt Text](img/console%2C%20api%20navigation.jpg)
![Alt text](img/api%2C%20go%20to%20credentials.jpg)