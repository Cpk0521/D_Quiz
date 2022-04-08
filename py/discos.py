import json


#   id | title | name | cover
discolist = [ 
    [0, '/', '/', ['np_cd.png']],
    [1, 'Debut single', 'はじめてのかくめい！', ['hajimeteno-kakumei_jk_gentei.jpg', 'hajimeteno-kakumei_jk.jpg']],
    [2, 'Mini Album', 'DREAMY-LOGUE', ['02_dreamy-logue_jk_shokai.jpg', '02_dreamy-logue_jk.jpg']],
    [3, 'きゃにめ&配信限定シングル', 'あたりまえだから', ['03_atarimaedakara_jk.jpg']],
    [4, 'Digital Single', '夏の花火と君と青', ['07_natsuno-hanabi_jk.jpg']],
    [5, '2nd Single', '人生イージー？', ['05_jinsei-easy_jk_syokai.jpg', '05_jinsei-easy_jk.jpg']],
    [6, '3rd Single', 'あやふわアスタリスク', ['06_ayafuwa_jk_syokai.jpg', '06_ayafuwa_jk.jpg']],
    [7, '4th Single', 'おもいでしりとり', ['08_omoide-shiritori_jk_syokai.jpg', '08_omoide-shiritori_jk.jpg']],
    [8, '1st Album', 'DIALOGUE＋1', ['dialogue+1_jk_normal.jpg', 'dialogue+1_jk_shokai.jpg', 'dialogue+1_jk_canime.jpg']],
    [9, 'きゃにめ＆配信限定クリスマスシングル', 'はっちゃけダイアローグ＋クリスマス！', ['xmas_jk.jpg']],
    [10, '5th Single', '僕らが愚かだなんて誰が言った', ['12_bokuraga_jk_shokai.jpg','12_bokuraga_jk_normal.jpg']],
    [11, '6th Single', '恋は世界定理と共に', ['13_koiha-sekaiteirito-tomoni_jk_shokai.jpg', '13_koiha-sekaiteirito-tomoni_jk_normal.jpg']],
]

