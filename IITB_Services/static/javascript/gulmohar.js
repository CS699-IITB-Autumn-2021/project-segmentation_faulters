if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded',ready)
}else{
    ready()
}
function ready(){

    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
    for(var i = 0; i < quantityInputs.length; i++){
        var input = quantityInputs[i]
        input.addEventListener('change', quantityChanged)
    }


    document.getElementsByClassName('btn-purchase')[0].addEventListener('click',purchasedClicked)
}

function purchasedClicked()
{

    var cartItemContainer = document.getElementsByClassName('cartItem')[0]
    var cartRows = cartItemContainer.getElementsByClassName('cart-row')
    var total = 0
    var list = []
    for(var i = 0; i < cartRows.length; i++){
        var cartRow = cartRows[i]
        var cartlabel = cartRow.getElementsByClassName('cart-item-title')[0]
        var title = cartlabel.textContent
        var priceElement = cartRow.getElementsByClassName('cart-price')[0]
        var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
        var price  = parseFloat(priceElement.innerText.replace('₹',''))
        var quantity = quantityElement.value
        if(quantity>0)
        list.push([title,quantity])
        quantityElement.value=0
        updateCartTotal() // to set all values to 0 again
        total += price*quantity
    }
    total = Math.round(total*100)/100
    // document.getElementsByClassName('cart-total-price')[0].innerText = '₹ '+ total
    if(total > 0){
        var temp = listprint(list)
        var orderd= orderdetails(list)
        var r = confirm(' \n Your order list is:\n'+temp+ 'Your Total is : '+total+'\nClick OK to confirm')
        if (r == true) {
            alert('Thank you for your order..')
            var vendor="Gulmohar"
            console.log(temp)
            window.location.href= "/orderDone?price="+total+"&list="+orderd+"&vendor="+vendor;
        } else {
            alert('Try again')
        }
        
    }else {
        alert('please add items')
    }

}
function listprint(list)
{
    var listString = ''
    for(var i = 0; i < list.length; i++)
    {
        listString+=i+1
        listString+='. '
        listString+=list[i][0];
        listString+=':'
        listString+=list[i][1]
        listString+="\n"
    }
    return listString
}
function orderdetails(list)
{
    var listString = ''
    for(var i = 0; i < list.length; i++)
    {
        listString+=list[i][0];
        listString+=':'
        listString+=list[i][1]
        listString+="!,"
    }
    return listString
}

function quantityChanged(event){
    var input = event.target
    if(isNaN(input.value) || input.value < 0)input.value=0
    updateCartTotal()
}

function deleteClick(name) {
    document.getElementsByName(name)[0].value = 0
    updateCartTotal()
  }


function updateCartTotal(){
    var cartItemContainer = document.getElementsByClassName('cartItem')[0]
    var cartRows = cartItemContainer.getElementsByClassName('cart-row')
    var total = 0
    for(var i = 0; i < cartRows.length; i++){
        var cartRow = cartRows[i]
        var priceElement = cartRow.getElementsByClassName('cart-price')[0]
        var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
        var price  = parseFloat(priceElement.innerText.replace('₹',''))
        var quantity = quantityElement.value
        total += price*quantity

    }
    total = Math.round(total*100)/100
    document.getElementsByClassName('cart-total-price')[0].innerText = '₹ '+ total
}