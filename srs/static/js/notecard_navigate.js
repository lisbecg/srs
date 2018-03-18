/**
 * Ignore the old number of
 *
 * @type {number}: Counts the number of time this js is called.
 */
var COUNTER = 0;

/**
 * Detects if the pressed key is UP or DOWN.
 */
$(document).keydown(
    function(e)
    {
        if(COUNTER % 2 == 0) {
            // Ignore this INDEX's increment
        } else if (e.keyCode == 38 ) { //Up
            if( INDEX > TOP && TOP < MAX_TOP){
                TOP += 1;
                BOTTOM = TOP - 4;
                start = TOP - 5;
                // new_list = trim_list(notecards, start);
                new_list = trim_list(activateNotecards, start);
                load_notecards(new_list);
            }else if( INDEX < MAX_TOP) {
                $(".imageDiv:focus").prev().focus();
                INDEX++;
            }
        } else if (e.keyCode == 40) { //Down
            if( INDEX < BOTTOM && BOTTOM > 1){
                BOTTOM -= 1;
                TOP = BOTTOM + 4 ;
                start = TOP - 5;
                // new_list = trim_list(notecards, start);
                new_list = trim_list(activateNotecards, start);
                load_notecards(new_list);
            }else if( INDEX > 1){
                $(".imageDiv:focus").next().focus();
                INDEX--;
            }
        }

        COUNTER++;
    }
);

/**
 * Changes the default position to one.
* */
$(document).ready(function() {
    if(document.getElementById('bottomDiv1')) {
        document.getElementById('bottomDiv1').focus();
        // load_notecards(notecards);
        load_notecards(activateNotecards);
    }
}
);

/**
 * Loads from all the notecards those that want to be represented in the view.
 *
 * @param notecards: Array of notecards.
 */
// function load_notecards(notecards){
function load_notecards(activateNotecards){
    // MAX_DISPLAY = ((notecards.length > 5 )? 5 : notecards.length);
    MAX_DISPLAY = ((activateNotecards.length > 5 )? 5 : activateNotecards.length);
    EMPTY_DISPLAY = 5 - MAX_DISPLAY;
    for(var i = 0; i < MAX_DISPLAY; i++) {
        var id =  'bottomDiv'+ (i+1);
        // document.getElementById(id).innerHTML = notecards[i].fields.name + "<br>" + notecards[i].fields.body;
        // document.getElementById(id).href = 'http://'+window.location.host+'/srs/notecard/'+notecards[i].pk+'/';
        // keywords_ = notecards[i].fields.keywords.split("$$");
        document.getElementById(id).innerHTML = activateNotecards[i].fields.name + "<br>" + activateNotecards[i].fields.body;
        document.getElementById(id).href = 'http://'+window.location.host+'/srs/notecard/'+activateNotecards[i].pk+'/';
        keywords_ = activateNotecards[i].fields.keywords.split("$$");
        for (var j = 0; j < keywords_.length; j++) {
            document.getElementById(id).title += " " + keywords_[j];
        }
    }

    for(var i = MAX_DISPLAY ; i < 5; i++) {
        var id =  'bottomDiv'+ (i+1);
        document.getElementById(id).innerHTML = "";
        document.getElementById(id).href = "";
        document.getElementById(id).title = "";
        document.getElementById(id).removeAttribute("innerHTML");
        document.getElementById(id).removeAttribute("href");
        document.getElementById(id).removeAttribute("title");
    }
}

/**
 * Fills array with five notecards to be displayed.
 *
 * @param notecards: Array of notecards.
 * @param index: Starting index for taking the notecards.
 *
 * @returns {Array}: Array with the five notecards to be displayed.
 */
// function trim_list(notecards, index){
function trim_list(activateNotecards, index){
    new_list = [];
    var end = index + 5;
    for(index; index < end && index < activateNotecards.length; index++){
        new_list.push(activateNotecards[index]);
    }
    return new_list;
}
