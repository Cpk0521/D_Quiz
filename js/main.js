var dir_audio = './audio'
var dir_image = './image'

var discolist;
var songlist;
var Q;
var audio_player;

$.getJSON("json/DataList.json", function(data) {
    discolist = data['discolist'];
    songlist = data['Songs'];
})

class Quiz {
    constructor(){
        this.questionlog = []
        this.curr = 0
        this.correct = 0;
    }

    createquiz() {

        this.questionlog = [];
        let special = [];

        songlist.forEach(element => {
            
            if(element.must.length > 0){
                special.push(element);
            }else{
                let question = {};

                question.correct = element.name;
                question.audio = element.audio;
                question.disco = element.discos;

                question.answers = [];
                question.answers.push(element.name);

                while (question.answers.length < 4) {
                    let randomsong = songlist[Math.floor(Math.random() * songlist.length)].name;
                    if ($.inArray(randomsong, question.answers) == -1) {
                        question.answers.push(randomsong);
                    }
                }

                question.answers.sort(() => Math.random() - 0.5);

                this.questionlog.push(question)
            }

        });

        this.questionlog.sort(() => Math.random() - 0.5);

        do {

            let rand_id = Math.floor(Math.random() * special.length)
            let rand_special = special[rand_id];
            let question = {};

            question.correct = rand_special.name;
            question.audio = rand_special.audio;
            question.disco = rand_special.discos;

            question.answers = [];
            question.answers.push(rand_special.name);

            let del_list = [];

            if(rand_special.must.length > 4){

                while (question.answers.length < 4) {
                    let rand_must_id = Math.floor(Math.random() * rand_special.must.length);
                    let rand_song_id = rand_special.must[rand_must_id].id;
                    let randomsong = songlist[rand_song_id-1].name;

                    if ($.inArray(randomsong, question.answers) == -1) {
                        question.answers.push(randomsong);
                    }
                }
    
            }else if(rand_special.must.length <= 4){

                rand_special.must.forEach(e =>{
                    let song = songlist[e.id-1].name;
                    question.answers.push(song);
                })

                while (question.answers.length < 4) {
                    let randomsong = songlist[Math.floor(Math.random() * songlist.length)].name;
                    if ($.inArray(randomsong, question.answers) == -1) {
                        question.answers.push(randomsong);
                    }
                }
            }

            question.answers.sort(() => Math.random() - 0.5);
            
            this.questionlog.push(question);

            special.splice(rand_id, 1);

            del_list = rand_special.must;
            console.log(del_list);

            for (let i = 0; i < special.length; i++) {
                for (let ii = 0; ii < del_list.length; ii++) {

                    if(special[i].id == del_list[ii].id){
                        special.splice(i, 1);
                    }
                }
            }

        } while (special.length > 0) 

    }

    getCurr(){
        return this.questionlog[this.curr];
    }

    checkAns(choose){
        if(this.questionlog[this.curr].correct == choose){
            this.correct ++;
        }

        return this.questionlog[this.curr].correct == choose;
    }

    nextQ(){
        if(this.curr < this.questionlog.length)
            this.curr ++;

        return this.curr < this.questionlog.length
    }

    getResult(){

        let percentage = Math.floor(this.correct/this.questionlog.length * 100);

        let ranking;
        if (percentage == 0) {
            //F
            ranking = 'F';
        }else if(percentage > 0 && percentage < 25){
            //E
            ranking = 'E';
        }else if(percentage >= 25 && percentage < 50){
            //D
            ranking = 'D';
        }else if(percentage >= 50 && percentage< 75){
            //C
            ranking = 'C';
        }else if(percentage >=75 && percentage < 90){
            //B
            ranking = 'B';
        }else if(percentage >= 90 && percentage < 100){
            //A
            ranking = 'A';
        }else if(percentage == 100){
            //S
            ranking = 'S';
        }

        return {'totals':this.questionlog.length, 'correct':this.correct, 'percentage':percentage, 'ranking':ranking};
    }

}


