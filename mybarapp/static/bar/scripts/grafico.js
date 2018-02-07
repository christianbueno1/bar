var v = [8,3];
d3.select("div.chart")
.selectAll("div").data(v).enter().append("div")
.text(  function(d,i) { return d; }     )
.attr("style", function(d,i) { return "width: "+d*10+"px;"; } );