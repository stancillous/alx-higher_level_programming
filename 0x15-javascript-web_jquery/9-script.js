$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $helloElement = $('div#hello');

  function getSalut () {
    return $.get({
      url,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $helloElement.text(res.hello);
  });
});