function loadquestion(){

    let questions = Q.getCurr();
    $('#questionbox').removeClass('d-none').addClass('d-block');

    for (let index = 0; index < questions.answers.length; index++) {
        $('#anwers>div>.choosebtn>span').eq(index).text(questions.answers[index]);
    }


    $('#soundbtn').addClass('lock');
    audio_player = new Howl({
        src: [`${dir_audio}/${questions.audio}`],
        html5: true,
        onload: ()=>{

            // audio_player._sprite.randomclip = [0, 1700];

            let offset = Math.floor(Math.random() * (audio_player._duration - 10));
            audio_player._sprite.randomclip = [offset*1000, 20000];

            audio_player.play('randomclip');
            $('#soundbtn').removeClass('lock');
        },
        onplay: ()=>{
            $('#soundbtn>i').removeClass('fa-play').addClass('fa-pause');
        },
        onpause: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onstop: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        },
        onend: ()=>{
            $('#soundbtn>i').removeClass('fa-pause').addClass('fa-play');
        }
    })

    $('#disco').html('');
    $('#anwer_name').children('span').removeClass('text-Success').removeClass('text-Danger').html(questions.correct);

    questions.disco.forEach(e => {

        let data = discolist.find(ele => ele.id == e.disco);

        let p = `<div class="p-3 text-center">
                    <img class='discoimg' src="${dir_image}/disco/${data.cover[0].file}">
                    <p class="font-style m-1" style="font-size: xx-small;">${data.title}</p>
                    <p class="font-style m-1 fw-bold">${data.name}</p>
                </div>`;

        $('#disco').append(p);
    })
}  

function ShowResult(){

    $('#quiz').addClass('d-none');
    $('#result').removeClass('d-none');
    $('#result').fadeIn('slow');

    result = Q.getResult();
    
    $('#q_t').text(result.totals);
    $('#q_c').text(result.correct).addClass('text-Danger');

    $('#rankimg').attr('src', `./image/ranking/ClassIconL_${result.ranking}.png`);
    
    $('a.twitter.sp-btn').attr('href', `https://twitter.com/intent/tweet?text=ダイアローグ楽曲検定！%0a全${result.totals}問中${result.correct}問正解！%0a&hashtags=ダイアローグ,ダイアローグ楽曲檢定&url=https://cpk0521.github.io/D_Quiz/%0a`)
}


$('#start-btn').click(()=>{
    
    Q = new Quiz();
    Q.createquiz();
    $('#menu').addClass('d-none');

    $('#quiz').removeClass('d-none').addClass('d-block');
    loadquestion();
})

$('#anwers>div>div.choosebtn').click(function(){
    $('div.choosebtn').removeClass('is-selected');
    $(this).addClass('is-selected');
    $('#questionbox>div>#confirm-btn').removeClass('choosing').addClass('selecting');

})

$('#confirm-btn').click(function(){
    $(this).removeClass('selecting').addClass('choosing');
    $('#questionbox').removeClass('d-block').addClass('d-none');

    let ans = $('.choosebtn.is-selected').children('span').text();
    $('div.choosebtn').removeClass('is-selected');

    audio_player.stop();
    audio_player.unload();
    audio_player = null;

    if (Q.checkAns(ans)){
        $('#anwer_name').children('span').addClass('text-Success');
    }else{
        $('#anwer_name').children('span').addClass('text-Danger');
    }

    $('#checkanwer').removeClass('d-none').addClass('d-block');
})


$('#checkanwer>div>#next-btn').click(function(){

    $('#checkanwer').removeClass('d-block').addClass('d-none');

    if(Q.nextQ()){
        loadquestion();
    }else{
        ShowResult();
    }

})

$('.continue.sp-btn').click(()=>{
    location.reload();
})

$('#soundbtn').click(()=>{
    if (audio_player.playing()) {
        audio_player.stop();
    } else {
        audio_player.play('randomclip');
    }
})