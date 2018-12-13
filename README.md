# Logs Analysis Project

This project intends to retrieve from database an analysis of the logs for a newspaper company.

This is part of the required projects for Udacity Nanodegree Progam.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Understanding the project

The PostgreSQL database contais fictional data from a news website.

The sample database constists in three tables:

* **articles**: contains the publicized articles with its details
* **authors**: contains the author data and its bio
* **log**: contains the web server logs indicating the accessed articles for each day

The logs_analysis.py script will be able to answer to three questions:

**1. What are the most popular three articles of all time?**

Where the anwser should be:

	Candidate is jerk, alleges rival -- 338647 views
	Bears love berries, alleges bear -- 253801 views
	Bad things gone, say good people -- 170098 views

**2. Who are the most popular article authors of all time?**

Where the anwser should be:

	Ursula La Multa -- 507594 views
	Rudolf von Treppenwitz -- 423457 views
	Anonymous Contributor -- 170098 views
	Markoff Chaney -- 84557 views

**3. On which days did more than 1% of requests lead to errors?**

Where the anwser should be:

	July 17, 2016 -- 2.26% errors

## Requirements

In order to run the script, you'll need:

* **Python 3**;
* **PostgreSQL** (version 9.X or greater);
* **psycopg2** python library (install it with `pip install psycopg2`);

## Optional requirement

You could run this project in a Vagrant VM, as provided in the `Vagratfile`.

## How to run?

Once you've downloaded and installed the Vagrant VM, you're ready to run the script.

1. In your terminal, start the VM with `vagrant up`

2. Access it with `vagrant ssh`

3. Go to the shared folder: `cd /vagrant`

4. Make sure you've cloned this repository in your local machine inside the **vagrant** folder

5. Import the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) (make sure to unzip it) to the PostgreSQL database: `psql -d news -f newsdata.sql`

6. Access the folder where the **logs_analysis.py** is located and run it with **python3 logs_analysis.py**

## Author

* **Alexandre Marcel Lucas** - Udacity student
