document.querySelector('button').addEventListener('click', function(event) {
    const container = document.querySelector("#container")
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    var row = document.querySelector('#row').value
    var col = document.querySelector('#col').value
    var arr = [];
    while (arr.length < 6) {
        var randomNum = Math.floor(Math.random() * row * col) + 1
        if (arr.indexOf(randomNum) === -1) {
            arr.push(randomNum)
        }
    console.log(arr)
    }
    for(var i=0; i<row; i++) {
        for (var j=0; j<col; j++) {
            const card = document.createElement('div')
            const card_front = document.createElement('div')
            const card_back = document.createElement('div')
            card.className = 'card' 
            card_front.className = 'card_front' 
            card_back.className = 'card_back' 
            card.row = i
            card.col = j
            card.num = i*col + j + 1
            card.style.marginTop = `${i*130}px`
            card.style.marginLeft = `${j*90}px`
            card_front.innerText = `${card.num}`
            if (arr.indexOf(card.num) === -1) {
                card_back.innerText = `꽝`
            } else {
                // card_back.classList.toggle(`png0`)
                const card_img = document.createElement('img')
                card_img.src = `images/${arr.indexOf(card.num) % 3}.png`
                card_img.className = `card_img`
                card_img.style.border = ''
                card_back.appendChild(card_img)
            }
            card.addEventListener('click', function(event) {
                card.classList.toggle('wrap')
            })
            card.appendChild(card_front)
            card.appendChild(card_back)
            container.appendChild(card)
        }
    }
})
