function file_upload()
{
    // フォームデータを取得
    var formdata = new FormData($('#my_form').get(0));

    // POSTでアップロード
    $.ajax({
        url  : "http://your_site.com/upload.php",
        type : "POST",
        data : formdata,
        cache       : false,
        contentType : false,
        processData : false,
        dataType    : "html"
    })
    .done(function(data, textStatus, jqXHR){
        alert(data);
    })
    .fail(function(jqXHR, textStatus, errorThrown){
        alert("fail");
    });
}
