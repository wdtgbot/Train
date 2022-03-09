const body0 = `a=1&b=2&c=3`
const body1 = body0.split("&")
console.log(body1)
for(var i = 0; i < body1.length; i++) {
    console.log(body1[i])
    if (body1[i].indexOf("a") != -1) {
        console.log(body1[i].split("=")[1])
    }
}