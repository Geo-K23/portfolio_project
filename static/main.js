function fetchPoultryData() {
    fetch('/api/poultry')
        .then(response => response.json())
        .then(data => {
            data.forEach(product => {
                const productElement = document.createElement('div');
                productElement.innerHTML = `
                    <h2>${product.name}</h2>
                    <p>Price: $${product.price}</p>
                    <p>Quantity: ${product.quantity} available</p>
                    <p>Seller: ${product.seller}</p>
                    <p>Phone: ${product.phone}</p>
                    <p>${product.description}</p>
                `;
                document.getElementById('products').appendChild(productElement);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}

fetchPoultryData();
