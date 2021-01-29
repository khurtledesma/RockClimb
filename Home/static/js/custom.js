/*route finder script */

$(function () {
        $('#citySubmit').click(function (e) {
            e.preventDefault() // stops the page from reloading 
            var userInput = $('#city').val(); //gathers search input 
            if (userInput === "") { //ensures fields are filled out
                alert("Please fill out all of the fields.");
            } else {
                mapUrl = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyCikhDfCw0_pf9qJHUW4GNwIi2x-Iau2P0&q=' + userInput + '',
                    $('#map').html(
                        '<iframe src="' + mapUrl + '" allowfullscreen> </iframe>'
                    )
                $.ajax({
                    url: 'http://api.openweathermap.org/data/2.5/weather?q=' + userInput + '&units=imperial&appid=319ce877549b8a92d0ca175e58407932',
                    dataType: 'json', //dataType
                    type: 'get', //getting JSON
                    cache: false,
                    success: function (data) {
                        
                        function timeConvert(x) {
                            var date = new Date(x * 1000);
                            var hours = date.getHours();
                            var minutes = "0" + date.getMinutes();
                            var seconds = "0" + date.getSeconds();
                            var formatTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
                            return formatTime 
                        }
                    
                        var timeNow = new Date();
                        timeNowHours = timeNow.getHours();
                        timeNowMinutes = timeNow.getMinutes();
                        var timeNowFormat = timeNowHours + ':' + timeNowMinutes
                    
                        var temp = data.main.temp
                        var description = data.weather[0].description
                        var wind = data.wind.speed
                        var sunriseUnix = data.sys.sunrise
                        var sunsetUnix = data.sys.sunset
                        var sunrise = timeConvert(sunriseUnix)
                        var sunset = timeConvert(sunsetUnix)
                        var weatherIcon = data.weather[0].icon
                       
                        $('#cityWeather').html(
                            '<h3>' + userInput + '</h3>'
                        )
                        $('#cityClimbs').html(
                            userInput
                        )
                        $('#cityTemperature').html(
                            '<h1>' + temp + ' ° F </h1>'
                        )
                        $('#cityDescription').html(
                           description
                        )
                        $('#cityWind').html(
                           wind + 'mph'
                        )
                        $('#sunRise').html(
                            'Sunrise:' + sunrise
                        )
                        $('#sunSet').html(
                            'Sunset:' + sunset
                        )
                        $('#weatherIcon').html(
                            '<img src="http://openweathermap.org/img/wn/' + weatherIcon + '.png "width="100px" height="100px" alt="Weather icon"> '
                        )
                        $('#currentTime').html(
                            timeNowFormat
                        )
                        $("#results").removeAttr("hidden");
                    }
                });
            }
        })
    })

/*My Climbs onclick toggler */
$(function () {        
    $(".climbListInfo").hide();
    $(".climbList").click(function () {
        $(this).children(".climbListInfo").toggle();
    });
}
);    