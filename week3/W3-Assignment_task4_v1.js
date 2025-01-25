function loadXMLDoc() {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      Arry = JSON.parse(this.responseText);
      data_obj = Arry.data;
      results_obj = data_obj.results;
      res_list = [];
      console.info("~~~~~~~~~~~~~" + results_obj.length);
      for (i = 0; i < results_obj.length; i++) {
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

      bigDiv = document.getElementById("big");
      for (j = 0; j < 13; j++) {
        bigboxNode = document.createElement("div");
        bigboxNode.setAttribute("id", "img" + j);
        bigboxNode.setAttribute("class", "bigbox");

        textnode = document.createTextNode(res_list[j][1]);

        if (j < 3) {
          img_id = document.getElementById("img" + j);
          img_id.src = res_list[j][0];
          div_id = document.getElementById("div" + j);
          div_id.appendChild(textnode);
        } else {
          bigboxNode.style.backgroundImage = "url(" + res_list[j][0] + ")";
          starNode = document.createElement("div");
          starNode.setAttribute("class", "star");
          starImgNode = document.createElement("img");
          starImgNode.src = "w3-pictures/staricon.png";
          starNode.appendChild(starImgNode);

          footNode = document.createElement("div");
          footNode.setAttribute("class", "foot");
          footTxtNode = document.createElement("div");
          footTxtNode.setAttribute("class", "foot-text");
          footTxtNode.appendChild(textnode);
          footNode.appendChild(footTxtNode);

          bigboxNode.appendChild(starNode);
          bigboxNode.appendChild(footNode);
          bigDiv.appendChild(bigboxNode);
        }
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
const loadBtn = document.querySelector(".more");

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

loadBtn.addEventListener("click", () => {
  let childcnt = document.getElementById("big").childElementCount;
  console.log("~~~~~~~" + childcnt);

  bigDiv = document.getElementById("big");
  for (j = 3 + childcnt; j < 3 + childcnt + 10; j++) {
    bigboxNode = document.createElement("div");
    bigboxNode.setAttribute("id", "img" + j);
    bigboxNode.setAttribute("class", "bigbox");

    textnode = document.createTextNode(res_list[j][1]);

    bigboxNode.style.backgroundImage = "url(" + res_list[j][0] + ")";
    starNode = document.createElement("div");
    starNode.setAttribute("class", "star");
    starImgNode = document.createElement("img");
    starImgNode.src = "w3-pictures/staricon.png";
    starNode.appendChild(starImgNode);

    footNode = document.createElement("div");
    footNode.setAttribute("class", "foot");
    footTxtNode = document.createElement("div");
    footTxtNode.setAttribute("class", "foot-text");
    footTxtNode.appendChild(textnode);
    footNode.appendChild(footTxtNode);

    bigboxNode.appendChild(starNode);
    bigboxNode.appendChild(footNode);
    bigDiv.appendChild(bigboxNode);

    let currentCnt = document.getElementById("big").childElementCount;
    if (currentCnt === res_list.length - 3) {
      loadBtn.style.cssText = "display:none;";
    }
  }
});
loadXMLDoc();
