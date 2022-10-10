console.log('Hello World')
const deleteMenu = document.getElementById('delete-menu');

deleteMenu.addEventListener('click',(e)=>{
  e.preventDefault();
  const id= deleteMenu.dataset.id;
  const csrfToken = deleteMenu.dataset.csrftoken
  if(confirm('Are you sure do you want to delete this menu?')){
    fetch(`http://localhost:8000/menus/delete/${id}`,
      {
        method:'POST',
        headers:{'X-CSRFToken':csrfToken}    
      })
    .then(res=>{
      window.location.replace('http://localhost:8000/menus/')
    })
    .catch(err=>console.log(err))

  }
})