function addUserMessage(message){
    var element = document.getElementById("conversation");
    var messageBox = document.createElement("div");
    messageBox.setAttribute("id", "usermessage");

    var text = document.createTextNode(message);
    messageBox.appendChild(text);
    element.appendChild(messageBox);
}

function addBotMessage(message){
    var element = document.getElementById("conversation");
    var messageBox = document.createElement("div");
    messageBox.setAttribute("id", "botmessage");

    var text = document.createTextNode(message);
    messageBox.appendChild(text);
    element.appendChild(messageBox);
}

function changeUrlMap(url){
    document.getElementById("dynamicmap").src = url;
}

function addWhiteLines(){
    var element = document.getElementById("conversation");
    var whiteLines = document.createElement("br");
    element.appendChild(whiteLines);
}

function addLoader(){
    var element = document.getElementById("conversation");
    var loader = document.createElement("div");
    loader.setAttribute("id", "loader");
    element.appendChild(loader);

}

function removeLoader(){
    var element = document.getElementById("loader");
    return element.parentNode.removeChild(element);
}

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