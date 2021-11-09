// JS Sources

function getFormCreate(){

    let modalBody = document.querySelector("#modalCreateForm")

    fetch("add-sources", {
        method: "GET",
        credentials: "include",
        })
    .then(response => {response.text()
    .then(data => modalBody.innerHTML = data)})
    .catch(e => console.log(e))
}

function createSource(){

    let form = document.querySelector("#formCreate")
    let formData = new FormData(form)

    fetch("add-sources", {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {response.json()
    .then(data => console.log(data))
    document.location.reload(true)
        })
    .catch(e => console.log(e))
}


function getFormEditSource(pk=0){
    
    let modalBody = document.querySelector("#modalEditForm")

    fetch(`edit-sources/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log(e))

}

function submitFormEditSource(pk=0){

    let form = document.querySelector("#formEditSource")    
    let formData = new FormData(form)

    fetch(`edit-sources/${pk}`, {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {
        response.json()
        .then(data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log(e))
    
}

function delSource(pk=0){
    fetch(`del-sources/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log(e))
}
    
// JS Entry

function getFormCreateEntry(){
    let modalBody = document.querySelector("#modalCreateForm")

    fetch("add-entries", {
        method: "GET",
        credentials: "include",
        })
    .then(response => {response.text()
    .then(data => modalBody.innerHTML = data)})
    .catch(e => console.log(e))
}

function createEntries(){

    let form = document.querySelector("#formCreateEntries")
    let formData = new FormData(form)

    fetch("add-entries", {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {response.json()
    .then(data => console.log(data))
    document.location.reload(true)
        })
    .catch(e => console.log(e))
}


function getFormEditEntries(pk=0){
    
    let modalBody = document.querySelector("#modalEditForm")

    fetch(`edit-entries/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log(e))

}

function submitEditFormEntries(pk=0){

    let form = document.querySelector("#formEditEntries")
    let formData = new FormData(form)

    fetch(`edit-entries/${pk}`, {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {
        response.json()
        .then(data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log(e))
}

function delEntry(pk=0){
    fetch(`del-entries/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log(e))
}

// Invoices


function getDetailsInvoices(pk=0){

    let modalBody = document.querySelector("#modalDetail")

    fetch(`invoices-details/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log(e))
}


function delInvoices(pk=0){
    fetch(`del-invoices/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log(e))
}