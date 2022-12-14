const form =document.querySelector("#form");
const Name  =document.querySelector("#Name")
const Amount =document.querySelector("#Amount")

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
    if(Amount.value.trim() == ''){
        setError(Price,'Enter Price');
    }else if(isNaN(Amount.value)){
        setError( Amount,'Invalid Price');
    }else{
        setSuccess( Amount);
    }
  
    
    if (Name.value.trim() == ''){
            setError(Name, "Enter  Name");
    }else if(product.value.trim().length < 2 || Name.value.trim().length > 15){
            setError(Name, "Product Name must be in Min 4 and Max 15 letters");
    }else{
            setSuccess(Name);
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

