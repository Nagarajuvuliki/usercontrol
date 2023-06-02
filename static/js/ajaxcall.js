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
        $("#form-field-level2name").val(data.level2.name)
        $("#form-field-level3name").val(data.level3.name)
        $("#form-field-level4name").val(data.level4.name)
        $("#form-field-level5name").val(data.level5.name)
        console.log(data.level1.name)
    
    },

    failure: function() {
    $('#org_msg').html(data.msg)
    }});});
    console.log("{{request.session.username}}")