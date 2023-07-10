var questionAnswer;
var questionCode;
var isRegex = false;
var explanation = '';

function getParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');
    const answer = queryString.get('answer');
    const regex = queryString.get('isRegex');
    console.log(initCode);
    console.log(answer);
    console.log(regex);
    // Get the markdown code
    // const decodedCode = decodeURIComponent(initCode);
    questionCode = initCode;

    // Get the answer
    // const decodedAnswer = decodeURIComponent(answer);
    questionAnswer = answer;
    
    // Is the answer regex?
    // const decodedRegex = decodeURIComponent(regex);
    isRegex = (regex === "true");

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
    var converter = new window.showdown.Converter();
    var lines = markdown.split("\n");
    if(markdown.includes(">>>")) {
        newMarkdown = markdown.split(">>>")
        explanationMD = newMarkdown[1];
        markdown = newMarkdown[0];
        explanation = converter.makeHtml(explanationMD);
    }
    var html = converter.makeHtml(markdown);
    document.getElementById("Markdown").innerHTML = html;
}

var executed = false;
function createExplainer() {
    if(executed) {return;}
    else {
        executed = true;
        if(explanation == '' && isRegex==false){
            explanation = "The correct answer is " + questionAnswer
        } else if(explanation == '' && isRegex==true){
            explanation = "Correct answer must match the regular expression " + questionAnswer
        }
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

var body = document.body;
var observer = new MutationObserver(function(mutations) {
     parent.postMessage({
         height: document.documentElement.offsetHeight
     }, "*");
});

observer.observe(body, {
     childList: true,
     subtree: true
});

window.addEventListener('message', function(event) {
    var iframe = document.querySelector('iframe');
    if (typeof event.data === 'object' && event.data.height) {
        iframe.style.height = event.data.height + 'px';
    }
});

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

