(function() {
    var epaAPI = "http://opendata.epa.gov.tw/ws/Data/UV/?$orderby=PublishAgency&$skip=0&$top=1000&format=json&callback=?";
    $.getJSON( epaAPI, function(){
      format: "json"
    }).done(function(data) {
          console.log(data);
      });
  })();