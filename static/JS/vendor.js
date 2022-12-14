const form =document.querySelector("#form");
const Name =document.querySelector('#Name')
const phone_No =document.querySelector('#Phone_No')
const email =document.querySelector('#Email')
const billing_Address =document.querySelector('#Billing_Address')


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
    if (phone_No.value.trim() == ''){
        setError(phone_No, "Enter Phone Number");
    }else if(phone_No.value.trim().length > 10 || phone_No.value.trim().length < 10 || isNaN(phone_No.value)){
        setError(phone_No,'Invalid Mobile Number');
    }else{
        setSuccess(phone_No);
    }

    if ( Name.value.trim() == ''){
        setError( Name, "Enter Name");
    }else if(isNaN( Name.value.trim().length < 4 || Name.value.trim().length > 30)){
        setError(Name, "Name must be in Min 4 and Max 30 Characters");
        
    }else{
        setSuccess(Name);
    }

    if ( billing_Address.value.trim() == ''){
        setError( billing_Address, "Enter  Address");
    }else if(isNaN( billing_Address.value.trim().length < 10 || billing_Address.value.trim().length > 50)){
        setError(billing_Address, "Address must be in Min 10 and Max 50 Characters");
        
    }else{
        setSuccess( billing_Address);
    }

    if (email .value.trim() == ''){
        setError(email , "Enter Email ");
    }else if(isEmailValid(email.value)){
        setSuccess(email );
    }else{
        setError(email ,"Provide valid Email");
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
function isEmailValid(email){
    const reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return reg.test(email);
}
