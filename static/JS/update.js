const form =document.querySelector("#form");
const ifsc_num =document.querySelector('#IFSC_Number')
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
    if (ifsc_num.value.trim() == ''){
        setError(ifsc_num, "Enter IFSC Number");
    }else if(isIFSCValid(ifsc_num.value)){
        setSuccess(ifsc_num);
    }else{
        setError(ifsc_num,"Provide valid IFSC Number");
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
