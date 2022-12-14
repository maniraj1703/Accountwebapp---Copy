const form =document.querySelector("#form");
const product  =document.querySelector('#Product')
const productQuantity =document.querySelector('#ProductQuantity')
const Price =document.querySelector('#Price')

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
     if (productQuantity.value.trim() == ''){
        setError(productQuantity, "Provide quantity of Product");
    }else if(isNaN(productQuantity.value)){
        setError(productQuantity,"Provide quantity of Product");
    }else{
         setSuccess(productQuantity);
    }


    if(Price.value.trim() == ''){
        setError(Price,'Enter Price');
    }else if(isNaN( Price.value)){
        setError( Price,'Invalid Price');
    }else{
        setSuccess( Price);
    }
  
    
    if (product.value.trim() == ''){
            setError(product, "Enter Product Name");
    }else if(product.value.trim().length < 4 || product.value.trim().length > 15){
            setError(product, "Product Name must be in Min 4 and Max 15 letters");
    }else{
            setSuccess(product);
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

