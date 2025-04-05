const handleSubmit = (event) => {
    event.preventDefault();
    const symbol = document.getElementById('symbol').value
    return window.location.href = `/plot/${symbol}`
}