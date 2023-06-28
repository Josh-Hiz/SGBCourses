var questionAnswer;
var questionCode;
var isRegex;
var explanation = '';

function getParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');
    const answer = queryString.get('answer');
    const regex = queryString.get('isRegex');

    // Get the markdown code
    const decodedCode = decodeURIComponent(initCode);
    questionCode = decodedCode;

    // Get the answer
    const decodedAnswer = decodeURIComponent(answer);
    questionAnswer = decodedAnswer;
    
    // Is the answer regex?
    const decodedRegex = decodeURIComponent(regex);
    isRegex = (decodedRegex === "true");

    parseMarkdown(questionCode);
}

// Check answer should grab the value thats in the input box on the form and 
// parse it for regular expressions and then check if questionAnswer = userAnswer 
// to return true or false
function checkAnswer(){
    let userAnswer = document.getElementById("userAnswer").value;

    if (isRegex){        
        // Turn questionAnswer into a regular expression
        const re = new RegExp(questionAnswer);
        console.log(questionAnswer);
        console.log(re);
        if (re.test(userAnswer)){
            console.log("Regular expression matches")
            return true;
        } else {
            console.log("Regular expression does not match")
            return false;
        }
    } else { 
        if (userAnswer == questionAnswer){
            return true;
        } else {
            return false;
        }
    }
}

function parseMarkdown(markdown) {
    if(markdown.includes(">>>")) {
        newMarkdown = markdown.split(">>>")
        explanation = newMarkdown[1];
        markdown = newMarkdown[0];
    }
    var converter = new window.showdown.Converter();
    var html = converter.makeHtml(markdown);
    explanation = converter.makeHtml(explanation);
    document.getElementById("Markdown").innerHTML = html;
}

var executed = false;
function createExplainer() {
    if(executed) {return;}
    else {
        executed = true;
        const explainButton = document.createElement("button");
        explainButton.setAttribute("type", "explain");
        explainButton.innerText = "Explain";
        explainButton.addEventListener("click", function(event) {
            event.preventDefault();
            document.getElementById("result").innerHTML = `
            <div class="alert alert-info">
                ${explanation}
            </div>
            `;
        });
        document.forms[0].appendChild(explainButton);
    }
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
            createExplainer();
        }
    });
}

getParams();
document.addEventListener("DOMContentLoaded", setUpEventListener);

