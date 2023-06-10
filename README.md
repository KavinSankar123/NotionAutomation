# Automated Notion Assignment Manager

## About
Hello! I created this project to automate fetching my assignments from my classes from Canvas and automatically put them on my Notion calendar.

## What is Canvas and Notion?
- Canvas:
  - The University of Pittsburgh, like many other universities, use Canvas to allow professors to post grades, information, and assignments online. 
- Notion:
  - "is a productivity and note-taking web application developed by Notion Labs Inc. It offers organizational tools including task management, project tracking, to-do lists, bookmarking, and more."

### How I use Notion
- I mainly use notion for note taking as well as using their calendars to put my assignments on. It looks something like this:
- 


## How Does it Work?
- Canvas has an API that allows students to run an API request to fetch their course, assignments, user info, and more.
- How My Script Works:
  - I wrote a Python script to automatically make a request through Canvas to fetch all my assignments from all my courses
  - I then package the data to be uploaded to Notion through the Notion API.
