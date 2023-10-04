const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $characterDiv = $('div#character');

$.ajax({
  url,
  dataType: 'json'
}).done((data) => {
  $characterDiv.text(data.name);
});