#   id | name | disco | audio | link | optionshow
audiolist = [
    [1, 'はじめてのかくめい！', [1] , 'lcQiuaHbswg.mp3', [25], 'true'],
    [2, 'ダイアローグ＋インビテーション！', [1] , 'hkJMM_FXmlM.mp3', [], 'true'],
    [3, '大冒険をよろしく', [2] , 'LAyZudsnN0k.mp3', [], 'true'],
    [4, '好きだよ、好き。', [2] , 'J4ZW1q7ASLo.mp3', [], 'true'],
    [5, 'トーク！トーク！トーク！', [2] , '97ykdCh9e6E.mp3', [], 'true'],
    [6, 'Domestic Force!!', [2] , 'gj1a8NzTtkM.mp3', [], 'true'],
    [7, 'パジャマdeパーティー', [2] , 'O53gRU1kAwI.mp3', [], 'true'],
    [8, 'ぼくらは素敵だ', [2] , 'RuLHw5yQcaM.mp3', [], 'true'],
    [9, 'あたりまえだから', [3], 'e3cFgLkNeX8.mp3', [], 'true'],
    [10, '夏の花火と君と青', [4, 8], '6xGC9Wj1tgQ.mp3', [], 'true'],
    [11, '人生イージー？', [5, 8], 'ytFe0hVqI.mp3', [], 'true'],
    [12, '走れ', [5], 'tYb7VFG6MIg.mp3', [], 'true'],
    [13, 'あやふわアスタリスク', [6, 8], 'bgljf35jvUA.mp3', [], 'true'],
    [14, '花咲く僕らのアンサーを', [6], '1M-Qwx3glSY.mp3', [], 'true'],
    [15, 'おもいでしりとり', [7, 8], '1gQ2UbQ11kA.mp3', [], 'true'],
    [16, 'シュガーロケット', [7], 'BT7jyDUP6EQ.mp3', [], 'true'],
    [17, 'Sincere Grace', [8], 'vdZPZGnbX2Q.mp3', [], 'true'],
    [18, 'ドラマティックピース!!', [8], 'wlfIsU82fFk.mp3', [], 'true'],
    [19, '謎解きはキスのあとで', [8], 'BVIVTzPKNF8.mp3', [], 'true'],
    [20, 'プライベイト', [8], 'fMGxBbLwY0M.mp3', [], 'true'],
    [21, 'I my me mind', [8], 'howMD2iAXyw.mp3', [], 'true'],
    [22, 'アイガッテ♡ランテ', [8], '6EPdwJIgQ.mp3', [], 'true'],
    [23, '20xxMUEの光', [8], 'L23gOJFMnK8.mp3', [], 'true'],
    [24, '透明できれい', [8], 'G4IeL2zq-jk.mp3', [], 'true'],
    [25, 'はじめてのかくめい！2021', [8], 'bEsSAAcKQBA.mp3', [1], 'true'],
    [26, 'はっちゃけダイアローグ＋クリスマス！', [9], 'EPBCxGeLybM.mp3', [29, 30, 31, 32, 33, 34, 35, 36], 'true'],
    [27, 'DIALOGUE＋は上々だ', [9], 'JWt8zVI3lpA.mp3', [], 'true'],
    [28, 'DIALOGUE＋はまた立ち上がる', [9], '2lFMSMlCRT4.mp3', [], 'true'],
    [29, 'はっちゃけダイアローグ＋クリスマス！（内山悠里菜 ver.）', [9], 'nR44Y4RLRpg.mp3', [26, 30, 31, 32, 33, 34, 35, 36], 'false'],
    [30, 'はっちゃけダイアローグ＋クリスマス！（稗田寧々ver.）', [9], 'OE6LZXc2JAE.mp3', [26, 29, 31, 32, 33, 34, 35, 36], 'false'],
    [31, 'はっちゃけダイアローグ＋クリスマス！（守屋亨香ver.）', [9], 'ML9IUOJqH8Q.mp3', [26, 29, 30, 32, 33, 34, 35, 36], 'false'],
    [32, 'はっちゃけダイアローグ＋クリスマス！（緒方佑奈ver.）', [9], 'hftnxHg1QN0.mp3', [26, 29, 30, 31, 33, 34, 35, 36], 'false'],
    [33, 'はっちゃけダイアローグ＋クリスマス！（鷹村彩花ver.）', [9], 'bePDB2SpnWQ.mp3', [26, 29, 30, 31, 32, 34, 35, 36], 'false'],
    [34, 'はっちゃけダイアローグ＋クリスマス！（宮原颯希ver.）', [9], 't0nsWs_5HmE.mp3', [26, 29, 30, 31, 32, 33, 35, 36], 'false'],
    [35, 'はっちゃけダイアローグ＋クリスマス！（飯塚麻結ver.）', [9], 'vf79hgyAP2g.mp3', [26, 29, 30, 31, 32, 33, 34, 36], 'false'],
    [36, 'はっちゃけダイアローグ＋クリスマス！（村上まなつver.）', [9], '8HAqIJFbiwg.mp3', [26, 29, 30, 31, 32, 33, 34, 35], 'false'],
    [37, '僕らが愚かだなんて誰が言った', [10], 'o4Btbt4oID0.mp3', [], 'true'],
    [38, '恋は世界定理と共に', [11], 'TE70qKo1Qys.mp3', [], 'true'],
]

jsondata = {'discolist':[], 'Songs':[]}

for disco in discolist:
    discojson = {'id':disco[0], 'title':disco[1], 'name':disco[2], 'cover':[]}
    for img in disco[3]:
        discojson['cover'].append({'file':img})
    jsondata['discolist'].append(discojson)

for song in audiolist:
    songjson = {'id':song[0], 'name':song[1], 'discos':[], 'audio':song[3], 'link':[], 'optshow':song[5]}
    for disco in song[2]:
        songjson['discos'].append({'disco':disco})
    for no in song[4]:
        songjson['link'].append({'id':no})
    jsondata['Songs'].append(songjson)

with open('DataList.json', 'w', encoding='utf-8') as outfile:
    json.dump(jsondata, outfile, indent=4, ensure_ascii=False)