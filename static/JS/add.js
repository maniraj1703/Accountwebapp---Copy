const form =document.querySelector("#form");
const phone_No =document.querySelector('#Phone_No')
const product =document.querySelector('#Product')
const productQuantity =document.querySelector('#ProductQuantity')
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
    if (product.value.trim() == ''){
        setError(product, "Enter Product Name");
    }else if(product.value.trim().length < 4 || product.value.trim().length > 15){
        setError(product, "Product Name must be in Min 4 and Max 15 letters");
    }else{
        setSuccess(product);
    }

    if(phone_No.value.trim() == ''){
        setError(phone_No,'Enter Phone Number');
    }else if(phone_No.value.trim().length > 10 || phone_No.value.trim().length < 10 || isNaN(phone_No.value)){
        setError(phone_No,'Invalid Phone Number');
    }else{
        setSuccess(phone_No);
    }

    if (productQuantity.value.trim() == ''){
        setError(productQuantity, "Provide quantity of Product");
    }else if(isNaN(productQuantity.value)){
        setError(productQuantity,"Provide quantity of Product");
    }else{
         setSuccess(productQuantity);
    }

   
    if(price.value.trim() == ''){
        setError(price,'Enter Price');
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