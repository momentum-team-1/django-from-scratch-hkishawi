let cardContainer = document.querySelector('.card-container')
cardContainer.addEventListener('click', (event) => {
   event.preventDefault()
   cardContainer.classList.toggle('flipped')
})