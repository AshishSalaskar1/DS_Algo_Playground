### Steps to get OAuth 2.0 token
1. Create a linkedin account with atleast 1 connection
2. Create a company page
3. Verify company page by linking with personal account
4. Product > Enable (Share on LinkedIn, Sign In with LinkedIn using OpenID Connect)
5. Auth -> Right bar -> Create OAuth2.0 -> login -> give all permissions -> copy token


### Upload Custom Image
1. registerUpload -> gives you back mediaUrl and uploadUrl
2. upload image to uploadUrl
3. You can then use mediaUrl for giving URL path

POST PATH: https://www.linkedin.com/feed/update/urn:li:share:7155121104653635584/