/*
function that shows the user message in the chatbox

*/
function addUserMessage(message){
    var element = document.getElementById("conversation");
    var messageBox = document.createElement("div");
    messageBox.setAttribute("id", "usermessage");

    var text = document.createTextNode(message);
    messageBox.appendChild(text);
    element.appendChild(messageBox);
}

/*
function that shows the bot response in the chatbox

*/
function addBotMessage(message){
    var element = document.getElementById("conversation");
    var messageBox = document.createElement("div");
    messageBox.setAttribute("id", "botmessage");

    var text = document.createTextNode(message);
    messageBox.appendChild(text);
    element.appendChild(messageBox);
}

/*
function that display the map next to the chatbox of the location asked by the user

*/
function changeUrlMap(url){
    document.getElementById("dynamicmap").src = url;
}

/*
function that add space between user and bot messages

*/
function addWhiteLines(){
    var element = document.getElementById("conversation");
    var whiteLines = document.createElement("br");
    element.appendChild(whiteLines);
}

/*
function that displays the spinner when the bot is thinking

*/
function addLoader(){
    var element = document.getElementById("conversation");
    var loader = document.createElement("div");
    loader.setAttribute("id", "loader");
    element.appendChild(loader);

}

/*
function that removes the spinner once the answer is ready

*/
function removeLoader(){
    var element = document.getElementById("loader");
    return element.parentNode.removeChild(element);
}

/*
Send the user message to the back end and retrieves it answers to the front

*/
document.getElementById("userentrybutton").addEventListener("click", function(){
    var userentry = $("#usertext").val();
    addUserMessage(userentry);
    addLoader();


    $.ajax({
        data:{
            query:userentry
        },
        type:"POST",
        url:"/process",
        success:function(response){
            removeLoader();
            addWhiteLines();
            changeUrlMap(response["url"]);
            addBotMessage(response["summary"]);
        }
    });
}, false);