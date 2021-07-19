$(document).ready(function(){
    $("#insert-more").click(function () {
         $("#mytable").each(function () {
             var tds = '<tr>';
             console.log("in side my talble")
             jQuery.each($('tr:last td', this), function () {
                 tds += '<td>' + $(this).html() + '</td>';
             });
             tds += '</tr>';
             if ($('tbody', this).length > 0) {
                 $('tbody', this).append(tds);
             } else {
                 $(this).append(tds);
             }
         });
    });
});

$(document).ready(function(){
    $("#removebutton").click(function() {
            console.log("inside delete function")
        $("#r1").remove();
    });
});

function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah')
                    .attr('src', e.target.result)
                    .width(150)
                    .height(200);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

$('#student_form').on('submit', function(){
    var that = $(this),
        url = that.attr('action'),
        method = that.attr('method'),
        data = {}

    that.find('[name]').each(function(index, value){
        var that = $(this),
            name = that.attr('name'),
            value = that.val();

            data[name]=value;
    });
    $.ajax({
        url:url,
        type:type,
        data:data,
        success:function(response){
            console.log(response);
        }

    });
    return false;
});