function getCookie(e){var t=null;if(document.cookie&&""!=document.cookie)for(var o=document.cookie.split(";"),a=0;a<o.length;a++){var i=jQuery.trim(o[a]);if(i.substring(0,e.length+1)==e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}function csrfSafeMethod(e){return/^(GET|HEAD|OPTIONS|TRACE)$/.test(e)}$(function(){$('[data-toggle="tooltip"]').tooltip();new EpicEditor({basePath:"//cdn.bootcss.com/epiceditor/0.2.2",clientSideStorage:!1,theme:{base:"/themes/base/epiceditor.css",preview:"/themes/preview/github.css",editor:"/themes/editor/epic-dark.css"},autogrow:{minHeight:250},button:{bar:!0}}).load()});var csrftoken=getCookie("csrftoken");$.ajaxSetup({beforeSend:function(e,t){csrfSafeMethod(t.type)||this.crossDomain||e.setRequestHeader("X-CSRFToken",csrftoken)}}),$("#category-modal .modal-footer button:first").click(function(){$.post("/new_category/",{category:$("#id_category").val()},function(e,t){if("success"===t){if("success"===e.status){var o='<input checked="checked" id="id_categories_'+e.category.id+'" name="categories" type="checkbox" value="'+e.category.id+'" />',a='<label for="id_categories_'+e.category.id+'">'+e.category.category+"</label>";$li=$("<li></li>").append($(a).prepend($(o))),$("#id_categories").append($li)}}else console.log("新分类的ajax请求失败：",t);$("#category-modal").modal("hide")},"json")}),$("#tag-modal .modal-footer button:first").click(function(){$.post("/new_tag/",{tag:$("#id_tag").val()},function(e,t){if("success"===t){if("success"===e.status){var o='<input checked="checked" id="id_tags_'+e.tag.id+'" name="tags" type="checkbox" value="'+e.tag.id+'" />',a='<label for="id_tags_'+e.tag.id+'">'+e.tag.tag+"</label>";$li=$("<li></li>").append($(a).prepend($(o))),$("#id_tags").append($li)}}else console.log("新标签的ajax请求失败：",t);$("#tag-modal").modal("hide")},"json")});