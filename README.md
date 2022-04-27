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
## Web-Scraping and Automation
Before running the script it is important to check whether 'credentials.json' is located inside the same folder as the python script is in. Fortunately, there is no need to pip install anything as the virtual environment (.venv) is provided as well.
### Linux Server Crontab
In a linux environment, you can use Crontab and create a cronjob to run every month. 

Open terminal and type: 
```bash
crontab -e 
```
If you are using crontab for the first time then it will prompt you to choose an editor, while nano is considered easiest the default editor we will be using is Vim. 

Type 2 and press Enter.
```
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]:
```
Next we will need to navigate to the end of the comments, press I on your keyboard to enter insert mode and now we can type the following to run the command every month.
```
0 0 1 * * cd ~/enter/file/path/here && python3 top-artists.py
```
## Google Script
To correctly set up Google Scripts for the newly uploaded top-artists, log in to your [Google Drive](https://drive.google.com/drive/u/0/my-drive).
> 1. Open top-artists Google sheet.
> 1. Click on Extensions > Apps Script
> 1. Copy + Paste the contents of [Code.js](Code.js) or [Code.gs](Code.gs) into the Apps Script program.
> 1. Under Files, click the plus Icon to Add a file and copy and paste the contents of [getAverageRatings.js](getAverageRatings.js) or [getAverageRatings.gs](getAverageRatings.gs) into the editor.

In case you aren't able to open the files mentioned above, you can find them here:
### Code.js / Code.gs
```javascript
function myFunction() {
  
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  const listOfArtists = sheet.getDataRange().getValues();

  let artists = [];
  for (let i = 0; i < listOfArtists.length; i++) {
    artists.push(listOfArtists[i][0]);
  }
  artists.shift();

  Logger.log(listOfArtists);
  Logger.log(artists);

  let form = FormApp.create('Top Artists Ranking');

  form.addTextItem()
    .setTitle('Your name:')
    .setRequired(true);

  form.addGridItem()
    .setTitle('Rate the top artists from 1 to 5. 1 being the least liked to 5 being the most liked.')
    .setRows(artists)
    .setColumns(['1','2','3','4','5']);

  form.setConfirmationMessage('Thank you for your response!')

  Logger.log('Published URL: ' + form.getPublishedUrl());

}
```
### getAverageRatings.js / getAverageRatings.gs
```javascript
function myFunction() {
  // Open a form by ID and log the responses to each question.
  // Copy + Paste the ID of the Google Drive folder into the id variable below
  const id = '';

  // ---------------------------------------------------------------------------
  let form = FormApp.openById(id);

  var formResponses = form.getResponses();

  var allRatingsRaw = [];
  var allRatings = [];

  for (var i = 0; i < formResponses.length; i++) {
    var formResponse = formResponses[i];
    var itemResponses = formResponse.getItemResponses();
    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      allRatingsRaw.push(itemResponse.getResponse());
    }
  }

  Logger.log(allRatingsRaw)

  let nums = [];
  let sum = 0;
  let results = [];

  for (let i = 1; i < allRatingsRaw.length; i+=2) {
      allRatings.push(allRatingsRaw[i]);
  }

  const count = allRatings.length;

  for (let i = 0; i < allRatings[0].length; i++) {
      nums.push(i);
  }

  for (let i = 0; i < nums.length; i++) {
      for (let r = 0; r < allRatings.length; r++) {
          let n = allRatings[r][nums[i]];
          sum = parseInt(sum) + parseInt(n);
      }
      let result = sum / count;
      results.push(result);
      sum = 0;
  }
  Logger.log(results)
  
  const app = SpreadsheetApp;
  let activeSheet = app.getActiveSpreadsheet().getActiveSheet();

  // get current active sheet
  for (let i = 0; i < results.length; i++) {
    activeSheet.getRange(2+i, 2).setValue(results[i])
  }
}
```