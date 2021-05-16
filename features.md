# Feature List

Here's a semi-complete list of features the frontend views will need to support.

# Architecture

## Login Page
Standard login screen, allows user to login with email, or google account

## Student Homepage
The following info will be available to the frontend
* list of available tutors and information (including whether they're online)
* list of previous sessions

The page should implement the following UI features:
* fields to modify student information, preferences
* rating buttons and comment fields for previous sessions (preferably an accordion menu)
* button to make a new request

## Tutor Homepage
`/tutor` route

The following info will be available to the frontend
* list of active student requests
* list of previous sessions

The page should implement the following UI features:
* fields to modify tutor information, preferences
* rating buttons and comment fields for previous sessions (preferably an accordion menu)

## Payment page(s)
The implementation of these will be specific to the payment APIs we integrate with

## Zoom embedding
This is a nice to have feature, the alternative is a zoom redirect when the tutor accepts

## Auto-refresh on status update
We need the page to poll the server to check various conditions, such as:

* whether a new request has been filed (for updating potential tutors with the new opportunity)
* whether a tutor has accepted a reqest (to generate a meeting link and session for the student and tutor)

# Further down the road

Regularly scheduled meetings, office hours, etc.
