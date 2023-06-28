var questionAnswer;
var questionCode;
var isRegex;

function getParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');
    const answer = queryString.get('answer');
    const regex = queryString.get('isRegex');

    // Get the markdown code
    const decodedCode = decodeURIComponent(initCode);
    questionCode = decodedCode;
    console.log(questionCode);

    // Get the answer
    const decodedAnswer = decodeURIComponent(answer);
    questionAnswer = decodedAnswer;
    console.log(questionAnswer);
    
    // Is the answer regex?
    const decodedRegex = decodeURIComponent(regex);
    isRegex = (decodedRegex === "true");
    console.log(isRegex);
    console.log(typeof(isRegex));

    parseMarkdown(questionCode);
}

// Check answer should grab the value thats in the input box on the form and 
// parse it for regular expressions and then check if questionAnswer = userAnswer 
// to return true or false
function checkAnswer(){
    let userAnswer = document.getElementById("userAnswer").value;

    if (isRegex){        
        questionAnswer = new RegExp(questionAnswer);
        console.log(questionAnswer);
        if (questionAnswer.test(userAnswer)){
            console.log("Regular expression matches")
            return true;
        } else {
            console.log("Regular expression does not match")
            return false;
        }
    } else { 
        if (userAnswer == questionAnswer){
            console.log("Answer matches")
            return true;
        } else {
            console.log("Answer does not match")
            return false;
        }
    }
}

function parseMarkdown(markdown) {
    var converter = new window.showdown.Converter();
    var html = converter.makeHtml(markdown);
    document.getElementById("Markdown").innerHTML = html;
}

function setUpEventListener() {
    document.getElementById("submit").addEventListener("click", function(event) {
        event.preventDefault(); // Add this line to prevent default form submission behavior
        if (checkAnswer()) {
            document.getElementById("result").innerHTML = `
            <div class="alert alert-success">
                <strong>Correct!</strong><br>
            </div>
            `;
        } else {
            document.getElementById("result").innerHTML = `
            <div class="alert alert-danger">
                <strong>Sorry, incorrect answer.</strong>
            </div>
            `;
        }
    });
}

getParams();
document.addEventListener("DOMContentLoaded", setUpEventListener);

