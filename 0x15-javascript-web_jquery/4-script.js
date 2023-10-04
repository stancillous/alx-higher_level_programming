const $header = $('header');
const $div = $('DIV#toggle_header');

$div.on('click', () => {
  const currentClass = $header.attr('class');

  if (currentClass === 'green') {
    $header.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $header.toggleClass(`${currentClass} green`);
  }
});
