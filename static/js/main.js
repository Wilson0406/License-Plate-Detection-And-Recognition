const cost = [500,200,17.6];
const input = document.getElementById("input");
const current = document.getElementById("curr");
const totalv = document.getElementById("totv");
const tax = document.getElementById("tax");
const totalInvoice = document.getElementById("total");
const generate = document.getElementById("generate");
const qr = document.getElementsByClassName("qr-code");

const service = ['Current Challan', 'Total Violation', 'TAX'];
let listItems = "";
let total = 0;
let count1 = 0;
let count2 = 0;
let count3 = 0;


// function htmlEncode(value) {
// 	return $('<div/>').text(value)
// 		.html();
// 	}
// remove.addEventListener("click", function(){
  
// })
function render(num) {
        listItems += `
            <tr class="row-data">
              <td colspan="2">${service[num]} </td>
              <td>₹${cost[num]}</td>
            </tr>
            `
        totalInvoice.innerHTML = `₹${total}`;
    // input.innerHTML = listItems;
}

generate.addEventListener("click", function() {
  let url = 'https://api.qrserver.com/v1/create-qr-code/?data=₹' + total + '&amp;size=250x250';
  location.replace(url)
})

current.addEventListener("click", function() {
  if(count1 == 0){
    total += 500;
    sessionStorage.setItem("totals", total);
    render(0);
  input.innerHTML = listItems;}
  count1 += 1;
})

totalv.addEventListener("click", function() {
  if(count2 == 0){
    total += 200;
    sessionStorage.setItem("totals", total);
    render(1);
  input.innerHTML = listItems;}
  count2 += 1;
})

tax.addEventListener("click", function() {
  if(count3 == 0){
    total += 17.6;
    sessionStorage.setItem("totals", total);
    render(2);
  input.innerHTML = listItems;}
  count3 += 1;
})
