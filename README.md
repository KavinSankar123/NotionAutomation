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
<img width="956" alt="Screen Shot 2023-06-10 at 11 53 46 AM" src="https://github.com/KavinSankar123/NotionAutomation/assets/90232501/2bd04013-410d-4776-90eb-d0b577a42fdc">



## How Does it Work?
- Canvas has an API that allows students to run an API request to fetch their course, assignments, user info, and more.
- How My Script Works:
  - I have one part of the script interacting with the Canvas API to fetch all my assignments from my courses.
  - I have another part of the script acting as an uploader to Notion using the Notion API.
  - When I fetch my assignment info, I parse and package the data to be sent through the Notion API.
  - That's it! 
    - Don't get me wrong, this took a while since I had to figure out how the API's worked and how their data was structured when you fetch information from them. 
