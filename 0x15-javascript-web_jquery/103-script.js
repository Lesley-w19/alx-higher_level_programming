window.addEventListener('DOMContentLoaded', () => {
    $('INPUT#language_code').keypress(function(event) {
        const keyCode = event.which;
        if (keyCode === 13) {
            const lang = $('INPUT#language_code').val();
            const url = 'https://www.fourtonfish.com/hellosalut/hello/'
            $.get(url + lang, function(data) {
                $('DIV#hello').text(data.hello);
            });
        }
    });
    $('INPUT#btn_translate').click(() => {
        const lang = $('INPUT#language_code').val();
        const url = 'https://www.fourtonfish.com/hellosalut/hello/'
        $.get(url + lang, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });
});