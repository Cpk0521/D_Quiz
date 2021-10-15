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
    [8, '1st Album', 'DIALOGUE＋1', ['dialogue+1_jk_normal.jpg', 'dialogue+1_jk_shokai.jpg', 'dialogue+1_jk_canime.jpg']]
]

#   id | name | disco | audio | Must
audiolist = [
    [1, 'はじめてのかくめい！', [1] , 'lcQiuaHbswg.mp3', [25]],
    [2, 'ダイアローグ＋インビテーション！', [1] , 'hkJMM_FXmlM.mp3', []],
    [3, '大冒険をよろしく', [2] , 'LAyZudsnN0k.mp3', []],
    [4, '好きだよ、好き。', [2] , 'J4ZW1q7ASLo.mp3', []],
    [5, 'トーク！トーク！トーク！', [2] , '97ykdCh9e6E.mp3', []],
    [6, 'Domestic Force!!', [2] , 'gj1a8NzTtkM.mp3', []],
    [7, 'パジャマdeパーティー', [2] , 'O53gRU1kAwI.mp3', []],
    [8, 'ぼくらは素敵だ', [2] , 'RuLHw5yQcaM.mp3', []],
    [9, 'あたりまえだから', [3], 'e3cFgLkNeX8.mp3', []],
    [10, '夏の花火と君と青', [4, 8], '6xGC9Wj1tgQ.mp3', []],
    [11, '人生イージー？', [5, 8], 'ytFe0hVqI.mp3', []],
    [12, '走れ', [5], 'tYb7VFG6MIg.mp3', []],
    [13, 'あやふわアスタリスク', [6, 8], 'bgljf35jvUA.mp3', []],
    [14, '花咲く僕らのアンサーを', [6], '1M-Qwx3glSY.mp3', []],
    [15, 'おもいでしりとり', [7, 8], '1gQ2UbQ11kA.mp3', []],
    [16, 'シュガーロケット', [7], 'BT7jyDUP6EQ.mp3', []],
    [17, 'Sincere Grace', [8], 'vdZPZGnbX2Q.mp3', []],
    [18, 'ドラマティックピース!!', [8], 'wlfIsU82fFk.mp3', []],
    [19, '謎解きはキスのあとで', [8], 'BVIVTzPKNF8.mp3', []],
    [20, 'プライベイト', [8], 'fMGxBbLwY0M.mp3', []],
    [21, 'I my me mind', [8], 'howMD2iAXyw.mp3', []],
    [22, 'アイガッテ♡ランテ', [8], '6EPdwJIgQ.mp3', []],
    [23, '20xxMUEの光', [8], 'L23gOJFMnK8.mp3', []],
    [24, '透明できれい', [8], 'G4IeL2zq-jk.mp3', []],
    [25, 'はじめてのかくめい！2021', [8], 'bEsSAAcKQBA.mp3', [1]],
]

jsondata = {'discolist':[], 'Songs':[]}

for disco in discolist:
    discojson = {'id':disco[0], 'title':disco[1], 'name':disco[2], 'cover':[]}
    for img in disco[3]:
        discojson['cover'].append({'file':img})
    jsondata['discolist'].append(discojson)

for song in audiolist:
    songjson = {'id':song[0], 'name':song[1], 'discos':[], 'audio':song[3], 'must':[]}
    for disco in song[2]:
        songjson['discos'].append({'disco':disco})
    for no in song[4]:
        songjson['must'].append({'id':no})
    jsondata['Songs'].append(songjson)

with open('DataList.json', 'w', encoding='utf-8') as outfile:
    json.dump(jsondata, outfile, indent=4, ensure_ascii=False)