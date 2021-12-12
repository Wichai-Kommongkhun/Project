$(document).ready(function(){
  $("#imgfile").change(function(){
    var fileLength = this.files.length;
    var match = ["image/jpeg", "image/png", "image/jpg", "image/gif"];
    var i;
    for (i = 0; i < fileLength; i++){
      var file = this.file[i];
      var imagefile = file.type;
      if(!((imagefile==match[0]) || (imagefile==match[1]) || (imagefile==match[2]) || (imagefile==match[3]))){
      
        alert('กรุณาเลือกไฟล์ ที่เป็นนามสกุล JPG/JPEG/PNG/GIF');
        $("#imgfile").val('');
        return false;
      }
    }
  });
});


