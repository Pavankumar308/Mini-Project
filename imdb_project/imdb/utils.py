def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows

from .models import *

def get_imdb_multi_line_plot_with_area_data():
    import json

    get_movies_1 = """
        SELECT COUNT(*),
            AVG(avg_rating) 
        FROM imdb_movie
        WHERE release_date 
        BETWEEN '1980-01-01' AND '1990-01-01';
    """
    get_movies_2 = """
        SELECT COUNT(*),
            AVG(avg_rating) 
        FROM imdb_movie
        WHERE release_date 
        BETWEEN '1990-01-01' AND '2000-01-01';
    """
    get_movies_3 = """
        SELECT COUNT(*),
            AVG(avg_rating) 
        FROM imdb_movie
        WHERE release_date 
        BETWEEN '2000-01-01' AND '2010-01-01';
    """
    get_movies_4 = """
        SELECT COUNT(*),
            AVG(avg_rating) 
        FROM imdb_movie
        WHERE release_date 
        BETWEEN '2010-01-01' AND '2020-01-01';
    """
    get_movies_5 = """
        SELECT COUNT(*),
            AVG(avg_rating) 
        FROM imdb_movie
        WHERE release_date 
        BETWEEN '2020-01-01' AND '2030-01-01';
    """
    count_avg = [get_movies_1, get_movies_2, get_movies_3, get_movies_4, get_movies_5]
    multi_line_plot_with_area_data = {
        "labels": [
            "1980-90", "1990-00", "2000-10", "2010-20", "2020-30",],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "Number of movies",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,255,0.7)",
                "data": [execute_sql_query(get_movies_1)[0][0], 
                            execute_sql_query(get_movies_2)[0][0],
                            execute_sql_query(get_movies_3)[0][0], 
                            execute_sql_query(get_movies_4)[0][0],
                            execute_sql_query(get_movies_5)[0][0]
                ]
            },
            {
                "label": "Avarage rating",
                "borderColor": "rgba(200, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [execute_sql_query(get_movies_1)[0][1],  
                            execute_sql_query(get_movies_2)[0][1],
                            execute_sql_query(get_movies_3)[0][1], 
                            execute_sql_query(get_movies_4)[0][1],
                            execute_sql_query(get_movies_5)[0][1]
                ]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Best movie seasons'
    }

def get_imdb_multi_line_plot_data():
    import json

    query = """
        SELECT d.name, 
            COUNT(*), 
            ROUND(AVG(m.avg_rating), 3)*10
        FROM imdb_movie AS m 
            INNER JOIN imdb_director AS d
            ON d.id = m.director_id
        GROUP BY d.id
        ORDER BY AVG(m.avg_rating) DESC
        LIMIT 5;
    """
    query_list = list(set(execute_sql_query(query)))

    director_list = []
    no_of_movies = []
    success_rate = []
    for item in query_list:
        director_list.append(item[0])
        no_of_movies.append(item[1])
        success_rate.append(item[2])

    multi_line_plot_data = {
        "labels": director_list,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Movies",
            "data": no_of_movies,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Success rate(%)",
            "data": success_rate,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Top Five Directors success rate'
    }


