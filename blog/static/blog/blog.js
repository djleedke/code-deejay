
/*---------- Navbar ---------*/
var overlay = false;

function toggleNav(){
    if(overlay) {
        document.getElementById("overlay").style.height = "0";
        document.getElementById("overlay").style.maxheight = "0%";
        overlay = false;
    } else {
        document.getElementById("overlay").style.height = "auto";
        document.getElementById("overlay").style.maxHeight = "1000px";
        overlay = true;
    }
}

/*---------- Admin Bar ---------*/

var editMode = false;

//Allows us to edit posts from their detail page rather than the admin site
$('#edit-post-detail').on('click', function(){

    if(editMode === false){
        $(this).text('Save');
        $('.post-detail-content').attr('contenteditable', 'true');

        //AJAX to get raw post content and place it in the div
        $.ajax({
            url: '/ajax/get-post-content',
            data: {
                'post-id': $('.post-detail-content').data('post-id')
            },
            dataType: 'json',
            success: function(data){
                //Adding <pre> tags to it as it is formatted in the database
                $('.post-detail-content').wrap('<pre class="editing">');
                $('.post-detail-content').text(data.content)
                editMode = true;
            }
        });
    } else {
        $(this).text('Edit');
        //AJAX to save new raw post content and then return it for the page
        $.ajax({
            url: '/ajax/update-post-content',
            data: {
                'post-id': $('.post-detail-content').data('post-id'),
                'content': $('.post-detail-content').text()
            },
            dataType: 'json',
            success: function(data){
                console.log('hey');
                $('.post-detail-content').attr('contenteditable', 'false');
                $('.post-detail-content').unwrap();
                $('.post-detail-content').html(($('.post-detail-content').text()));
                editMode = false;
            }
        });
    }
});