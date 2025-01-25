function loadXMLDoc() {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      Arry = JSON.parse(this.responseText);
      data_obj = Arry.data;
      results_obj = data_obj.results;
      res_list = [];

      for (i = 0; i < 13; i++) {
        imgtitle = [];
        imglist = results_obj[i].filelist;
        imglist_sub1 = imglist.substring(4, imglist.length - 1);
        httpidx = imglist_sub1.indexOf("http");
        imgurl =
          "http" + imglist_sub1.substring(0, imglist_sub1.indexOf("http"));
        imgtitle.push(imgurl);
        imgtitle.push(results_obj[i].stitle);
        res_list.push(imgtitle);
      }
      //console.log(res_list);

      for (j = 0; j < res_list.length; j++) {
        img_id = document.getElementById("img" + j);
        if (j < 3) {
          img_id.src = res_list[j][0];
        } else {
          img_id.style.backgroundImage = "url(" + res_list[j][0] + ")";
        }

        textnode = document.createTextNode(res_list[j][1]);
        div_id = document.getElementById("div" + j);
        div_id.appendChild(textnode);
      }
    }
  };
  url =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";
  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}

// burger menu
const hamburger = document.querySelector(".hamburger");
const cross = document.querySelector(".cross");
const menu = document.querySelector(".menu");

// click burger icon
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  cross.classList.toggle("active");
  menu.classList.toggle("active");
});

// click cross icon
cross.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  cross.classList.toggle("active");
  menu.classList.toggle("active");
});
loadXMLDoc();
