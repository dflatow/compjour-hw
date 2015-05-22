


## Hilary's Emails


## Quick pitch


About a third of the emails from Mrs. Clinton's personal account that were turned over to the House committee investigating the 2012 attack in Benghazi have been released by The New York Times. This project seeks to present the emails in a more informed way than just one big 349 page pdf list of chronologically ordered emails.


## The old way

Read a 349 page pdf of chronological emails.

## The new way

Look at a nice timeline of the Benghazi conflict with links to text format of emails sent by Hilary Clinton.

1. They visit my webpage
2. They view a time-line of the conflict and can easily navigate all email as they occur in relation to the conflict.
3. They can also search for emails containing certain words.

## Data details

### Where does the data come from? How is it collected?

The New York Times released about one third or (349 pages)[https://s3.amazonaws.com/s3.documentcloud.org/documents/2084634/emails.pdf] of the roughly 850 pages of Hilary Clinton's private emails released to the House committee investigating the 2012 attack in Benghazi. 

Through the FOIA the state department has also just recently released (all of the emails)[http://foia.state.gov/Search/Results.aspx?collection=Clinton_Email]. However, as far as I can tell right now there's no systematic way to download all the files and their meta-data.

### What data-cleaning/processing needs to be done?

If getting through NYT:
First we muse use optical character recognition to turn these pdf images into text. We do this using a built in feature of Google drive. Next, we must clean up the data and turn into a more friendly format. For example, we want to separate each individual email, and parse out key information such as the date, recipients, etc.

If using State Dept Website:
We'll need to figure out a way to download all the files with meta-data. They include the following fields "Subject", "Document Date", "From", "To", "Posted Date". 

## Implementation details

### Describe the public-facing endpoints

This is a one-page app. The user goes to this page and clicks on the interactive time-line of the Benghazi conflict and can also search all of the emails.

### How will the data be stored?

The email data and associated text will be stored in plain text files. We'll also include links to the raw image files as well (if possible).

## Who else has done it and how is your attempt better?

There are many articles about the content of these emails:
- [WSJ](http://www.wsj.com/articles/hillary-clintons-benghazi-emails-to-be-released-by-state-department-1432309888)

- [CNN](http://www.cnn.com/2015/05/22/politics/hillary-clinton-emails-release-benghazi/)

- [BBC](http://www.bbc.com/news/world-us-canada-32853708)

- [Gizmodo](http://gizmodo.com/read-hillary-clintons-benghazi-emails-right-here-1706004531) 

However, there's no no convenient way for the public to explore and come to their own conclusions regarding the content of the email. I seek to give that power to the people by making an easy interface to explore the emails.

## Pre-mortem

- __Too hard to download:__ It's obvious that the State Dept is making it as difficult as possible to read all the emails in a nice way. Therefore it might be difficult to programatically access all the emails. That said I'm making some good progress on this front.

- __Too much web design:__ I'm not a super experienced web designer so it might be tough to display all the emails in a nice way on one page as I'd like.

- __Nothing that surprising:__ One big criticism of this corpus of emails is that they're self-released. Not all that surprising that they're no shocking revelations. That said, maybe if we look at the pattern of emails, we can uncover something. For example, suppose we see a suspicious drop-off in email correspondence with key parties involved in the scandal at key times. That may be evidence of obfuscating evidence.

