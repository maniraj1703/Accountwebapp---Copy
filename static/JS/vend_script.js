const form =document.querySelector("#form");
const bank_name =document.querySelector('#Bank_Name')
const ifsc_num =document.querySelector('#IFSC_Number')
const acc_num =document.querySelector('#Acc_Number')
const holder_name =document.querySelector('#Holder_Name')
const mob_num =document.querySelector('#Mob_Number')

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
    if (bank_name.value.trim() == ''){
        setError(bank_name, "Enter Bank Name");
    }else if(bank_name.value.trim().length < 3 || bank_name.value.trim().length > 15){
        setError(bank_name, "Bank Name must be in Min 3 and Max 15 letters");
    }else{
        setSuccess(bank_name);
    }
    if (ifsc_num.value.trim() == ''){
        setError(ifsc_num, "Enter IFSC Number");
    }else if(isIFSCValid(ifsc_num.value)){
        setSuccess(ifsc_num);
    }else{
        setError(ifsc_num,"Provide valid IFSC Number");
    }if (acc_num.value.trim() == ''){
        setError(acc_num,"Enter Account Number");
    }else if(acc_num.value.trim().length > 13 || acc_num.value.trim().length < 13 || isNaN(acc_num.value)){
        setError(acc_num, "Invalid Account Number");
    }else{
        setSuccess(acc_num);
    }if(holder_name.value.trim() == ''){
        setError(holder_name,"Enter Holder Number");
    }else if(holder_name.value.trim().length < 3 || holder_name.value.trim().length > 30){
        setError(holder_name, "Name must be in Min 3 and Max 30 Characters");
    }else{
        setSuccess(holder_name);
    }
    if(mob_num.value.trim() == ''){
        setError(mob_num,'Enter Mobile Number');
    }else if(mob_num.value.trim().length > 10 || mob_num.value.trim().length < 10 || isNaN(mob_num.value)){
        setError(mob_num,'Invalid Mobile Number');
    }else{
        setSuccess(mob_num);
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
function isIFSCValid(ifsc){
    const reg = /^[A-Z]{4}0[A-Z0-9]{6}$/;
    return reg.test(ifsc);
}
