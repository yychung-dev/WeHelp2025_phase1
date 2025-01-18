console.log("=== Task 1 ===");
function findAndPrint(messages, currentStation) {
  const allStation = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xiaobitan",
    "Xindian City Hall",
    "Xindian",
  ];
  const allButBranch = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];
  const allSub1 = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xiaobitan",
  ];
  const allSub2 = ["Xiaobitan", "Qizhang", "Xindian City Hall", "Xindian"];
  if (!allStation.includes(currentStation)) {
    console.log(`Current station ${currentStation} is not in green line.`);
    return;
  }
  const friendName = Object.keys(messages);
  const friendSay = Object.values(messages);
  let friendStation = [];
  let distance = [];
  for (let i = 0; i < friendSay.length; i++) {
    let notInLine = "yes";
    for (let j = 0; j < allStation.length; j++) {
      let role = new RegExp(allStation[j]);
      if (role.test(friendSay[i])) {
        friendStation.splice(i, 0, allStation[j]);
        notInLine = "no";
        break;
      }
    }
    if (notInLine === "yes") {
      friendStation.splice(i, 0, "not in green line");
    }
  }
  for (let k = 0; k < friendStation.length; k++) {
    if (
      allButBranch.includes(currentStation) &&
      allButBranch.includes(friendStation[k])
    ) {
      distance.splice(
        k,
        0,
        Math.abs(
          allButBranch.indexOf(currentStation) -
            allButBranch.indexOf(friendStation[k])
        )
      );
    } else {
      if (
        allSub1.includes(currentStation) &&
        allSub1.includes(friendStation[k])
      ) {
        distance.splice(
          k,
          0,
          Math.abs(
            allSub1.indexOf(currentStation) - allSub1.indexOf(friendStation[k])
          )
        );
      } else {
        if (friendStation[k] === "not in green line") {
          distance.splice(k, 0, 99999);
        } else {
          distance.splice(
            k,
            0,
            Math.abs(
              allSub2.indexOf(currentStation) -
                allSub2.indexOf(friendStation[k])
            )
          );
        }
      }
    }
  }
  console.log(friendName[distance.indexOf(Math.min(...distance))]);
}

const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong");
findAndPrint(messages, "Songshan");
findAndPrint(messages, "Qizhang");
findAndPrint(messages, "Ximen");
findAndPrint(messages, "Xindian City Hall");

console.log("=== Task 2 ===");
let johnArr = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24,
];
let bobArr = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24,
];
let jennyArr = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24,
];

function countTime(hour, duration) {
  let result = [];
  for (let i = 0; i < duration; i++) {
    result.push(hour + i);
  }
  return result;
}

function chooseConsultant(consultants, criteria, unavailConstArr) {
  let consultantFinalResult = [];
  if (criteria === "price") {
    let priceresult = consultants.sort(function (a, b) {
      return a.price - b.price;
    });
    for (let i = 0; i < priceresult.length; i++) {
      if (!unavailConstArr.includes(priceresult[i].name)) {
        consultantFinalResult.push(priceresult[i].name);
      }
    }
    return consultantFinalResult[0];
  } else {
    let rateresult = consultants.sort(function (a, b) {
      return b.rate - a.rate;
    });
    for (let i = 0; i < rateresult.length; i++) {
      if (!unavailConstArr.includes(rateresult[i].name)) {
        consultantFinalResult.push(rateresult[i].name);
      }
    }
    return consultantFinalResult[0];
  }
}

function book(consultants, hour, duration, criteria) {
  let found = false;
  let targTimeArr = countTime(hour, duration);
  let unavailConstArr = new Set();
  while ([...unavailConstArr].length < 3) {
    let targConsultant = chooseConsultant(consultants, criteria, [
      ...unavailConstArr,
    ]);
    if (targConsultant === "John") {
      if (new Set(targTimeArr).isSubsetOf(new Set(johnArr))) {
        johnArr.splice(johnArr.indexOf(hour), duration);
        console.log("John");
        found = true;
        break;
      } else {
        unavailConstArr.add("John");
      }
    } else if (targConsultant === "Bob") {
      if (new Set(targTimeArr).isSubsetOf(new Set(bobArr))) {
        bobArr.splice(bobArr.indexOf(hour), duration);
        console.log("Bob");
        found = true;
        break;
      } else {
        unavailConstArr.add("Bob");
      }
    } else if (targConsultant === "Jenny") {
      if (new Set(targTimeArr).isSubsetOf(new Set(jennyArr))) {
        jennyArr.splice(jennyArr.indexOf(hour), duration);
        console.log("Jenny");
        found = true;
        break;
      } else {
        unavailConstArr.add("Jenny");
      }
    }
  }
  if (!found) {
    console.log("No Service");
  }
}

consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];
book(consultants, 15, 1, "price");
book(consultants, 11, 2, "price");
book(consultants, 10, 2, "price");
book(consultants, 20, 2, "rate");
book(consultants, 11, 1, "rate");
book(consultants, 11, 2, "rate");
book(consultants, 14, 3, "price");

console.log("=== Task 3 ===");
function func(...data) {
  let uniqueList = "";
  for (let i = 0; i < data.length; i++) {
    let uniqueFlag = 1;
    let name1 = pickMidname(data[i]);
    for (let j = 0; j < data.length; j++) {
      if (i !== j) {
        let name2 = pickMidname(data[j]);
        if (name1 === name2) {
          uniqueFlag = 0;
          break;
        }
      }
    }

    if (uniqueFlag === 1) {
      uniqueList = uniqueList + "" + data[i];
    }
  }
  if (uniqueList === "") {
    uniqueList = "沒有";
  }

  console.log(uniqueList);
}

function pickMidname(fullname) {
  let midname = "";
  if (fullname.length === 2) {
    midname = fullname[1];
  } else if (fullname.length === 3) {
    midname = fullname[1];
  } else if (fullname.length === 4) {
    midname = fullname[2];
  } else if (fullname.length === 5) {
    midname = fullname[2];
  }
  return midname;
}
func("彭大牆", "陳王明雅", "吳明");
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花");
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花");
func("郭宣雅", "夏曼藍波安", "郭宣恆");

console.log("=== Task 4 ===");
function getNumber(index) {
  let number = 0;
  let x = [4, 4, -1];
  let xTotal = 0;
  for (let i = 0; i < x.length; i++) {
    xTotal = xTotal + x[i];
  }

  let quotient = Math.trunc(index / 3);
  let remainder = index % 3;

  number = number + xTotal * quotient;

  for (let i = 0; i < remainder; i++) {
    number = number + x[i];
  }

  console.log(number);
}
getNumber(1);
getNumber(5);
getNumber(10);
getNumber(30);
