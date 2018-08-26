# slido-voter

A small script to spam upvotes on sli.do questions. Since the token in the Authorization header is used to determine
vote author, this script bypasses duplicate vote detection by re-authenticating before every vote request.
A single request can either increase the votes by one or remove a vote if it has already voted. 
Can be made much faster with any async request implementation but I don't see why would anyone need THAT many votes.
As far I've seen there is no flood protection so you can easily get 1k+ votes very quickly.

Usage:
1. Go to any event page in your browser of choice.
2. Your url should look something like this `https://app2.sli.do/event/abcdef/questions`.
3. 'abcdef' is the event slug. Save it for later.
4. Enable any request capturing tool in your browser. 
5. Trigger a request on the question you want to spam votes on(eg. vote on it).
6. The request payload should look something like this: {"event_question_id":1234, (...)}
7. You should now have both the event slug and question id.
8. `pip install -r requirements.txt` in the script directory if needed.
9. Call the script like so: `python vote.py event_slug question_id number_of_votes`. 
   In this example it would be: `python vote.py 'abcdef' 1234 10`(or any other positive number really).
   
