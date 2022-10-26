$.get('https://swapi-api.hbtn.io/api/people/5/?format=json',
  function (data, textStatus, jqXHR) {
    $('DIV#character').text(data.name);
  },
  'JSON'
);
