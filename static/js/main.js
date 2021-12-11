const btnD=document.querySelectorAll('.btn-delete')

//con este codigo al presionar eliminar si acepto el mensaje del evento me borra si cancelo detiene el click
if(btnD){
   const btnArray= Array.from(btnD)
   btnArray.forEach((btn)=>{
    btn.addEventListener('click', (e)=>{
        if(!confirm('Are you sure you want to delete it?')){
            e.preventDefault();
        }
    });
   });
}