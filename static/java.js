document.addEventListener("DOMContentLoaded", function () {
    const cartContent = document.getElementById('cart-content');
    const emptyMessage = document.getElementById('cart-empty-message');
    const cartSummary = document.getElementById('cart-summary');
    const serviceFeeEl = document.getElementById('service-fee');
    const totalSumEl = document.getElementById('total-sum');
    const serviceFeePercentage = 0.10;

    let cartHasItems = false;
    let totalSum = 0;

    // Savatdagi har bir mahsulotni localStorage'dan olish
    Object.keys(localStorage).forEach(key => {
        if (key.startsWith("product_")) {
            cartHasItems = true;
            const product = JSON.parse(localStorage.getItem(key));
            const price = parseFloat(product.price);
            const quantity = parseInt(product.quantity);
            const subtotal = price * quantity;
            totalSum += subtotal;

            // Savat elementlarini yaratish
            const itemElement = document.createElement('div');
            itemElement.classList.add('cart-item');
            itemElement.innerHTML = `
                <div class="cart-item-details">
                    <h3 class="cart-item-title">${product.title}</h3>
                    <p>${quantity} dona x ${price} so'm = ${(subtotal).toFixed(2)} so'm</p>
                </div>
                <button class="remove-btn" onclick="removeFromCart('${key}')">O'chirish</button>
            `;
            cartContent.appendChild(itemElement);
        }
    });

    // Savatdagi ma'lumotlarni yangilash
    if (cartHasItems) {
        const serviceFee = totalSum * serviceFeePercentage;
        const finalTotal = totalSum + serviceFee;

        serviceFeeEl.textContent = serviceFee.toFixed(2);
        totalSumEl.textContent = finalTotal.toFixed(2);

        cartContent.style.display = 'block';
        cartSummary.style.display = 'block';
    } else {
        emptyMessage.style.display = 'block';
    }

    // Savatni tozalash funksiyasi
    document.getElementById('clear-cart').addEventListener('click', function () {
        localStorage.clear();
        window.location.reload();
    });

    // Savatdan mahsulotni o'chirish funksiyasi
    window.removeFromCart = function (key) {
        localStorage.removeItem(key);
        window.location.reload();
    };
});