const form =document.querySelector("#form");
const phone =document.querySelector('#Phone_Number')
const product =document.querySelector('#Product')
const Product_Quantity =document.querySelector('#Product_Quantity')
const price =document.querySelector('#Price')


form.addEventListener('submit',(event)=>{
    
    validateForm();
    console.log(isFormValid());
    
    if (isFormValid() == true){
        form.submit();
    }else{
        event.preventDefault();
    }
});

function isFormValid(){
    const inputContainers = form.querySelectorAll('.form-group');
    let result = true;
    inputContainers.forEach((container)=>{
        if (container.classList.contains('error')){
            result = false;
        }
    });
    return result;
}

function validateForm(){
    if (phone.value.trim() == ''){
        setError(phone, "Enter Phone Number");
    }else if(phone.value.trim().length > 10 || mob_num.value.trim().length < 10 || isNaN(phone.value)){
        setError(phone,'Invalid Mobile Number');
    }else{
        setSuccess(phone);
    }

    if ( product.value.trim() == ''){
        setError( product, "Enter Product Name");
    }else if(isNaN( product.value.trim().length < 3 || product.value.trim().length > 30)){
        setError(product, "Name must be in Min 3 and Max 30 Characters");
        
    }else{
        setSuccess( product);
    }

    if ( Product_Quantity.value.trim() == ''){
        setError( Product_Quantity, "Enter Quantity");
    }else if(isNaN( Product_Quantity.value)){
        setError( Product_Quantity,'Invalid Quantity');
    }else{
        setSuccess( Product_Quantity );
    }


    if ( price.value.trim() == ''){
        setError( price, "Enter Price");
    }else if(isNaN( price.value)){
        setError( price,'Invalid Price');
    }else{
        setSuccess( price);
    }
}
function setError(element, errorMsg){
    const parent = element.parentElement;
    if (parent.classList.contains('success')){
        parent.classList.remove('success');
    }
    parent.classList.add('error');
    const paragraph = parent.querySelector('p');
    paragraph.textContent = errorMsg;
}
function setSuccess(element){
    const parent  = element.parentElement;
    if (parent.classList.contains('error')){
        parent.classList.remove('error');
    }
    parent.classList.add('success');
}
