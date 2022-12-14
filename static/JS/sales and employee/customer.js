const form =document.querySelector("#form");
const customer_name =document.querySelector('#cus_Name')
const customer_email =document.querySelector('#cus_Email')
const customer_Phoneno =document.querySelector('#cus_Phoneno')
const customer_Type =document.querySelector('#cus_Type')


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
    if (customer_name.value.trim() == ''){
        setError(customer_name, "Enter Customer Name");
    }else if(customer_name.value.trim().length < 3 || customer_name.value.trim().length > 15){
        setError(customer_name, "Customer Name must be in Min 3 and Max 15 letters");
    }else{
        setSuccess(customer_name);
    }



    if(customer_Phoneno.value.trim() == ''){
        setError(customer_Phoneno,'Enter Mobile Number');
    }else if(customer_Phoneno.value.trim().length > 10 || mob_num.value.trim().length < 10 || isNaN(customer_Phoneno.value)){
        setError(customer_Phoneno,'Invalid Mobile Number');
    }else{
        setSuccess(customer_Phoneno);
    }


    if (customer_email.value.trim() == ''){
        setError(customer_email, "Enter Customer Email");
    }else if(iscustomer_emailValid(customer_email.value)){
        setSuccess(customer_email);
    }else{
        setError(customer_email,"Provide valid Email");
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
function isEmailValid(customer_email){
    const reg = /^[A-Z]{4}0[A-Z0-9]{6}$/;
    return reg.test(customer_email);
}
