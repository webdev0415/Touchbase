# 0 = at root, example.com/username
# 1 = example.com/u/username
# 2 = username.example.com
# 3 = example.com/user/username
# 4 = example.com/profile/username
# 5 = example.com/people/username
# 6 = example.com/add/username
# 7 = api.whatsapp.com/send?phone=15551234657
# 8 = example.com/players
# 9 = origin.com/usa/en-us/search?searchString=username
# 10 = example.com/c/username
# 11 = example.com/users/username
# 12 = example.com/lover/
# 13 = example.com/main/user.php?user=username
# 14 = example.com/ui/users/username
# 15 = example.com/wiki/User:username
# 16 = example.com/p/username
# 17 = example.com/member/username
# 18 = example.com/traders/username
# 19 = example.com/accounts/username
# 20 = example.com/@/username
# 21 = example.com/api/media/live/username
# 22 = example.com/members/username
# 23 = example.com/photographer/username

# 24 = OAuth
# 25 = entered username
# 26 = entered WeChat ID
# 27 = entered name and number mehar#2202
# 28 = entered url

# exclude in string concat:
#   oauth, username, url, nameandnumber


OAF_supported = [
    'youtube.com',
    'steamcommunity.com'
]


url_c_list = {

    '/': [
        "instagram.com",
        "facebook.com",
        "twitter.com",
        "vsco.co",
        "kik.me",
        "vk.com",
        "telegram.me", #
        "myspace.com", 
        "flipboard.com/@",
        "gab.ai",
        "disqus.com",
        "ask.fm",
        "coroflot.com",
        "patreon.com",
        "pexels.com/@",
        "creativemarket.com",
        "dailymotion.com",
        "profiles.wordpress.org",
        "designspiration.com",
        "cash.app/$",
        "mixer.com",
        "gfycat.com/@",
        "producthunt.com/@",
        "ok.ru",
        "devrant.com",
        "younow.com",
        "tellonym.me",
        "taringa.net",
        "scribd.com",
        "reverbnation.com",
        "rateyourmusic.com/~",
        "repl.it/@",
        "slideshare.net",
        "weheartit.com",
        "virgool.io/@",
        "vimeo.com",
        "venmo.com",
        "unsplash.com/@",
        "twitch.tv",
        "dribbble.com",
        "ello.co",
        "eyeem.com",
        "foursquare.com",
        "giphy.com",
        "gitlab.com",
        "goodreads.com",
        "en.gravatar.com",
        "mstdn.io/@",
        "meetme.com",
        "mixcloud.com",
        "news.ycombinator.com/user?id=",
        "hackerone.com",
        "imageshack.us",
        "issuu.com",
        "hubpages.com/@",
        "coderwall.com",
        "pscp.tv",
        "mix.com",
        "codepen.io",
        "launchpad.net/~",
        "leetcode.com",
        "letterboxd.com",
        "kaggle.com",
        "keybase.io",
        "dev.to",
        "arc.dev",
        "psnprofiles.com",
        "pinterest.com",
        "funnyordie.com",
        "github.com",
        "genius.com",
        "soundcloud.com",
        "buzzfeed.com",
        "canva.com",
        "medium.com/@",
        "tinder.com/@", 
        "deviantart.com",
        "fotolog.com",
        "500px.com",
        "behance.net",
        "bitbucket.org",
        "angel.co",
        "blip.fm",
    ],


    '/u/': [
        "gog.com",
        "9gag.com",
        "reddit.com",
        "tradingview.com",
        "hub.docker.com",
        "fandom.com",
        "sourceforge.net",
        "community.signalusers.org",
        "pastebin.com"
    ],


    'subdomain': [
        "livejournal.com",
        "skyrock.com",
        "sarahah.com",
        "tumblr.com",
        "bandcamp.com",
        "blogspot.com",
        "carbonmade.com",
        "contently.com",
        "slack.com",
        "rajce.idnes.cz",
        "webnode.cz",
        "newgrounds.com",
        "itch.io",
        "jimdosite.com",
    ],


    '/user/': [
        "wattpad.com",
        "ifunny.co",
        "imgur.com",
        "crunchyroll.com",
        "discogs.com",
        "last.fm",
        "houzz.com",
        "trip.skyscanner.com",
        "api.kano.me/progress",
        "speedrun.com",
        "photobucket.com",
    ],


    '/profile/': [
        "okcupid.com",
        "kickstarter.com",
        "app.codesignal.com",
        "myanimelist.net",
        "badoo.com",
        "bitcoinforum.com",
        "namemc.com",
        "researchgate.net",
        "house-mixes.com"
        
    ],

    '/people/': [
        "etsy.com",
        "zhihu.com"
    ],

    '/add/': [
        "snapchat.com"
    ],

    'whatsapp': [
        "whatsapp.com"
    ],

    '/players/': [
        "faceit.com/en"
    ],


    #----------------================----------------================----------------================----------------================


    '/usa/en-us/search?searchString=': [ 
        "origin.com"
    ],


    '/c/': [
        "cloob.com"
    ],

    '/users/': [
        "codechef.com",
        "osu.ppy.sh",
        "trakt.tv",
        "pokemonshowdown.com",
        "pixabay.com/en"
    ],


    '/lover/': [
        "colourlovers.com"
    ],


    '/main/user.php?user=': [
        "imgsrc.ru"
    ],


    '/ui/users/': [
        "virustotal.com"
    ],


    '/wiki/User:': [
        "wikipedia.org"
    ],


    '/p/': [
        "ifttt.com"
    ],


    '/member/': [
        "instructables.com"
    ],


    '/traders/': [
        "investing.com"
    ],


    '/accounts/': [
        "kongregate.com"
    ],


    '/@/': [
        "plug.dj"
    ],


    '/api/media/live/': [
        "smashcast.tv"
    ],


    '/members/': [
        "tripadvisor.com"
    ],


    '/photographer/': [
        "youpic.com"
    ],


    'oauth': [
        "youtube.com", #https://developers.google.com/youtube/v3/guides/authentication
        "google.com", #,https://stackoverflow.com/questions/12662127/how-to-get-user-id-after-login-with-google-oauth
        "linkedin.com", #https://developer.linkedin.com/docs/oauth2 and https://developer.linkedin.com/docs/guide/v2/people/profile-api 
        "steamcommunity.com", #https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0001.29 and https://www.youtube.com/watch?v=DRAPS4FSmbk and https://www.youtube.com/watch?v=YpQuKZ7tqY4 
        "ebay.com", #https://developer.ebay.com/api-docs/static/oauth-tokens.html 
        "viber.com", #https://developers.viber.com/docs/api/rest-bot-api/
        "stackoverflow.com" #https://api.stackexchange.com/docs/authentication
    ],

    'username': [
        "uplay.ubisoft.com",
        "skype.com",
        "flickr.com",
        "xbox.com",
        "roblox.com",
        "pof.com", #plenty of fish
        "houseparty.com",
        "spotify.com",

    ],


    'wechat': [ #uses WeChat ID
        "wechat.com"
    ],


    'nameandnumber': [ #name and number means that the account is shaped as "example#1234"
        "discordapp.com",
        "battle.net"
    ],


    'url': [
        "amazon.com", #Amazon Wishlist
        "gofundme.com", #GoFundMe Campaign
        "kickstarter.com", #Kickstarter Campaign
        "dropbox.com", #Dropbox link
        "letgo.com", #Profile Link
        "teamspeak.com", #IP address or website link
        "about.me", #Profile Link
        "academia.edu", #Profile Link
        "en.aptoide.com", #App Store Link
        "basecamp.com", #opt in link
        "onyolo.com" #Profile Link
    ],
}


