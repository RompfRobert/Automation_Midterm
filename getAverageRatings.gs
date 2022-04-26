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
