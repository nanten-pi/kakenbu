let score = 0;

function showScore(){
    const totalScore = document.getElementById('score-message');
    if(score === 5) {
        totalScore.innerHTML = score + "点：さすが"
    } else if(score === 4) {
        totalScore.innerHTML = score + "点：もう一息";

    } else if(score === 3) {
        totalScore.innerHTML = score + "点：やりますねぇ";

    } else if(score === 2) {
        totalScore.innerHTML = score + "点:頑張れ";

    } else if(score === 1) {
        totalScore.innerHTML = score + "点:ﾄﾞﾝ( ﾟдﾟ)ﾏｲ";
        
    } else {
        totalScore.innerHTML = score + "点：無効な回答ですページを再読み込みしてください";

    }
}
const correct = '正解です';
const incorrect = '不正解です';

function answerQuiz1() {
    const quiz_1 = document.getElementById('quiz-1');
    const select = '1問目：' + quiz_1.answer.value + 'を選択しました';
    if (quiz_1.answer.value == 'a') {
        score++;
        console.log(select);
        console.log(correct);
    } else if (quiz_1.answer.value == 'b') {
        console.log(select);
        console.log(incorrect);
    } else if (quiz_1.answer.value == 'c') {
        console.log(select);
        console.log(incorrect);
    } else {
        alert('1問目の答えを入力してください');
    }
}

function answerQuiz2(){
    const quiz_2 = document.getElementById('quiz-2');
    const select = '2問目：' + quiz_2.answer.value + 'を選択しました';

    if (quiz_2.answer.value == 'a') {
        console.log(select);
        console.log(incorrect);
    } else if (quiz_2.answer.value == 'b') {
        score++;
        console.log(select);
        console.log(correct);
    } else if (quiz_2.answer.value == 'c') {
        console.log(select);
        console.log(incorrect);
    } else {
        alert('2問目の答えを入力してください');
    }
}

function answerQuiz3(){
    const quiz_3 = document.getElementById('quiz-3');
    const select = '3問目：' + quiz_3.answer.value + 'を選択しました';

    if (quiz_3.answer.value == 'a') {
        console.log(select);
        console.log(incorrect);
    } else if (quiz_3.answer.value == 'b') {
        console.log(select);
        console.log(incorrect);
    } else if (quiz_3.answer.value == 'c') {
        score++;
        console.log(select);
        console.log(correct);
    } else {
        alert('3問目の答えを入力してください');
    }
}

function answerQuiz4(){
    const quiz_4 = document.getElementById('quiz-4');
    const select = '4問目：' + quiz_4.answer.value + 'を選択しました';

    if (quiz_4.answer.value == 'a') {
        score++;
        console.log(select);
        console.log(correct);
    } else if (quiz_4.answer.value == 'b') {
        console.log(select);
        console.log(incorrect);

    } else if (quiz_4.answer.value == 'c') {
        console.log(select);
        console.log(incorrect);
    } else {
        alert('4問目の答えを入力してください');
    }
}

function answerQuiz5(){
    const quiz_5 = document.getElementById('quiz-5');
    const select = '5問目：' + quiz_5.answer.value + 'を選択しました';

    if (quiz_5.answer.value == 'a') {
        score++;
        console.log(select);
        console.log(correct);
    } else if (quiz_5.answer.value == 'b') {
        score++;
        console.log(select);
        console.log(correct);
    } else if (quiz_5.answer.value == 'c') {
        score++;
        console.log(select);
        console.log(correct);
    } else {
        alert('5問目の答えを入力してください');
    }
}
setInterval(function(){
  document.oncontextmenu = function () {return false;}
}, 100);
document.getElementsByTagName('html')[0].oncontextmenu = function () {return false;}
document.body.oncontextmenu = function () {return false;}
