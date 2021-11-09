
function myFunction() {
  var x = document.getElementById("addproduct");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function ProFn(){


var quantity = document.getElementById('productquantity').value;
var rate = document.getElementById('productrate').value
var discountPercent = document.getElementById('productdiscountPercent').value
var discount = document.getElementById('productdiscount').value
var gst = document.getElementById('productgst').value


var QR = quantity*rate;
var DPR = (discountPercent/100)*QR;
var ra = QR-DPR-discount;
var gt = gst*1
var FP = ra + gt;
console.log(FP)
document.getElementById('productvalue').value = FP;
}
