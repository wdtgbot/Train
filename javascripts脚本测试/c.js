var body0 = "answers=%5B%220%22%5D&seq=3&temperature=36.0&userId=&latitude=23.208688735961914&longitude=112.85215759277344&country=%E4%B8%AD%E5%9B%BDprovince=%E5%B9%BF%E4%B8%9C%E7%9C%81&city=%E4%BD%9B%E5%B1%B1%E5%B8%82&district=%E4%B8%89%E6%B0%B4%E5%8C%BA&township=%E4%BA%91%E4%B8%9C%E6%B5%B7%E8%A1%97%E9%81%93&street=%E5%A4%A7%E5%AD%A6%E8%B7%AF&myArea=&areacode=440607"
const body = body0.split("&")
const arr = ["province", "city", "district", "township", "street", "areacode", "latitude", "longitude"]
for(var i = 0; i < body.length; i++) {
  for (var m = 0; i < arr.length; m++) {
    if (body[i].indexOf(arr[i]) != -1) {
      console.log(body[i].split("=")[1])
    }
  }
}
$done()