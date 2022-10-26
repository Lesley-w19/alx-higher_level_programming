$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get(
      'https://www.fourtonfish.com/hellosalut/hello/' + $.param(
        { lang: $('INPUT#language_code').val() }
      ), function (data) {
        $('DIV#hello').html(data.hello);
      });
  });
});
