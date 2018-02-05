function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}



function prueba(){

  var texto_entrada = $('.message-input').val();
  var params = { "texto_entrada" : texto_entrada};
  $.ajax({
    url: '/obtenersalida',
    type: 'post', 
    data : params,       
            success: function (response) {
            mm=response;
             // alert('Datos Exitosamente Enviados');
              //$("#resultado").html(response);  
              }          
                       
              
          });}



function insertMessage() {
  msg = $('.message-input').val();
  //alert("mensaje"+msg);
  prueba();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})

var botsn = [
  'Lic. Juan Gutierritos',
  'Srita. Ma. del Rocio',
  'Mr. Anderson',
  'Sr. Juan Martin Carrera',
  'Lic. Rubalcaba R.',
  'Sr. Persie Vandor',  
  'Ing. Francois Valderramaz',
  'Seiya Perez',
  'Saga de Geminis',
  'Srita. Priscila D.',
  'Prof. Hernandez Mon.'  
];


var Fake = [
  'Estas en el chat de mesa de ayuda, ¿Como te llamas?',
  'Hola, Bienvenido a mesa de ayuda ¿Cual es tu nombre?',
  'Hola, ¿en que te puedo ayudar?',
  'Bienvenido, ¿en que podemos servirte?',
  'Que tal?, Como estas?',
  'Hola, estoy a tus ordenes... ¿Cual es tu nombre?' 
];

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
var mm=Fake[getRandomInt(0,Fake.length)];
//mm=rand(Fake.length);

$('#bname').text(botsn[getRandomInt(0,botsn.length)]);



function fakeMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  $('<div class="message loading new"><figure class="avatar"><img src="https://www.file-extensions.org/imgs/app-icon/128/8360/ripple-chat-bot.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();

  setTimeout(function() {
    $('.message.loading').remove();
    $('<div class="message new"><figure class="avatar"><img src="https://www.file-extensions.org/imgs/app-icon/128/8360/ripple-chat-bot.png" /></figure>' + mm + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
    i++;
  }, 1000 + (Math.random() * 20) * 100);



}
