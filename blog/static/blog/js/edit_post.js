$(function () {
    $('[data-toggle="tooltip"]').tooltip();
    var editor = new EpicEditor({
        basePath: "//cdn.bootcss.com/epiceditor/0.2.2",
        clientSideStorage: false,
        theme: {
            base: '/themes/base/epiceditor.css',
            preview: '/themes/preview/github.css',
            editor: '/themes/editor/epic-dark.css'
        },
        autogrow: {
            minHeight: 250
        },
        button: {
            bar: true
        }
    }).load();
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#category-modal .modal-footer button:first').click(function(){
    $.post('/new_category/', {
        'category': $('#id_category').val(),
    }, function(data, textStatus){
        if(textStatus === 'success') {
            if (data['status']==='success'){
                var checkbox = '<input checked=\"checked\" id=\"id_categories_' +
                    data['category']['id'] +
                    '\" name=\"categories\" type=\"checkbox\" value=\"' +
                    data['category']['id'] +
                    '\" />';
                var label = '<label for=\"id_categories_' +
                    data['category']['id'] +
                    '\">'+ data['category']['category'] + '</label>';
                $li = $('<li></li>').append($(label).prepend($(checkbox)));
                $('#id_categories').append($li);
            }
        }else{
            console.log('新分类的ajax请求失败：', textStatus);
        }
        $('#category-modal').modal('hide');
    }, 'json');
});

$('#tag-modal .modal-footer button:first').click(function(){
    $.post('/new_tag/', {
        'tag': $('#id_tag').val(),
    }, function(data, textStatus){
        if(textStatus === 'success'){
            if (data['status'] === 'success'){
              var checkbox = '<input checked=\"checked\" id=\"id_tags_' +
                  data['tag']['id'] +
                  '\" name=\"tags\" type=\"checkbox\" value=\"' +
                  data['tag']['id'] +
                  '\" />';
              var label = '<label for=\"id_tags_' +
                  data['tag']['id'] +
                  '\">'+ data['tag']['tag'] + '</label>';
              $li = $('<li></li>').append($(label).prepend($(checkbox)));
              $('#id_tags').append($li);
            }
        }else{
            console.log('新标签的ajax请求失败：', textStatus);
        }
        $('#tag-modal').modal('hide');
    }, 'json');
});
