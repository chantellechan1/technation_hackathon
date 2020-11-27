# Expected Twitter API Data

This file contains the expected formats of responses from Twitter API for various routes.

### GET /2/tweets/search/recent
```json

{
    "data": [
        {
            "author_id": "22492650",
            "created_at": "2020-11-27T03:54:59.000Z",
            "entities": {
                "annotations": [
                    {
                        "end": 31,
                        "normalized_text": "Adam's Barbeque",
                        "probability": 0.2943,
                        "start": 17,
                        "type": "Organization"
                    },
                    {
                        "end": 77,
                        "normalized_text": "Toronto",
                        "probability": 0.9986,
                        "start": 71,
                        "type": "Place"
                    }
                ],
                "hashtags": [
                    {
                        "end": 245,
                        "start": 229,
                        "tag": "adamsonbarbeque"
                    },
                    {
                        "end": 257,
                        "start": 246,
                        "tag": "AdamsonBBQ"
                    },
                    {
                        "end": 274,
                        "start": 258,
                        "tag": "adamsonbarbecue"
                    }
                ]
            },
            "id": "1332171031235190789",
            "text": "What happened to Adam's Barbeque was disgraceful.\n\nShootings are up in Toronto (all time high) and they sent 60 police officers to ONE small business.\n\nSmall businesses made up with 1% of the covid cases but they need to close?\n\n#adamsonbarbeque #AdamsonBBQ #adamsonbarbecue"
        },
        {
            "author_id": "1160616382972780545",
            "created_at": "2020-11-27T03:46:45.000Z",
            "entities": {
                "annotations": [
                    {
                        "end": 30,
                        "normalized_text": "ONTARIO AUDITOR GENERAL",
                        "probability": 0.5545,
                        "start": 8,
                        "type": "Organization"
                    },
                    {
                        "end": 47,
                        "normalized_text": "FORD",
                        "probability": 0.8147,
                        "start": 44,
                        "type": "Organization"
                    }
                ],
                "urls": [
                    {
                        "display_url": "instagram.com/p/CIBUGqthPGJ/\u2026",
                        "end": 260,
                        "expanded_url": "https://www.instagram.com/p/CIBUGqthPGJ/?fbclid=IwAR3UCJnQYdWvPIIUsAyEfI3yyu-V71R9HoO86Kkd4SX8HDbVbPyFK-LH6Rg",
                        "start": 237,
                        "url": "https://t.co/jMMJAn77K2"
                    }
                ]
            },
            "id": "1332168962528792576",
            "text": "Copied: ONTARIO AUDITOR GENERAL report says FORD did NOT use Public Health advice but used his own decisions on masks and covid measures with no science back up. He is destroying the middle class business for the new world order reset. \nhttps://t.co/jMMJAn77K2"
        }
    ],
    "meta": {
        "newest_id": "1332171031235190789",
        "next_token": "b26v89c19zqg8o3fosesr2puvbmb6phci8w95ly1oe7b1",
        "oldest_id": "1332155430898782208",
        "result_count": 11
    }
}

```