# old
# url_c_list = {

#     '/': [
#         "instagram.com",
#         "facebook.com",
#         "twitter.com",
#         "vsco.co",
#         "kik.me",
#         "vk.com",
#         "telegram.me",
#         "myspace.com",
#         "gab.ai",
#         "ask.fm",
#         "pscp.tv", # Periscope
#         "mix.com",
#         "psnprofiles.com", # Playstation network
#         "pinterest.com",
#         "funnyordie.com",
#         "github.com",
#         "genius.com",
#         "medium.com/@", #
#         "tinder.com/@", #
#         "deviantart.com",
#         "fotolog.com",
#     ],


#     '/u/': [
#         "gog.com",
#         "9gag.com",
#         "reddit.com",
#         "tradingview.com"
#     ],


#     'subdomain': [
#         "livejournal.com",
#         "skyrock.com",
#         "sarahah.com",
#         "tumblr.com"
#     ],


#     '/user/': [
#         "wattpad.com",
#         "ifunny.co",
#         "imgur.com",
#     ],


#     '/profile/': [
#         "okcupid.com",
#         "kickstarter.com",
#         "app.codesignal.com"
#     ],

#     '/people/': [
#         "etsy.com",
#     ],

#     '/add/': [
#         "snapchat.com"
#     ],

#     'whatsapp': [
#         "whatsapp.com"
#     ],

#     '/players/': [
#         "faceit.com/en"
#     ],


#     'oauth': [
#         "youtube.com",
#         "plus.google.com", # ha, ded
#         "linkedin.com",
#         "amazon.com",
#         "soundcloud.com",
#         "steamcommunity.com"
#     ]

# }