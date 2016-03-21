data = [["Alabama", 60],
["Alaska", 20],
["American Samoa", 11],
["Arizona", 85],
["Arkansas", 37],
["California", 548],
["Colorado", 78],
["Connecticut", 71],
["Delaware", 31],
["Democrats Abroad", 17],
["District of Columbia", 46],
["Florida", 246],
["Georgia", 117],
["Guam", 12],
["Hawaii", 35],
["Idaho", 27],
["Illinois", 182],
["Indiana", 92],
["Iowa", 52],
["Kansas", 37],
["Kentucky", 60],
["Louisiana", 59],
["Maine", 30],
["Maryland", 118],
["Massachusetts", 116],
["Michigan", 147],
["Minnesota", 93],
["Mississippi", 41],
["Missouri", 84],
["Montana", 27],
["Nebraska", 30],
["Nevada", 43],
["New Hampshire", 32],
["New Jersey", 142],
["New Mexico", 43],
["New York", 291],
["North Carolina", 121],
["North Dakota", 23],
["Northern Marianas", 11],
["Ohio", 160],
["Oklahoma", 42],
["Oregon", 74],
["Pennsylvania", 210],
["Puerto Rico", 67],
["Rhode Island", 33],
["South Carolina", 59],
["South Dakota", 25],
["Tennessee", 75],
["Texas", 251],
["Unassigned", 1],
["Utah", 37],
["Vermont", 26],
["Virgin Islands", 12],
["Virginia", 109],
["Washington", 118],
["West Virginia", 37],
["Wisconsin", 96],
["Wyoming", 18]]

occurred = ["Iowa","New Hampshire","Nevada","South Carolina","Alabama","Arkansas","Colorado","Georgia","Massachusetts","Minnesota","Oklahoma","Tennessee","Texas","Vermont","Virginia","American Samoa","Kansas","Louisiana","Nebraska","Maine","Michigan","Mississippi","Northern Marianas","Florida","Illinois","Missouri","North Carolina","Ohio"]

var setup = d3.select(".chart")
    .data(data)
    .enter()
    .append("div")
    .style("width", function(d) { return d[1] * 2.5 + "px"; })
    .style("background-color", function(d) {
	if(occurred.indexOf(d[0]) != -1){
	    return "cyan";
	}else{
	    return "blue";
	}
    })
    .style("color", function(d) {
	if(occurred.indexOf(d[0]) != -1){
	    return "black";
	}else{
	    return "lightsteelblue";
	}
    })
    .style("margin","1px")
    .style("padding","1px")
    .text(function(d) { return d[0] + ": "+ d[1]; });
