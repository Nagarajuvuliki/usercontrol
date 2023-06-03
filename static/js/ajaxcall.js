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
        
//levels start
//fetching data from levels
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
    
//change level1 name
$("#level1name").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.
    
    $.ajax({
        type: "POST",
        url: "levels",
        data: {
            form:"levelnames",
            level:"level1",
            level_name:$('#form-field-level1name').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        
            dataType: "json",
            },
            beforeSend: function() {
                $('#ringcontainer1').css("display", "block");
            },
            success: function(data){
                $('#ringcontainer1').css("display", "none");
        
                $('#form-field-level1name').val(data.name)
                $('#msglevel1').text(data.msg);
        }
    });
    
});
//change level2 name
$("#level2name").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: "levels",
        data: {
            form:"levelnames",
            level:"level2",
            level_name:$('#form-field-level2name').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        
            dataType: "json",
            },
            beforeSend: function() {
                $('#ringcontainer1').css("display", "block");
            },
            success: function(data){
                $('#ringcontainer1').css("display", "none");
                $('#form-field-level2name').val(data.name)
                $('#msglevel2').text(data.msg);
        }
    });
    
});
//change level3 name
$("#level3name").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: "levels",
        data: {
            form:"levelnames",
            level:"level3",
            level_name:$('#form-field-level3name').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        
            dataType: "json",
            }, // serializes the form's elements.
            beforeSend: function() {
                $('#ringcontainer1').css("display", "block");
            },
            success: function(data){
                $('#ringcontainer1').css("display", "none");
                $('#form-field-level3name').val(data.name)
                $('#msglevel3').text(data.msg);
        }
    });
    
});
//change level4 name
$("#level4name").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: "levels",
        data: {
            form:"levelnames",
            level:"level4",
            level_name:$('#form-field-level4name').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        
            dataType: "json",
            },
            beforeSend: function() {
                $('#ringcontainer1').css("display", "block");
            },
            success: function(data){
                $('#ringcontainer1').css("display", "none");
                $('#form-field-level4name').val(data.name)
                $('#msglevel4').text(data.msg);
        }
    });
    
});
//change level5 name
$("#level5name").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: "levels",
        data: {
            form:"levelnames",
            level:"level5",
            level_name:$('#form-field-level5name').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        
            dataType: "json",
            },
            beforeSend: function() {
                $('#ringcontainer1').css("display", "block");
            },
            success: function(data){
                $('#ringcontainer1').css("display", "none");
                $('#form-field-level5name').val(data.name)
                $('#msglevel5').text(data.msg);
          
        }
    });
    
});

// $("#level5name").submit(function(e) {

//     e.preventDefault(); // avoid to execute the actual submit of the form.

//     var form = $(this);
//     var actionUrl = form.attr('action');
    
//     $.ajax({
//         type: "POST",
//         url: "levels",
//         data: form.serialize(), // serializes the form's elements.
//         success: function(data)
//         {
//           alert(data); // show response from the php script.
//         }
//     });
    
// });

//levels close