# tutors (change name later)

# Architecture

## Login Page
`/login` route, give option to create account or sign in to existing one

## Student Homepage
`/student` route, 

* list of available tutors and information (including whether they're online)
* fields to modify student information, preferences
* list of previous sessions, which can be rated and commented on
* button to make a new request (attached to code which will update the page when the request is accepted by a tutor)

## Tutor Homepage
`/tutor` route

* list of active student requests
* fields to modify tutor information, preferences

## API Routes
* `/students` 
* `/tutors`
* `/match` (described below)

## Schemas
* `Subject` describes the possible subjects a student and tutor can discuss during a session.
* `Student` describes student properties
* `Tutor` describes tutor properties
* `TutorSession` describes session properties, outcomes like rating, etc.

# Database
The MVP only needs a SQLite DB, the thing to watch out for here is containing DB abstractions so that when we move to another type of database, refactoring is limited only to the "under the hood" code.

# Matching Algorithm
`/match` REST API route (this is what our frontend will call rather than implementing the algorithm described below in the browser)

Simplest implementation is to filter available tutors by subject preference (excluding tutors who don't tutor on math for math questions, etc), and rank the resulting list by average tutor rating. 

We can get more fancy in the future with a couple modifications:
1. We weight the ratings of students "similar" to the requester more highly in our list ranking system (this requires we build some similarity metric)
2. We can use some (very simple) language recognition to group similar subjects. For example, if a student requests help with "derivatives", they can be matched to a tutor who offers help with "calculus" because our algorithm recognizes the similarity between these words.

# Contributing
I'll push to this repo, and only use unstable branches until I've reviewed that everything on a branch works, then I'll merge it into main.

# Things that are up in the air

## Zoom/Google Meet API
I need to look more closely into which one to use and how these work

