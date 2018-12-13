#!/usr/bin/env python3


""" Udacity - Logs Analysis Project
This project intends to retrieve from database an analysis of the logs.
It is required for the newspaper company ;-)
"""

import psycopg2


def db_connect():
    """Creates a database conn and returns the connection jointly with
        the db instance.
    """
    db = psycopg2.connect("dbname=news")
    conn = db.cursor()
    return db, conn


def do_query(query):
    """Executes a query in the database and returns all the rows as a
        list of tuples.
    """
    db, conn = db_connect()
    conn.execute(query)
    results = conn.fetchall()
    db.close()
    return results


def get_top_articles():
    """Retrieve the three most accessed articles from the web server logs"""
    query = """
        SELECT title, COUNT(*) AS accesses
        FROM articles, log
        WHERE slug=replace(path,'/article/','')
        AND path != '/'
        GROUP BY title
        ORDER BY count(*) DESC
        LIMIT 3
    """
    print("1. What are the most popular three articles of all time?\n")
    results = do_query(query)
    for title, accesses in results:
        print('{} -- {} views'.format(title, accesses))


def get_top_authors():
    """It print the rank of most popular authors based on the accesses
        to their articles.
    """
    query = """
        SELECT name, COUNT(*) AS total
        FROM articles, log, authors
        WHERE authors.id=articles.author
        AND slug=replace(path,'/article/','')
        AND path != '/'
        GROUP BY name
        ORDER BY COUNT(*) DESC
    """
    print("\n2. Who are the most popular article authors of all time?\n")
    results = do_query(query)
    for name, total in results:
        print('{} -- {} views'.format(name, total))


def get_day_errors():
    """It prints out the days where more than 1% of accesses were errors.
    """
    query = """
        SELECT to_char(_.date, 'FMMonth DD, YYYY') AS log_date,
               round(_.error * 100,2)::numeric AS percent_error
        FROM (SELECT date(time),
               AVG(CASE WHEN status = '200 OK' THEN 0 ELSE 1 END) AS error
              FROM log
              GROUP BY date(time)) as _
        WHERE error >= 0.01;
    """
    print("\n3. On which days did more than 1% of requests lead to errors?\n")
    results = do_query(query)
    for date, percent_error in results:
        print('{} -- {}% errors'.format(date, percent_error))


if __name__ == '__main__':
    get_top_articles()
    get_top_authors()
    get_day_errors()
