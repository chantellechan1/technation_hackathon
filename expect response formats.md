# Expected Twitter API Data

This file contains the expected formats of responses from Twitter API for various routes.

### GET /2/tweets/search/recent
```json
{
    "data": [
        {
            "author_id": "713735624",
            "id": "1331802879359819783",
            "text": "I forgot to post my finished glow in the dark floating cat head gown. Worn here with the harness I made a month or so ago. My nails match the dress too. https://t.co/py7jZKkW4Y"
        },
        {
            "author_id": "2991801188",
            "id": "1331802843427139585",
            "text": "@cat_0401 \u500b\u4eba\u5b85\u306b\u3066\u30af\u30bd\u72ed\u3044()\u304a\u82b1\u5c4b\u3055\u3093\u55b6\u3093\u3067\u307e\u3059\ud83d\ude47\u200d\u2642\ufe0f https://t.co/eAWatgW1BG"
        },
        {
            "author_id": "1317520450486824960",
            "id": "1331802786644811778",
            "text": "cat. wit a cone https://t.co/ALhqRWe5Sb"
        },
        {
            "author_id": "2450395334",
            "id": "1331802782404382721",
            "text": "Jenny Any Dot unzipping her skin to reveal a second skin underneath covered in a bedazzled cat body suit is queer culture. I won\u2019t be explaining this. https://t.co/6uk635uwt2"
        },
        {
            "author_id": "1073673742524411904",
            "id": "1331802762661617665",
            "text": "@hukumaru_cat \u3069\u308c\u3060\u3051\u5426\u5b9a\u3055\u308c\u3066\u3082\u8cab\u304f\u30ab\u30fc\u30c9\u3002 https://t.co/vO7YJIvIvp"
        },
        {
            "author_id": "6778212",
            "id": "1331802738146107393",
            "text": "It\u2019s not the holiday season if Coco Cat doesn\u2019t climb our tree at least once. https://t.co/TeHtulrWzV"
        },
        {
            "author_id": "44708928",
            "id": "1331802736279638016",
            "text": "@kelseybick Christmas Cat motivation: https://t.co/iydLuQS9dF"
        },
        {
            "author_id": "915523513074589697",
            "id": "1331802718625689601",
            "text": "\u4eca\u65e5\u306e\u306b\u3083\u3093\u3053\n\n\u624b\u306e\u4f4d\u7f6e\u304c\u304a\u3082\u3057\u308d\u3044\ud83d\ude0a\n#\u732b #\u30a2\u30e1\u30b7\u30e7 #\u306d\u3053 #\u732b\u597d\u304d #\u732b\u5199\u771f #cat #\u98fc\u3044\u732b #\u306b\u3083\u3093\u3053 #\u30da\u30c3\u30c8 #\u732b\u3068\u66ae\u3089\u3059 #\u30a2\u30e1\u30ea\u30ab\u30f3\u30b7\u30e7\u30fc\u30c8\u30d8\u30a2 #\u732b\u306e\u3044\u308b\u66ae\u3089\u3057 https://t.co/yn8Hpm1vAr"
        },
        {
            "author_id": "1323640813608300544",
            "id": "1331802711730188289",
            "text": "This makes my cat look fat and the way she seat \ud83d\ude02\ud83d\ude02\ud83d\ude02 https://t.co/PaCak9WADl"
        },
        {
            "author_id": "1963740164",
            "id": "1331802698052669440",
            "text": "@PatriotAJGhost @pannrising @MurderFancier @kingcarlin3 @cookiem89151957 @_Testy2 @OGKBEAR @Beanie_girl89 @OmarRises @soul_katz @AlexH1717 @AnnieGetHerGun @MelTheBos1 @MeltingInMarana @socratesrocks @IamAmySueCase @4trumpAmy @tammiesawakenow @TankSaysFu @JamesNamegame @CarolinaIsAlpha @ECRoberts3 @RedStateYankee @DaGreatSloth @bryan2_60 @NeekoalTX @Mongo3804 @TheFUNGIS1 @DamCL3 @MAGAKAGAlways @OU_KAG @BH_Teddy_911 @Blondies45 @SexyAssPatriot2 @realNick_777 @PraiseInHisName @fastcow26 @kingfre3dom @Jamesnathanham2 @RebelBaroness35 @RebelNurse76 @jaal811 @nancyleeca @Diabeetus_Cat @Patriot3651 Thank ya AJ, proud to ride!\ud83d\udc4a\ud83c\udffc\ud83c\uddfa\ud83c\uddf8\ud83d\udc4d\ud83c\udffb https://t.co/mMeN7EWVd7"
        }
    ],
    "meta": {
        "newest_id": "1331802879359819783",
        "next_token": "b26v89c19zqg8o3fosescbzhwx1boip44g36wy75mtsot",
        "oldest_id": "1331802698052669440",
        "result_count": 10
    }
}
```

one tweet with the entities:
```python
{
    'created_at': '2020-11-26T04:16:57.000Z', 
    'author_id': '3065523432', 
    'text': "@alexboakeillo Here's my girl, Rynisa! Swashbuckling Arcane Trickster with her cat, Effie! https://t.co/Id4usfpp56", 
    'entities': {
        'urls': [
            {'start': 91, 'end': 114, 'url': 'https://t.co/Id4usfpp56', 'expanded_url': 'https://twitter.com/Em_Nemma/status/1331814173978759169/photo/1', 'display_url': 'pic.twitter.com/Id4usfpp56'}, 
            {'start': 91, 'end': 114, 'url': 'https://t.co/Id4usfpp56', 'expanded_url': 'https://twitter.com/Em_Nemma/status/1331814173978759169/photo/1', 'display_url': 'pic.twitter.com/Id4usfpp56'}
        ], 
        'mentions': [
            {'start': 0, 'end': 14, 'username': 'alexboakeillo'}
        ], 
        'annotations': [
            {'start': 31, 'end': 36, 'probability': 0.4124, 'type': 'Person', 'normalized_text': 'Rynisa'}, 
            {'start': 84, 'end': 88, 'probability': 0.4385, 'type': 'Person', 'normalized_text': 'Effie'}
        ]
    }, 
    'id': '1331814173978759169'
    }
```