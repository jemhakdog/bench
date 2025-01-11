async function addToCart(button) {
    // Get product details from the card
    const card = button.closest('.card-body');
    const productName = card.querySelector('h5 a').textContent;
    const productImage = card.querySelector('img').src;

    // Show loading alert
    await Swal.fire({
        title: 'Adding to Cart',
        text: 'Please wait...',
        icon: 'info',
        showConfirmButton: false,
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading();
        },
        timer: 1000
    });

    // Show success alert
    await Swal.fire({
        title: 'Added to Cart!',
        text: `${productName} has been added to your cart`,
        icon: 'success',
        confirmButtonText: 'Continue Shopping',
        showCancelButton: true,
        cancelButtonText: 'View Cart',
        customClass: {
            confirmButton: 'btn btn-primary',
            cancelButton: 'btn btn-secondary'
        }
    }).then((result) => {
        if (!result.isConfirmed) {
            // If user clicks "View Cart", redirect to cart page
            window.location.href = '/cart';
        }
    });
}
