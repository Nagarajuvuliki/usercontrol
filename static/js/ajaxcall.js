$('#selectorg').on('change', function(e){
    e.preventDefault();
    $.ajax({
        type : "POST",
        url: "dashboard",
        data: {
        form:"org_form",
        org_name:$('#selectorg').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        // csrfmiddlewaretoken: '{{ csrf_token }}',

        dataType: "json",
        },
        success: function(data){
            console.log(data.msg)
            $('#org_msg').text(data.msg);
            setTimeout(function(){
                window.location.replace("dashboard");
            },1000); 
        
        },

        failure: function() {
        $('#org_msg').html(data.msg)
        }});});
        console.log("{{request.session.username}}")
$('#levels_btn').on('click', function(e){
e.preventDefault();
$.ajax({
    type : "POST",
    url: "levels",
    data: {
    form:"getlevels",
    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    // csrfmiddlewaretoken: '{{ csrf_token }}',

    dataType: "json",
    },
    beforeSend: function() {
        $('#ringcontainer').css("display", "block");
    },
    success: function(data){
        $('#ringcontainer').css("display", "none");
        $("#form-field-level1name").val(data.level1.name)
        console.log(data.level1.name)
    
    },

    failure: function() {
    $('#org_msg').html(data.msg)
    }});});
    console.log("{{request.session.username}}")