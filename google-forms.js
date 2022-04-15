function myFunction() {
  
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    const artists = sheet.getDataRange().getValues();
  
    Logger.log(artists);
  
    let form = FormApp.create('Top Artists Ranking');
  
    form.addTextItem()
      .setTitle('What is your name?')
  
  
    form.addGridItem()
      .setTitle('Rate the top artists from 1 to 5. 1 being the least liked to 5 being the most liked.')
      .setRows(artists[0])
      .setColumns(['1','2','3','4','5']);
  
    Logger.log('Published URL: ' + form.getPublishedUrl());
  
  }
  