from django.db import models
import psycopg2
import csv

class Movie(models.Model):
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    release = models.CharField(max_length=200, default="release")
    url = models.CharField(max_length=200, default="url")

    @staticmethod
    def get_movies():
        with open('ratingsinfo/data/movies.csv', encoding='latin-1') as f:
            conn = psycopg2.connect("dbname=movielens user=Cameron host=/tmp/")
            cur = conn.cursor()
            movies = csv.reader(f, delimiter="|")
            for row in movies:
                movie = Movie(movie_id=row[0], title=row[1], release=row[2], url=row[4])
                movie.save()
            conn.commit()
            cur.close()
            conn.close()


class Rater(models.Model):
    rater_id = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=200, default="sex")
    occupation = models.CharField(max_length=200, default="occupation")

    @staticmethod
    def get_raters():
        with open('ratingsinfo/data/raters.csv', encoding='latin-1') as f:
            conn = psycopg2.connect("dbname=movielens user=Cameron host=/tmp/")
            cur = conn.cursor()
            raters = csv.reader(f, delimiter="|")
            for row in raters:
                rater = Rater(rater_id=row[0], age=row[1], sex=row[2], occupation=row[3])
                rater.save()
            conn.commit()
            cur.close()
            conn.close()


class Rating(models.Model):
    movie_id = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rater_id = models.IntegerField(default=0)

    @staticmethod
    def get_ratings():
        with open('ratingsinfo/data/ratings.csv', encoding='latin-1') as f:
            conn = psycopg2.connect("dbname=movielens user=Cameron host=/tmp/")
            cur = conn.cursor()
            ratings = csv.reader(f, delimiter="\t")
            for row in ratings:
                rating = Rating(rater_id=row[0], movie_id=row[1], score=row[2])
                rating.save()
            conn.commit()
            cur.close()
            conn.close()
