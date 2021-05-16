# tutors (change name later)

# Architecture

## Login Page
`/login` route, give option to create account or sign in to existing one

Backend:

`/api/token-auth/` route accepts `POST`s with username and password as parameters, 
returns either an error message or a token.

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

Done:
* `/api/students`
* `/api/sessions`
* `/api/requests`
* `/api/tutors`
* `/api/users`
* `/api/token-auth`

TODO:
* `/api/roles`

Displays a list of roles for the user that `GET`s this route (some subset of `{'tutor', 'student'}`)

* `api/available-requests`

See "Matching Algorithm" below.

* Detail views for each model.

## Models
* `User` can be connected to a `Student` or `Tutor`, and describes attributes common to any user of the site (email, password, username, etc.)
* `Student` describes student properties
* `Tutor` describes tutor properties
* `TutorSession` describes session properties, outcomes like rating, etc.
* `SessionRequest` is owned by a student, and describes a signal sent to available tutors that a new session is available.
* `Subject` describes the general category of a tutor session and student request.

# Matching Algorithm
Handled by `/api/available-requests`, assigns requests to tutors based on fitness for the problem.

`GET`ting this route as an authenticated tutor serves custom requests to each tutor.

Simplest implementation is to filter available tutors by subject preference (excluding tutors who don't tutor on math for math questions, etc), and rank the resulting list by average tutor rating. 

We can get more fancy in the future with a couple modifications:
1. We weight the ratings of students "similar" to the requester more highly in our list ranking system (this requires we build some similarity metric)
2. We can use some (very simple) language recognition to group similar subjects. For example, if a student requests help with "derivatives", they can be matched to a tutor who offers help with "calculus" because our algorithm recognizes the similarity between these words.

# Jitsi

We're using Jitsi P2P to manage video calls, this can be set up using the Jitsi setup guide for self-hosting.

