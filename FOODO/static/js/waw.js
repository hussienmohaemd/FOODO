jQuery(document).ready(function() {
  jQuery("#menu").click(function () {
    jQuery("nav").slideToggle(400, function () {
      jQuery(this).toggleClass("nav-expanded").css('display', '');
    });
  });
});

jQuery(document).ready(function() {
  jQuery("#close").click(function () {
    jQuery("nav").slideToggle(400, function () {
      jQuery(this).toggleClass("nav-expanded").css('display', '');
    });
  });
});

var menu = document.getElementById("menu");
var close = document.getElementById("close");

menu.addEventListener('click', showClose);

function showClose () {
   var menu = document.getElementById("menu");
   var close = document.getElementById("close");
   menu.style.display = "none";
   close.style.display = "block";
}


close.addEventListener('click', showMenu);

function showMenu () {
   var menu = document.getElementById("menu");
   var close = document.getElementById("close");
   menu.style.display = "block";
   close.style.display = "none";
}

