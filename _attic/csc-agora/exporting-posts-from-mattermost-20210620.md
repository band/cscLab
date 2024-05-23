2021-08-27 Updates by Bill; if warranted

Exporting Messages From Mattermost Via API

Links:

Pete's how-to video, "Exporting Messages From Mattermost Via API"
https://www.youtube.com/watch?v=0Lxx29sd9GY

"API: Authentication"
https://api.mattermost.com/#tag/authentication

```zsh
curl -i -d '{"login_id":"someone@nowhere.com","password":"thisisabadpassword"}' http://localhost:8065/api/v4/users/login
```
 - for some reason the above command did not work, but login did work
   using my personal access token (server config?)

"Mattermost: Personal Access Tokens"
https://docs.mattermost.com/developer/personal-access-tokens.html

"API: Get posts for a channel"
https://api.mattermost.com/#operation/GetPostsForChannel

# use this to get the Team ID
curl -H 'Authorization: Bearer replace-me' https://chat.collectivesensecommons.org/api/v4/teams | jq .

# use this to get the Channel ID
# you can also get the Channel ID in the Mattermost client, use "View Info" in the channel header
curl -H 'Authorization: Bearer replace-me' https://chat.collectivesensecommons.org/api/v4/teams/yzebbrg9njfkdyt74a6kh69qke/channels | jq .

# Use this to get Posts
curl -H 'Authorization: Bearer replace-me' https://chat.collectivesensecommons.org/api/v4/channels/muchxoznm7bn8ykihmtbu9ka7y/posts | jq .
