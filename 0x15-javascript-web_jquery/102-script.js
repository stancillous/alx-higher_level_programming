$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.getJSON(
        `https://fourtonfish.com/hellosalut/hello/?lang=${language}`,
        function (data) {
            $('#hello').text(data.hello);
        }
    );
  });
});
