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