def get_imdb_two_bar_plot_data():
    import json

    query = """
        SELECT AVG(m.avg_rating), COUNT(*)
        FROM imdb_movie AS m 
        GROUP BY strftime('%m', m.release_date)
        ORDER BY strftime('%m', m.release_date);
    """
    query_list = execute_sql_query(query)
    no_of_movies = []
    avg_rating_in_month = []
    for data in query_list:
        no_of_movies.append(data[1])
        avg_rating_in_month.append(data[0])
    multi_bar_plot_data = {
        "labels": ["January", "February", "March", "April", "May", "June",
                   "July", 'August', 'September', 'October', 'November', 'December'],
        "datasets": [
            {
                "label": "Movies",
                "data": no_of_movies,
                "borderColor": "rgba(0, 200, 200, 0.09)",
                "borderWidth": "0",
                "backgroundColor": "#a05195",
                "fontFamily": "Poppins"
            },
            {
                "label": "Avarage Rating",
                "data": avg_rating_in_month,
                "borderColor": "rgba(255,255,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "#f95d6a",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Movies and Actors'
    }

def single_imdb_bar_chart_data_one():
    import json

    query = """
        SELECT m.genre, 
        count(*)
        FROM imdb_movie AS m
        INNER JOIN imdb_cast AS c
            ON c.movie_id = m.movie_id
        GROUP BY m.genre;
    """
    query_list = list(set(execute_sql_query(query)))
    genre_list = []
    actors_list = []
    for item in query_list:
        genre_list.append(item[0])
        actors_list.append(item[1])
    single_bar_chart_data = {
        "datasets": [{
            'label': 'Number of actors',
            "data": actors_list,
            "backgroundColor": [
                "#003f5c",
                "#2f4b7c",
                "#665191",
                "#a05195",
                "#d45087",
                "#f95d6a",
                "#ff7c43",
                "#ffa600"
            ],
            "hoverBackgroundColor": [
                "#003f5c",
                "#2f4b7c",
                "#665191",
                "#a05195",
                "#d45087",
                "#f95d6a",
                "#ff7c43",
                "#ffa600"
            ]

        }],
        "labels": genre_list
    }

    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Actors in Genre'
    }


def get_imdb_polar_chart_data():
    import json

    query = """
        SELECT d.name, 
        COUNT(*)
        FROM (imdb_movie AS m
            INNER JOIN imdb_director AS d
            ON d.id = m.director_id)
        INNER JOIN imdb_cast AS c
        ON m.movie_id = c.movie_id
        GROUP BY d.id
        ORDER BY COUNT(*) DESC
        LIMIT 5;
    """

    query_list = execute_sql_query(query)
    query_list = list(set(query_list))
    director_list = []
    actors_list = []
    for item in query_list:
        director_list.append(item[0])
        actors_list.append(item[1])

    polar_chart_data = {
        "datasets": [{
            "data": actors_list,
            "backgroundColor": [
                "#003f5c",
                "#2f4b7c",
                "#665191",
                "#a05195",
                "#d45087",
                "#f95d6a",
                "#ff7c43",
                "#ffa600"
            ]

        }],
        "labels": director_list
        
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Director with Actors'
    }


def populate_database_actors():
    import json
    from random import randint
    import datetime

    f = open('/home/rgukt/Desktop/complete_data/actors_5000.json', 'r')
    actors_list = f.read()
    actors_list = json.loads(actors_list)
    for actor in actors_list:
        date=datetime.date(randint(1850, 2000), randint(1,12),randint(1,28))
        if actor['fb_likes'] == '':
            actor['fb_likes'] = '0'
        a = Actor(actor_id=actor['actor_id'],name=actor['name'],  gender=actor['gender'], fb_likes=int(actor['fb_likes']), date_of_birth=date)
        a.save()

    
def populate_database_directors():
    import json
    f = open('/home/rgukt/Desktop/complete_data/directors_5000.json', 'r')
    directors_list = f.read()
    directors_list = json.loads(directors_list)
    for director in directors_list:
        if director['no_of_facebook_likes'] == '':
            director['no_of_facebook_likes'] = '0'
        d = Director(name=director['name'], gender=director['gender'], no_of_facebook_likes=director['no_of_facebook_likes'])
        d.save()
def populate_database_movies():
    import json
    from random import randint, choice
    import datetime
    f = open('/home/rgukt/Desktop/complete_data/movies_5000.json', 'r')
    movies_list = f.read()
    movies_list = json.loads(movies_list)
    for movie in movies_list:
        if movie['likes_on_fb'] == '':
            movie['likes_on_fb'] = '0'
        if movie['budget'] == '':
            movie['budget'] = '100'
        if movie['year_of_release'] == '':
            movie['year_of_release'] = '2000'
        if movie['average_rating'] == '':
            movie['average_rating'] = '0'
        
        movie_director = Director.objects.get(name=movie['director_name'])
        date =  date=datetime.date(int(movie['year_of_release']), randint(1,12),randint(1,28))
        movie_genre = choice(movie['genres'])
        try:
            Movie.objects.get(movie_id=movie['movie_id'])
        except Movie.DoesNotExist:
            m = Movie.objects.create(movie_id=movie['movie_id'],
                name=movie['name'],
                release_date=date,
                imdb_link=movie['imdb_link'],
                avg_rating=float(movie['average_rating']),
                budget=int(movie['budget']),
                collections=movie['box_office_collection_in_crores'],
                language=movie['language'],
                country=movie['country'],
                likes_on_fb=int(movie['likes_on_fb'],),
                genre = movie_genre,
                director=movie_director
            )
            m.save()
            for actor in movie['actors']:
                a = Actor.objects.get(actor_id=actor['actor_id'])
                c = Cast.objects.create(actor=a, movie=m, role=a.name)
                c.save()