// select all divs, give them a purple background
$("div").css("background", "purple");

// select all divs w class highlight make them 200px wide
$("div .highlight").css("width", "200px");

// select div w id third, give it orange border
// didnt work
$("div #third").css("border", "1px solid orange");
// does work
$("#third").css("border", "1px solid orange");

// bunus - select 1st div, change font to pink
// didnt work
$("div[0]").css("fontColor", "pink")
// use css psuedo-selector first-of-type
// there is no fontColor; use fontSize when saving to js obj
$("div:first-of-type").css("color", "pink")

// theres also a built in jQuery shortcut. 
// is slower tho, not built into css
$("div:first").css("color", "pink")