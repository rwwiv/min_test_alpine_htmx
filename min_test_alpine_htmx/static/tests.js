document.addEventListener('alpine:init', () => {
  Alpine.data('booklist', () => ({
    books: ['re:monarch', 'landmines', 'hellmode']
  }))
  Alpine.data('animallist', () => ({
    animals: ['dog', 'cat', 'manbearpig']
  }))
})
