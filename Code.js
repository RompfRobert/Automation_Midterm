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
