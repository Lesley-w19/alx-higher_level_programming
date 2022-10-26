$.get(
  'https://swapi-api.hbtn.io/api/films/?format=json',
  (data, textStatus, jqXHR) => {
    const allMovies = data.results;

    $.each(allMovies, function (index, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  },
  'JSON'
);
