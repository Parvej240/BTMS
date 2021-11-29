var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product Id:', productId, 'Action', action)
        console.log('User: ', user)
        if (user === 'AnonymousUser') {
            console.log('Not Logged in')
        } else {
            console.log('User is Logged in')
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User in Logged in, Sending Data....')
    var url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            location.reload()
        })
}