# Twitter Bot Memo

## Pitch

Every time someone tweets with #whereami this bot will "find" that user by looking at the geotag of their #whereami post

For example, someone tweets the following:

<blockquote class="twitter-tweet" lang="en"><p>Fell asleep at work for a couple mins and woke up confused af 😂 <a href="https://twitter.com/hashtag/whereamI?src=hash">#whereamI</a></p>&mdash; andrea (@Drea_x0) <a href="https://twitter.com/Drea_x0/status/590702114105614338">April 22, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The bot will respond:

<blockquote class="twitter-tweet" lang="en"><p>Not to worry, I <a href="https://twitter.com/hashtag/found?src=hash">#found</a> you! You're in Washington Square Park! 
</blockquote>
![](https://raw.githubusercontent.com/dflatow/twitter-bot/master/map.png)
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## Extentions

Every time someone tweets with #homesweethome or #worksucks (or maybe #creepy or #privacy), this bot will try and predict<sup>1</sup> the home and work location of that user by looking at that user's previously geotagged posts. If it can find such a location(s) with sufficiently high certainty it will trigger the bot's action.

For example, someone tweets the following:

<blockquote class="twitter-tweet" lang="en"><p>Ever get so bored at work that you balance a hammer ??? <a href="https://twitter.com/hashtag/WorkSucks?src=hash">#WorkSucks</a> <a href="https://twitter.com/hashtag/Boredom?src=hash">#Boredom</a> <a href="http://t.co/Q4bSvzmGxV">pic.twitter.com/Q4bSvzmGxV</a></p>&mdash; C&#39;The Chainsaw&#39;G (@BaltimoreChrisG) <a href="https://twitter.com/BaltimoreChrisG/status/590660413391577089">April 21, 2015</a>
</blockquote>
![](https://pbs.twimg.com/media/CDJygtwW4AA0Wro.jpg:small)
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The bot will respond:

<blockquote class="twitter-tweet" lang="en"><p>Yeah I know it's been a long day, but your home sweet home is waiting! 
</blockquote>
![](https://raw.githubusercontent.com/dflatow/twitter-bot/master/map.png)
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<sup>1</sup> It will use the software I co-authored for a reaseach [paper](https://github.com/dflatow/WSDM_2015_DEMO/wiki/TOY-DEMO) (now published in WSDM  2015) to predict a user's home/work address.

<h1 id="the-steps">The steps</h1>

<ol>
  <li>Bot checks Twitter API endpoint of <a href="https://dev.twitter.com/rest/public/search">public/search</a> for the hashtag #whoami</li>
  <li>For each Tweet, the bot checks if the the post has geolocation enabled</li>
  <li>Look up coordinates in the the coordinates of the post.</li>
  <li>Use the <a href="https://developers.google.com/maps/documentation/embed/guide#search_mode">Google Maps Search API</a> to get the address and a pic.</li>
</ol>


<h1 id="the-steps">Extension steps</h1>

<ol>
  <li>Bot checks Twitter API endpoint of <a href="https://dev.twitter.com/rest/public/search">public/search</a> for the hashtag #worksucks</li>
  <li>For each Tweet, the bot checks if the the user has geolocation enabled</li>
  <li>Predict user's home location</li>
  <li>Use the <a href="https://developers.google.com/maps/documentation/embed/guide#search_mode">Google Maps Search API</a> to get an address and a pic. (Maybe street view?)</li>
</ol>