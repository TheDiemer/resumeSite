function playAudio(url) {
        var a = new Audio(url);
        a.play();
}
$(document).ready(function() {
    //check if this is user's first time on page
    if(!getCookie('Theme')){
        console.log("Should only ever run once");
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            currentTheme = "dark";
        } else {
            currentTheme = "light";
        }
    } else {
        currentTheme = getCookie('Theme');
    }
    setTheme(currentTheme);
});

var setTheme = function (theme) {
        if (theme == 'dark') {
		// dark
		$( "body" ).removeClass("standard");
		$( "body" ).addClass( "dark" );
		$(".inner-switch").text("Light");
		setCookie('Theme', 'dark', 30);
	} else {
	        $("body").removeClass("dark");
                $("body").addClass("standard");
		$(".inner-switch").text("Dark");
		setCookie('Theme', 'standard', 30);
	}
};

currentTheme = getCookie('Theme');
setTheme(currentTheme);

$( ".inner-switch" ).on("click", function() {
        if ($("body").hasClass("dark")) {
                // standard
                setTheme('standard');
        } else {
                // dark mode
                setTheme('dark');
        }
});
function getCookie(name) {
        var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return v ? v[2] : null;
}

function setCookie(name, value, days) {
        var d = new Date;
        d.setTime(d.getTime() + 24 * 60 * 60 * 1000 * days);
        document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}

function deleteCookie(name) { setCookie(name, '', -1); }

//$( ".inner-switch" ).on("click", function(){
//    if( $( "body" ).hasClass( "dark" )) {
//      $( "body" ).removeClass( "dark" );
//      $( ".inner-switch" ).text( "Dark Mode OFF" );
//    } else {
//      $( "body" ).addClass( "dark" );
//      $( ".inner-switch" ).text( "Dark Mode ON" );
//    }
//});
