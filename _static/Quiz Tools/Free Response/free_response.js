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
    const radios = document.querySelectorAll('input[type=radio]');
    for(let i = 0; i < radios.length; i++) {
        if(radios[i].checked) {
            if(choices[radios[i].id] == true) {
                return true;
            }
        }
    }
    return false;
}

function parseMarkdown(markdown) {
    var converter = new window.showdown.Converter();
    var lines = markdown.split("\n");
    var justQuestions = lines.filter((line) => line.startsWith("- [ ]") || line.startsWith("- [x]") || line.startsWith("1. [ ]") || line.startsWith("1. [x]"));

    if(justQuestions.length > 0){
        for (let i = 0; i < justQuestions.length; i++) {
            var id = "choice" + i;
            var answer = justQuestions[i].slice(7);
            var isAnswer = justQuestions[i].startsWith("- [x]") || justQuestions[i].startsWith("1. [x]");
            choices[id] = isAnswer;
            var html = `<br><input type="radio" id="${id}" name="question">
                        <label for="${id}">${answer}</label></br>`;
            document.getElementById("Markdown").innerHTML += html;
        }
        document.getElementById("Markdown").innerHTML += '<br><button type="submit" id="submit">Submit Answer</button><p id="result"></p>';
    }
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

